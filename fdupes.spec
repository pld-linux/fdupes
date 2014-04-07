Summary:	Program identifying or deleting duplicate files
Summary(pl.UTF-8):	Program identyfikujący lub usuwający duplikaty plików
Name:		fdupes
Version:	1.51
Release:	1
License:	MIT
Group:		Applications/File
Source0:	https://fdupes.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	47d0410c90c9e51e450933ba35a32b62
Patch0:		%{name}-make.patch
URL:		https://code.google.com/p/fdupes/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fdupes is a program to scan directories for duplicate files, with
options to list and delete them. It first compares file sizes and MD5
signatures, and then performs a byte-by-byte check for verification.

%description -l pl.UTF-8
fdupes to program przeszukujący katalogi pod kątem duplikatów plików z
możliwością wypisania lub usunięcia ich. Najpierw porównuje rozmiary
plików i sygnatury MD5, a następnie przeprowadza sprawdzenie bajt po
bajcie w celu weryfikacji.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	COMPILER_OPTIONS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	PREFIX=%{_prefix} \
	INSTALL="install -p" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CONTRIBUTORS README TODO
%attr(755,root,root) %{_bindir}/fdupes
%{_mandir}/man1/fdupes.1*

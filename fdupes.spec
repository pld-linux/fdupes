Summary:	Program identifying or deleting duplicate files
Summary(pl.UTF-8):	Program identyfikujący lub usuwający duplikaty plików
Name:		fdupes
Version:	1.40
Release:	1
License:	MIT
Group:		Applications/File
Source0:	http://netdial.caribe.net/~adrian2/programs/%{name}-%{version}.tar.gz
# Source0-md5:	11de9ab4466089b6acbb62816b30b189
Patch0:		%{name}-make.patch
URL:		http://netdial.caribe.net/~adrian2/fdupes.html
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
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CONTRIBUTORS README TODO
%attr(755,root,root) %{_bindir}/fdupes
%{_mandir}/man1/fdupes.1*

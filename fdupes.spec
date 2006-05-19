Summary:	Program identifying or deleting duplicate files
Name:		fdupes
Version:	1.40
Release:	0.1
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

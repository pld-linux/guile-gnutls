Summary:	Guile bindings for GnuTLS
Summary(pl.UTF-8):	Wiązania Guile do GnuTLS
Name:		guile-gnutls
Version:	5.0.1
Release:	1
License:	LGPL v2.1+ (library), FDL v1.3+ (documentation)
Group:		Development/Languages
Source0:	https://ftp.gnu.org/gnu/gnutls/%{name}-%{version}.tar.gz
# Source0-md5:	32084c6251713db026ad13e5e399be7b
Patch0:		%{name}-info.patch
URL:		https://gitlab.com/gnutls/guile
BuildRequires:	gc-devel >= 7.3
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	gmp-devel >= 4.1
BuildRequires:	gnutls-devel >= 3.7.9
BuildRequires:	guile >= 5:3.0
BuildRequires:	guile-devel >= 5:3.0
BuildRequires:	libffi-devel
BuildRequires:	libunistring-devel >= 0.9.3
BuildRequires:	pkgconfig
BuildRequires:	texinfo
Requires:	gnutls-libs >= 3.7.9
Requires:	guile-libs >= 5:3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautostrip	.*\.go

%description
Guile bindings for GnuTLS.

%description -l pl.UTF-8
Wiązania Guile do GnuTLS.

%prep
%setup -q
%patch -P0 -p1

%build
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/guile/3.*/extensions/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/guile/3.*/extensions/guile-gnutls-v-2.so*
%{_libdir}/guile/3.*/site-ccache/gnutls.go
%{_libdir}/guile/3.*/site-ccache/gnutls
%{_datadir}/guile/site/3.*/gnutls.scm
%{_datadir}/guile/site/3.*/gnutls
%{_infodir}/gnutls-guile.info*

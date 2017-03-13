Name:           ea-apache24-mod_xsendfile
Version:        0.12
%define 		release_prefix 1
Release: 		%{release_prefix}%{?dist}.cpanel
Summary:        A small Apache2 module that processes X-SENDFILE headers
Group:          System Environment/Daemons
License:        Apache
URL:            http://tn123.ath.cx/mod_xsendfile/
Source0:        https://github.com/nmaier/mod_xsendfile/archive/0.12.tar.gz
Source1:		300-mod_xsendfile.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ea-apache24-devel
Requires:       ea-apache24 ea-apache24-devel

%description
mod_xsendfile is a small Apache2 module that processes X-SENDFILE
headers registered by the original output handler.

If it encounters the presence of such header it will discard all
output and send the file specified by that header instead using Apache
internals including all optimizations like caching-headers and
sendfile or mmap if configured.

It is useful for processing script-output of e.g. php, perl or any
cgi.

%prep
%setup -q


%build
apxs -c mod_xsendfile.c


%install
rm -rf $RPM_BUILD_ROOT
LEXEC=$(apxs -q LIBEXECDIR)
install -d -m 0755 "${RPM_BUILD_ROOT}${LEXEC}"
apxs -S LIBEXECDIR="${RPM_BUILD_ROOT}${LEXEC}" -i mod_xsendfile.la

install -d -m 0755 "${RPM_BUILD_ROOT}/%{_docdir}/%{name}-%{version}"
install -m 0644 docs/* "${RPM_BUILD_ROOT}/%{_docdir}/%{name}-%{version}"

install -d -m 0755 %{buildroot}%{_sysconfdir}/apache2/conf.modules.d
%{__install} -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/apache2/conf.modules.d/300-mod_xsendfile.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/apache2/modules/mod_xsendfile.so
%{_sysconfdir}/apache2/conf.modules.d/300-mod_xsendfile.conf
%doc
%{_docdir}/%{name}-%{version}


%changelog
* Mon Mar 13 2017 Jacob Perkins <jacob.perkins@cpanel.net> - 0.12-1
- Initial commit
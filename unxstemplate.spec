Summary:	A small static library for unxsVZ templates
Name:		unxstemplate
Version:	1.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://unixservice.com/source/libs/%{name}-%{version}.tar.gz
# Source0-md5:	d29b0cbd6601197a99b04b216f78aedf
Patch0:		%{name}-DESTDIR.patch
URL:		http://unixservice.com/unxstemplate
BuildRequires:	mysql-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library used by many unxsVZ C cgi programs for file and stream
creation based on templates with simple {{var}} substitution and
complex and multiline char data that is provided by externally defined
functions that replace {{funcX}} in templates. These functions can
recursively call other templates. Templates are stored in unxsVZ
application MySQL tTemplate tables.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir} \
	includedir=%{_includedir}
%clean

%files
%defattr(644,root,root,755)
%doc README LICENSE
%dir %{_libdir}/openisp
%{_libdir}/openisp/libtemplate.a
%dir %{_includedir}/openisp
%{_includedir}/openisp/template.h

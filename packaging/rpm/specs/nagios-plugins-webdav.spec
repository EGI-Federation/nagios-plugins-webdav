%global debug_package %{nil}

Name:           nagios-plugins-webdav
Version:        0.2.1
Release:        1%{?dist}
Summary:        Nagios Plugin - check_webdav
Group:          Applications/Internet
License:        ASL 2.0
Source0:        %{name}-%{version}.tar.gz
URL:            https://gitlab.cern.ch/lcgdm/nagios-plugins-webdav
BuildArch:      x86_64

Requires:       time
Requires:       pycurl
Requires:       python-GridMon
Requires:       voms-clients3

%description
This package provides a nagios plugin to test the webdav interface of an endpoint.

The endpoint should permit an authenticated user to perform file access and management
operations to successfully pass this test.

%prep
%setup -q
# %{!?__python2: %global __python2 /usr/bin/python2}
# %{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

%build

%install
mkdir -p %{buildroot}%{_libdir}/nagios/plugins
cp --preserve=timestamps src/check_webdav %{buildroot}%{_libdir}/nagios/plugins

%files
%{_libdir}/nagios/plugins/check_webdav
%doc LICENSE
%doc README.md


%clean
rm -rf %{buildroot}

%changelog
* Thu Dec 03 2015 Georgios Bitzes <georgios.bitzes@cern.ch> - 0.2.0
- Change package dependency to voms-clients3
* Thu Dec 03 2015 Georgios Bitzes <georgios.bitzes@cern.ch> - 0.2.0
- Ready for preprod etf
* Mon Sep 28 2015 Georgios Bitzes <georgios.bitzes@cern.ch> - 0.1
- Initial build

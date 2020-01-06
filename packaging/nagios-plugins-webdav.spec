%global debug_package %{nil}

Name:           nagios-plugins-webdav
Version:        0.4.3
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

%if %{?rhel}%{!?rhel:0} >= 7
Requires:       voms-clients
%else
Requires:       voms-clients3
%endif

Requires:       nmap

%description
This package provides a nagios plugin to test the webdav interface of an endpoint.

The endpoint should permit an authenticated user to perform file access and management
operations to successfully pass this test.

%prep
%setup -q

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
* Mon Jan 06 2020 Georgios Bitzes <georgios.bitzes@cern.ch> - 0.4.3
- Implement --fixed-content-length and --dynafed flags.
- Show last contacted IP.
* Mon Sep 09 2019 Georgios Bitzes <georgios.bitzes@cern.ch> - 0.4.2
- Support "access-control-allow-methods" in OPTIONS output for compatibility with dCache
* Mon Mar 11 2019 Georgios Bitzes <georgios.bitzes@cern.ch> - 0.4.1
- Fix parsing of nmap ssl-enum-ciphers on CentOS7
* Mon May 02 2016 Georgios Bitzes <georgios.bitzes@cern.ch> - 0.4.0
- Bugfix, skipped tests were triggering a slow warning
* Wed Apr 13 2016 Georgios Bitzes <georgios.bitzes@cern.ch> - 0.3.9
- Bugfix, nmap would check the wrong ports
* Tue Apr 12 2016 Georgios Bitzes <georgios.bitzes@cern.ch> - 0.3.8
- Add TLS ciphers test
* Tue Mar 29 2016 Georgios Bitzes <georgios.bitzes@cern.ch> - 0.3.7
- Better error reporting, small delay after a PUT
* Tue Mar 22 2016 Georgios Bitzes <georgios.bitzes@cern.ch> - 0.3.5
- Bugfix: Mark overall result as slow even for a non-critical test
* Tue Mar 22 2016 Georgios Bitzes <georgios.bitzes@cern.ch> - 0.3.4
- Add no-cleanup flag, increase default failure timeout
* Mon Mar 21 2016 Georgios Bitzes <georgios.bitzes@cern.ch> - 0.3.3
- Sanitize sensitive URL parameters
* Mon Mar 21 2016 Georgios Bitzes <georgios.bitzes@cern.ch> - 0.3.2
- Print redirected URL
* Thu Mar 17 2016 Georgios Bitzes <georgios.bitzes@cern.ch> - 0.3.1
- Issue a PUT with "Expect: 100-Continue"
* Wed Feb 23 2016 Georgios Bitzes <georgios.bitzes@cern.ch> - 0.3.0
- Improve detection of accumulated testfiles
* Wed Feb 23 2016 Georgios Bitzes <georgios.bitzes@cern.ch> - 0.2.9
- Fix automatic cleanup of accumulated testfiles
* Wed Feb 23 2016 Georgios Bitzes <georgios.bitzes@cern.ch> - 0.2.8
- Mark "DELETE on non-existent" test as non-critical
* Wed Feb 03 2016 Georgios Bitzes <georgios.bitzes@cern.ch> - 0.2.7
- Add DELETE on non-existent test, expecting 404
* Wed Jan 20 2016 Georgios Bitzes <georgios.bitzes@cern.ch> - 0.2.6
- Mark a failed PUT as WARNING, not CRITICAL
* Tue Jan 19 2016 Georgios Bitzes <georgios.bitzes@cern.ch> - 0.2.5
- Add --no-crls option to workaround a strange bug where libcurl/NSS reports "SSL connect error"
* Tue Jan 12 2016 Georgios Bitzes <georgios.bitzes@cern.ch> - 0.2.4
- Remove test numbers, force TLS v1
* Wed Dec 16 2015 Georgios Bitzes <georgios.bitzes@cern.ch> - 0.2.2
- Add test numbers to have nagios sort them properly
* Thu Dec 03 2015 Georgios Bitzes <georgios.bitzes@cern.ch> - 0.2.1
- Change package dependency to voms-clients3
* Thu Dec 03 2015 Georgios Bitzes <georgios.bitzes@cern.ch> - 0.2.0
- Ready for preprod etf
* Mon Sep 28 2015 Georgios Bitzes <georgios.bitzes@cern.ch> - 0.1
- Initial build

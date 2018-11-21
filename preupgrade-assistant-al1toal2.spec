%{!?sys_python_sitelib: %global sys_python_sitelib %(%{__sys_python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?sys_python_sitearch: %global sys_python_sitearch %(%{__sys_python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           preupgrade-assistant-al1toal2
Version:        0.0.1
Release:        1%{?dist}
Summary:        Modules used by preupgrade-assistant from AL1 to AL2
Group:          System Environment/Libraries
License:        ASL 2.0
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  preupgrade-assistant-tools
Requires:       preupgrade-assistant
Requires:       bash
Requires:       %{sys_python_pkg}


%description
This package contains modules which can be used to test
your system for upgrade compatibility between
the Amazon Linux 2018.03 release and
the Amazon Linux 2 General Availability release.


%prep
%setup -q -n %{name}-%{version}


%build
preupg-xccdf-compose AL1_AL2


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p -m 755 $RPM_BUILD_ROOT%{_datadir}/doc/preupgrade-assistant-al1toal2
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/preupgrade
mv LICENSE $RPM_BUILD_ROOT%{_datadir}/doc/preupgrade-assistant-al1toal2/
mv AL1_AL2-results $RPM_BUILD_ROOT%{_datadir}/preupgrade/AL1_AL2
rm -rf $RPM_BUILD_ROOT/%{_datadir}/preupgrade/common


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir %{_datadir}/doc/preupgrade-assistant-al1toal2/
%doc %{_datadir}/doc/preupgrade-assistant-al1toal2/LICENSE
%dir %{_datadir}/preupgrade/AL1_AL2/
%{_datadir}/preupgrade/AL1_AL2/


%changelog

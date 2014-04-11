%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

Name:           pytap13
Version:        0.0.3
Release:        1%{?dist}
Summary:        Python parser for the Test Anything Protocol (TAP) version 13

License:        GPLv2+
URL:            https://bitbucket.org/fedoraqa/pytap13
Source0:        https://qadevel.cloud.fedoraproject.org/releases/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python-yamlish
BuildRequires:  python2-devel python-setuptools

%description
Python parser for the Test Anything Protocol (TAP) version 13

%prep
%setup -q

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%doc README.md
%{python_sitelib}/pytap13.*
%{python_sitelib}/*.egg-info

%changelog
* Fri Apr 11 2014 Tim Flink <tflink@fedoraproject.org> - 0.0.3-1
- initial packaging

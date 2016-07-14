%global pypi_name cotyledon

%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-%{pypi_name}
Version:        1.2.5
Release:        0.1.pre_review%{?dist}
Summary:        Cotyledon provides a framework for defining long-running services

License:        ASL 2.0
URL:            https://cotyledon.readthedocs.io
Source0:        https://pypi.io/packages/source/c/cotyledon/cotyledon-1.2.5.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pbr

Requires:  python-setproctitle

%description
Cotyledon provides a framework for defining long-running services.


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove tests
rm -rf %{pypi_name}/tests

%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%{_bindir}/%{pypi_name}-example


%changelog
* Thu Jul 14 2016 Alan Pevec <apevec AT redhat.com> - 1.2.5-0.1.pre_review
- drop tests, docs, py3 for the initial CloudSIG build

* Thu Jul 14 2016 Pradeep Kilambi <pkilambi@redhat.com> - 1.2.3-2
- Fix source url

* Wed Jul 6 2016 Mehdi Abaakouk <sileht@redhat.com> - 1.2.3-1
- Initial package.

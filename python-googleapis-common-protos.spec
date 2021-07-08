%global srcname googleapis-common-protos

Name:           python-%{srcname}
Version:        1.53.0
Release:        3%{?dist}
Summary:        Common protobufs used in Google APIs

License:        ASL 2.0
URL:            https://github.com/googleapis/python-api-common-protos/
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%generate_buildrequires
# Let’s not install the “grpc” extra here if we can help it. That would add a
# BR on python3dist(grpcio), but this package is required by
# python3dist(grpcio-status), which would create a circular dependency with
# grpc.
%pyproject_buildrequires -r


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{common_description}


%pyproject_extras_subpkg -n python3-%{srcname} grpc


%prep
%autosetup -n python-api-common-protos-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files google


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%doc README.md

%{python3_sitelib}/googleapis_common_protos-%{version}-py%{python3_version}-nspkg.pth


%changelog
* Thu Jul 08 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.53.0-3
- Tweak how the description macro is written
- Drop obsolete python_provide macro
- Switch to pyproject-rpm-macros
- Add the metapackage for the “grpc” extra

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.53.0-2
- Rebuilt for Python 3.10

* Sun Mar 21 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.53.0-1
- Update to 1.53.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.52.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.52.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 18 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.52.0-1
- Update to 1.52.0

* Sun May 31 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.51.0-2
- Rebuild for Python 3.9

* Fri May 29 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.51.0-1
- Initial RPM release

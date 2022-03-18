# When bootstrapping, we do not include the “grpc” extra in the BR’s. That adds
# a BR on python3dist(grpcio), but this package is required by
# python3dist(grpcio-status), which creates a circular dependency with grpc.
%bcond_with bootstrap

Name:           python-googleapis-common-protos
Version:        1.56.0
Release:        %autorelease
Summary:        Common protobufs used in Google APIs

License:        ASL 2.0
URL:            https://github.com/googleapis/python-api-common-protos/
Source0:        %{url}/archive/v%{version}/googleapis-common-protos-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n python3-googleapis-common-protos
Summary:        %{summary}

%description -n python3-googleapis-common-protos %{common_description}


%pyproject_extras_subpkg -n python3-googleapis-common-protos grpc


%prep
%autosetup -n python-api-common-protos-%{version}


%generate_buildrequires
%pyproject_buildrequires -r %{?!with_bootstrap:-x grpc}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files google


%check
# Upstream has no tests.
#
# Note that google and google.logging are namespace packages.
%pyproject_check_import %{?with_bootstrap:-e 'google.longrunning.*grpc*'}


%files -n python3-googleapis-common-protos -f %{pyproject_files}
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%doc CODE_OF_CONDUCT.md
%doc README.md

%{python3_sitelib}/googleapis_common_protos-%{version}-py%{python3_version}-nspkg.pth


%changelog
%autochangelog

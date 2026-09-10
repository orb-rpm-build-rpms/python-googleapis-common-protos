%bcond tests 1

# When bootstrapping, we do not include the “grpc” extra in the BR’s. That adds
# a BR on python3dist(grpcio), but this package is required by
# python3dist(grpcio-status), which creates a circular dependency with grpc.
%bcond_with bootstrap

Name:           python-googleapis-common-protos
# Bumped from Fedora's 1.63.0: that release caps protobuf below 6.0 (upstream
# setup.py plus the pull/212 patch), which cannot resolve against the protobuf
# 6.33.5 we package. 1.75.3 requires protobuf>=6.33.5,<8.0.0 upstream, matching
# the packaged protobuf exactly, so the downstream cap patch is no longer needed.
Version:        1.75.3
Release:        %autorelease
Summary:        Common protobufs used in Google APIs

License:        Apache-2.0
URL:            https://github.com/googleapis/python-api-common-protos
# The upstream GitHub repo only tags through v1.66.0 (which still caps protobuf
# below 6.0); releases 1.68+ are published to PyPI only, so take the sdist from
# there. It ships tests/unit, so %%check is unaffected.
Source:         https://files.pythonhosted.org/packages/source/g/googleapis-common-protos/googleapis_common_protos-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n python3-googleapis-common-protos
Summary:        %{summary}

%description -n python3-googleapis-common-protos %{common_description}


%pyproject_extras_subpkg -n python3-googleapis-common-protos grpc


%prep
# The PyPI sdist unpacks to googleapis_common_protos-%%{version} rather than the
# GitHub archive's python-api-common-protos-%%{version}.
%autosetup -n googleapis_common_protos-%{version}


%generate_buildrequires
%pyproject_buildrequires %{?!with_bootstrap:-x grpc}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l google


%check
%if %{with tests}
# NOTE(mhayden): Setting PYTHONUSERBASE as a hack for PEP 420 namespaces.
# Thanks to churchyard for the fix.
PYTHONUSERBASE=%{buildroot}%{_prefix} \
    %pytest tests/unit
%endif


%files -n python3-googleapis-common-protos -f %{pyproject_files}
# The PyPI sdist does not ship CHANGELOG.md, only README.rst.
%doc README.rst


%changelog
%autochangelog

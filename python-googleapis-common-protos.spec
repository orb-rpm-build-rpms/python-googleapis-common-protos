%global srcname googleapis-common-protos

# When bootstrapping, we do not include the “grpc” extra in the BR’s. That adds
# a BR on python3dist(grpcio), but this package is required by
# python3dist(grpcio-status), which creates a circular dependency with grpc.
%bcond_with bootstrap

Name:           python-%{srcname}
Version:        1.53.0
Release:        %autorelease
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
%if %{without bootstrap}
%pyproject_buildrequires -x grpc
%else
%pyproject_buildrequires -r
%endif


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


%check
# Upstream has no tests.
#
# Note that google and google.logging are namespace packages.
%{py3_check_import google.api
     google.api.annotations_pb2
     google.api.auth_pb2
     google.api.backend_pb2
     google.api.billing_pb2
     google.api.client_pb2
     google.api.config_change_pb2
     google.api.consumer_pb2
     google.api.context_pb2
     google.api.control_pb2
     google.api.distribution_pb2
     google.api.documentation_pb2
     google.api.endpoint_pb2
     google.api.field_behavior_pb2
     google.api.httpbody_pb2
     google.api.http_pb2
     google.api.label_pb2
     google.api.launch_stage_pb2
     google.api.logging_pb2
     google.api.log_pb2
     google.api.metric_pb2
     google.api.monitored_resource_pb2
     google.api.monitoring_pb2
     google.api.quota_pb2
     google.api.resource_pb2
     google.api.service_pb2
     google.api.source_info_pb2
     google.api.system_parameter_pb2
     google.api.usage_pb2
     google.gapic
     google.gapic.metadata
     google.gapic.metadata.gapic_metadata_pb2
     google.logging.type
     google.logging.type.http_request_pb2
     google.logging.type.log_severity_pb2
     google.longrunning
     google.longrunning.operations_pb2
     google.longrunning.operations_proto_pb2
     google.longrunning.operations_proto
     google.rpc
     google.rpc.code_pb2
     google.rpc.error_details_pb2
     google.rpc.status_pb2
     google.rpc.context
     google.rpc.context.attribute_context_pb2
     google.type
     google.type.calendar_period_pb2
     google.type.color_pb2
     google.type.date_pb2
     google.type.datetime_pb2
     google.type.dayofweek_pb2
     google.type.expr_pb2
     google.type.fraction_pb2
     google.type.latlng_pb2
     google.type.money_pb2
     google.type.month_pb2
     google.type.postal_address_pb2
     google.type.quaternion_pb2
     google.type.timeofday_pb2}

%if %{without bootstrap}
%{py3_check_import google.longrunning.operations_grpc_pb2
    google.longrunning.operations_grpc
    google.longrunning.operations_pb2_grpc}
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%doc README.md

%{python3_sitelib}/googleapis_common_protos-%{version}-py%{python3_version}-nspkg.pth


%changelog
%autochangelog

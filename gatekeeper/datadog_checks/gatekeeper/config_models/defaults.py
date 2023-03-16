# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>

from datadog_checks.base.utils.models.fields import get_default_field_value


def shared_proxy(field, value):
    return get_default_field_value(field, value)


def shared_service(field, value):
    return get_default_field_value(field, value)


def shared_skip_proxy(_field, _value):
    return False


def shared_timeout(_field, _value):
    return 10


def instance_allow_redirects(_field, _value):
    return True


def instance_auth_token(field, value):
    return get_default_field_value(field, value)


def instance_auth_type(_field, _value):
    return 'basic'


def instance_aws_host(field, value):
    return get_default_field_value(field, value)


def instance_aws_region(field, value):
    return get_default_field_value(field, value)


def instance_aws_service(field, value):
    return get_default_field_value(field, value)


def instance_bearer_token_auth(field, value):
    return get_default_field_value(field, value)


def instance_bearer_token_path(field, value):
    return get_default_field_value(field, value)


def instance_bearer_token_refresh_interval(_field, _value):
    return 60


def instance_connect_timeout(field, value):
    return get_default_field_value(field, value)


def instance_disable_generic_tags(_field, _value):
    return False


def instance_empty_default_hostname(_field, _value):
    return False


def instance_exclude_labels(field, value):
    return get_default_field_value(field, value)


def instance_extra_headers(field, value):
    return get_default_field_value(field, value)


def instance_headers(field, value):
    return get_default_field_value(field, value)


def instance_health_service_check(_field, _value):
    return True


def instance_ignore_metrics(field, value):
    return get_default_field_value(field, value)


def instance_ignore_metrics_by_labels(field, value):
    return get_default_field_value(field, value)


def instance_ignore_tags(field, value):
    return get_default_field_value(field, value)


def instance_include_labels(field, value):
    return get_default_field_value(field, value)


def instance_kerberos_auth(_field, _value):
    return 'disabled'


def instance_kerberos_cache(field, value):
    return get_default_field_value(field, value)


def instance_kerberos_delegate(_field, _value):
    return False


def instance_kerberos_force_initiate(_field, _value):
    return False


def instance_kerberos_hostname(field, value):
    return get_default_field_value(field, value)


def instance_kerberos_keytab(field, value):
    return get_default_field_value(field, value)


def instance_kerberos_principal(field, value):
    return get_default_field_value(field, value)


def instance_label_joins(field, value):
    return get_default_field_value(field, value)


def instance_label_to_hostname(field, value):
    return get_default_field_value(field, value)


def instance_labels_mapper(field, value):
    return get_default_field_value(field, value)


def instance_log_requests(_field, _value):
    return False


def instance_metric_patterns(field, value):
    return get_default_field_value(field, value)


def instance_metrics(field, value):
    return get_default_field_value(field, value)


def instance_min_collection_interval(_field, _value):
    return 15


def instance_namespace(_field, _value):
    return 'service'


def instance_ntlm_domain(field, value):
    return get_default_field_value(field, value)


def instance_password(field, value):
    return get_default_field_value(field, value)


def instance_persist_connections(_field, _value):
    return False


def instance_prometheus_metrics_prefix(field, value):
    return get_default_field_value(field, value)


def instance_proxy(field, value):
    return get_default_field_value(field, value)


def instance_read_timeout(field, value):
    return get_default_field_value(field, value)


def instance_request_size(_field, _value):
    return 10


def instance_send_distribution_buckets(_field, _value):
    return False


def instance_send_distribution_counts_as_monotonic(_field, _value):
    return False


def instance_send_distribution_sums_as_monotonic(_field, _value):
    return False


def instance_send_histograms_buckets(_field, _value):
    return True


def instance_send_monotonic_counter(_field, _value):
    return True


def instance_send_monotonic_with_gauge(_field, _value):
    return False


def instance_service(field, value):
    return get_default_field_value(field, value)


def instance_skip_proxy(_field, _value):
    return False


def instance_tags(field, value):
    return get_default_field_value(field, value)


def instance_timeout(_field, _value):
    return 10


def instance_tls_ca_cert(field, value):
    return get_default_field_value(field, value)


def instance_tls_cert(field, value):
    return get_default_field_value(field, value)


def instance_tls_ignore_warning(_field, _value):
    return False


def instance_tls_private_key(field, value):
    return get_default_field_value(field, value)


def instance_tls_protocols_allowed(field, value):
    return get_default_field_value(field, value)


def instance_tls_use_host_header(_field, _value):
    return False


def instance_tls_verify(_field, _value):
    return True


def instance_type_overrides(field, value):
    return get_default_field_value(field, value)


def instance_use_legacy_auth_encoding(_field, _value):
    return True


def instance_use_process_start_time(_field, _value):
    return False


def instance_username(field, value):
    return get_default_field_value(field, value)

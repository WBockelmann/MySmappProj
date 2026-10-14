{% macro get_version() %}

  {% do log("The installed version of dbt is (called by macro): " ~ dbt_version, info=true) %}

{% endmacro %}
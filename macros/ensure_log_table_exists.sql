{%- macro ensure_log_table_exists() -%}
	{%- set log_tbl_ddl -%}
		create table if not exists raw.core.dbt_run_logs( Action varchar, create_ts timestamp(9))
	{%- endset -%}
	{%- do run_query( log_tbl_ddl ) -%}
{%- endmacro -%}


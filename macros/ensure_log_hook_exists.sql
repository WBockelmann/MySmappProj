{%- macro ensure_log_hook_exists() -%}
	{%- set log_tbl_ddl -%}
		create table if not exists raw.core.hooks_log( hook_type varchar, table_name varchar, executed_at timestamp(9))
	{%- endset -%}
	{%- do run_query( log_tbl_ddl ) -%}
{%- endmacro -%}


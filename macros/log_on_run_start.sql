{%- macro log_on_run_start() -%}
	insert into raw.core.dbt_run_logs( Action , create_ts )
	values( 'on_run_start' , current_timestamp )
	;
{%- endmacro -%}
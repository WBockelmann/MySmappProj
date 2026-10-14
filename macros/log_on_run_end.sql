{%- macro log_on_run_end() -%}
	insert into raw.core.dbt_run_logs( Action , create_ts )
	values( 'on_run_end' , current_timestamp )
	;
{%- endmacro -%}
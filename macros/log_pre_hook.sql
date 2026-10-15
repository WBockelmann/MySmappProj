{%- macro log_pre_hook(schema_name , table_name ) -%}
	insert into raw.core.dbt_hook_logs( hook_type , table_name , executed_at )
	values( 'pre-hook' , concat('{{schema_name}}' , concat('.' , '{{table_name}}' ) ) , current_timestamp )
	;
{%- endmacro -%}

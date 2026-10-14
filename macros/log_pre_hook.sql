{%- macro log_pre_hook(schema_name , tab_name) -%}
	insert into raw.core.hooks_log( hook_type , table_name , executed_at )
	values( 'pre-hook' , concat('{{schema_name}}' , concat('.' , '{{table_name}}' ) ) , current_timestamp )
	;
{%- endmacro -%}

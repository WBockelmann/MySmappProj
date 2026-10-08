select *
from {{ ref('select_customer_data_cpy') }}
where last_name = 'M.'
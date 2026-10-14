{{ config(pre_hook="{{ log_pre_hook(this.schema , this.name) }}" , post_hook="{{ log_post_hook(this.schema , this.name) }}") }}


select  *
from    {{ ref('SELEKTEN_1') }}

union

select  *
from    {{ ref('SELEKTEN_2') }}



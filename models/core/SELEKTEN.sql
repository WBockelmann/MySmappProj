

select  *
from    {{ ref('SELEKTEN_1') }}

union

select  *
from    {{ ref('SELEKTEN_2') }}



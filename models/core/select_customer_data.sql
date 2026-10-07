select    hubc.hk_customer
        , satc.first_name
        , satc.last_name
        , satc.record_source

from raw.core.hub_customer hubc
     join raw.core.sat_customer satc 
       on satc.hk_customer = hubc.hk_customer


       

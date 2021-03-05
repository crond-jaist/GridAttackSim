name = ns3_1 
time_delta = 1ns 
broker = tcp://localhost:5570 
values 
    fncs_msg/HOUSE_1@Market_1/submit_bid_state
        topic = fncs_msg/HOUSE_1@Market_1/submit_bid_state
        default = ""
        type = string
        list = false
    fncs_msg/Market_1@HOUSE_1/clearPrice 
        topic = fncs_msg/Market_1@HOUSE_1/clearPrice 
        default = "" 
        ttype = string 
        list = false 
    fncs_msg/Market_1@HOUSE_1/mktID 
        topic = fncs_msg/Market_1@HOUSE_1/mktID 
        default = "" 
        type = string 
        list = false 
    fncs_msg/Market_1@HOUSE_1/avgPrice 
        topic = fncs_msg/Market_1@HOUSE_1/avgPrice 
        default = "" 
        type = string 
        list = false 
    fncs_msg/Market_1@HOUSE_1/stdevPrice 
        topic = fncs_msg/Market_1@HOUSE_1/stdevPrice 
        default = "" 
        type = string 
        list = false 
    fncs_msg/Market_1@HOUSE_1/clearPrice 
        topic = fncs_msg/Market_1@HOUSE_1/clearPrice 
        default = "" 
        type = string 
        list = false 

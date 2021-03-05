
outF = open("fncs_msg.txt", "w")
index = 1
line = ""
total_houses = int(raw_input("Enter Total House(s): "))
while (index <= total_houses):




    line = line + "route \"commit:Market_1.current_market.clearing_price -> HOUSE_"+str(index)+"/clearPrice; 0\";\n";
    line = line + "route \"commit:Market_1.market_id -> HOUSE_"+str(index)+"/mktID; 0\";\n";
    line = line + "route \"commit:Market_1.current_price_mean_24h -> HOUSE_"+str(index)+"/avgPrice; 0\";\n";
    line = line + "route \"commit:Market_1.current_price_mean_24h -> HOUSE_"+str(index)+"/avgPrice; 0\";\n";
    line = line + "route \"commit:Market_1.current_price_stdev_24h -> HOUSE_"+str(index)+"/stdevPrice; 0\";\n";



    line = line + "subscribe \"function:auction/submit_bid_state <- ns3_1/fncs_msg/HOUSE_"+str(index)+"@Market_1/submit_bid_state\";\n";
    line = line + "subscribe \"precommit:HOUSE_"+str(index)+".proxy_clear_price <- ns3_1/fncs_msg/Market_1@HOUSE_"+str(index)+"/clearPrice\";\n";
    line = line + "subscribe \"precommit:HOUSE_"+str(index)+".proxy_market_id <- ns3_1/fncs_msg/Market_1@HOUSE_"+str(index)+"/mktID\";\n";
    line = line + "subscribe \"precommit:HOUSE_"+str(index)+".proxy_average <- ns3_1/fncs_msg/Market_1@HOUSE_"+str(index)+"/avgPrice\";\n";
    line = line + "subscribe \"precommit:HOUSE_"+str(index)+".proxy_standard_deviation <- ns3_1/fncs_msg/Market_1@HOUSE_"+str(index)+"/stdevPrice\";\n";





    index +=1



outF.write(line)
print("Finished")

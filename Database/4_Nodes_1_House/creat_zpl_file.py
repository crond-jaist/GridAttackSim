
def main():
	outF = open("fncs.zpl", "w")
	index = 1
	total_houses = int(raw_input("Enter Total Houses: "))
	space = " "
	line = "name = ns3_1 \n"
	line = line + "time_delta = 1ns \n"
	line = line + "broker = tcp://localhost:5570 \n"
	line = line + "values \n"
	while (index <= total_houses):
	    line = line + space*4 +"fncs_msg/HOUSE_"+str(index)+"@Market_1/submit_bid_state\n"
	    line = line + space*8 +"topic = fncs_msg/HOUSE_"+str(index)+"@Market_1/submit_bid_state\n"
	    line = line + space*8 +"default = \"\"\n"
	    line = line + space*8 +"type = string\n"
	    line = line + space*8 +"list = false\n"




	    line = line + space*4 +"fncs_msg/Market_1@HOUSE_"+str(index)+"/clearPrice \n"
	    line = line + space*8 +"topic = fncs_msg/Market_1@HOUSE_"+str(index)+"/clearPrice \n"
	    line = line + space*8 +"default = \"\" \n"
	    line = line + space*8 +"ttype = string \n"
	    line = line + space*8 +"list = false \n"




	    line = line + space*4 +"fncs_msg/Market_1@HOUSE_"+str(index)+"/mktID \n"
	    line = line + space*8 +"topic = fncs_msg/Market_1@HOUSE_"+str(index)+"/mktID \n"
	    line = line + space*8 +"default = \"\" \n"
	    line = line + space*8 +"type = string \n"
	    line = line + space*8 +"list = false \n"




	    line = line + space*4 +"fncs_msg/Market_1@HOUSE_"+str(index)+"/avgPrice \n"
	    line = line + space*8 +"topic = fncs_msg/Market_1@HOUSE_"+str(index)+"/avgPrice \n"
	    line = line + space*8 +"default = \"\" \n"
	    line = line + space*8 +"type = string \n"
	    line = line + space*8 +"list = false \n"


	    line = line + space*4 +"fncs_msg/Market_1@HOUSE_"+str(index)+"/stdevPrice \n"
	    line = line + space*8 +"topic = fncs_msg/Market_1@HOUSE_"+str(index)+"/stdevPrice \n"
	    line = line + space*8 +"default = \"\" \n"
	    line = line + space*8 +"type = string \n"
	    line = line + space*8 +"list = false \n"



	    line = line + space*4 +"fncs_msg/Market_1@HOUSE_"+str(index)+"/clearPrice \n"
	    line = line + space*8 +"topic = fncs_msg/Market_1@HOUSE_"+str(index)+"/clearPrice \n"
	    line = line + space*8 +"default = \"\" \n"
	    line = line + space*8 +"type = string \n"
	    line = line + space*8 +"list = false \n"



	    index +=1



	outF.write(line)
	print("Finished")
if __name__ == '__main__':
    main()

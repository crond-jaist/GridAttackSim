filepath = 'GridLab-D_old.glm'
outF = open("GridLab-D.glm", "w")
with open(filepath) as fp:
   line = fp.readline()
   cnt = 0
   index = 1
   while line:
       #print("Line {}: {}".format(cnt, line.strip()))
       line = fp.readline()
       if line.strip() == 'object controller {':
           line = line + "\n \t name HOUSE_"+str(index)+";\n"
           line = line + "\t proxy_average 0.042676;\n"
           line = line + "\t proxy_standard_deviation 0.020000;\n"
           line = line + "\t proxy_market_id 1;\n"
           line = line + "\t proxy_clear_price 0.042676;\n"
           line = line + "\t proxy_price_cap 3.78;\n"
           index +=1
       outF.write(line)
       cnt += 1
print("Finished")

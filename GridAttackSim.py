from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import tkinter.font as tkfont
import json
import shutil
import os
import sys
import fileinput
import subprocess
from tkinter import messagebox
from tkinter import Menu
import time
import glob
import datetime
from graphviz import Source  
window = Tk()

window.title("Smart Grid Simulation")
window.option_add( "*font", "Times 14" )

window.geometry()
window.config(bg="#D6E2F3")

database_path = "Database/"


menu = Menu(window)

menu_file = Menu(menu)
menu_file.add_command(label='New', font=("Times", 11))

menu_file.add_separator()

menu_file.add_command(label='Open', font=("Times", 11))

menu_file.add_separator()

menu_file.add_command(label='Exit', font=("Times", 11))

menu.add_cascade(label='File', menu=menu_file, font=("Times", 11))

menu_documents = Menu(menu)
menu_documents.add_command(label='Document', font=("Times", 11))
menu.add_cascade(label='Document', menu=menu_documents, font=("Times", 11))


menu_help = Menu(menu)
menu_help.add_command(label='Contact Us', font=("Times", 11))
menu.add_cascade(label='Help', menu=menu_help, font=("Times", 11))

menu.config(bg='#49A')

window.config(menu=menu)






lbl = Label(window, text="Smart Grid Attack Simulation System ", font=("Times", 18), background="#D6E2F3", foreground="#000280")

lbl.grid(column=0, row=0, columnspan=2)


lbl_smartgrid_model = Label(window, text="   Smart Grid Model\n", background="#D6E2F3", foreground="#000280")
# sticky="W" left align
lbl_smartgrid_model.grid(sticky="W", column=0, row=2)
lbl_smartgrid_model.config(width=18)
combo_smartgrid_model = Combobox(window, width=35)

combo_smartgrid_model['values']= ("1 Node 255 Houses", 
	"4 Nodes 1 House", 
	"4 Nodes 492 Houses", 
	"13 Nodes 15 Houses", 
	"13 Nodes 73 Houses")

combo_smartgrid_model.current(4) #set the selected item

combo_smartgrid_model.grid(column=1, row=2)



def show_model():

    path_1 = database_path+combo_smartgrid_model.get().replace(" ", "_") + '/'+'GridLab-D.glm'
    path_2 = database_path+combo_smartgrid_model.get().replace(" ", "_") + '/'+'GridLab-D.dot'
    os.system('python glmMap.py ' + path_1 + ' ' + path_2)
    s = Source.from_file(path_2)
    s.view()
    print(os.getcwd())




btn_show_model = Button(window, text=" Show Model", command=show_model)
btn_show_model.grid(column=2, row=2)





lbl_application = Label( window, justify=LEFT, anchor="w", text="   Application\n", background="#D6E2F3", foreground="#000280")
lbl_application.grid(sticky="W", column=0, row=4)
combo_application = Combobox(window, width=35)

combo_application ['values']= ("Demand/Response (DR)", "Dynamic Pricing (DP)", "Both DR and DP")

combo_application.current(0) #set the selected item

combo_application.grid(column=1, row=4)






def on_attack_category_change(index, value, op):
    if combo_attack_category.get() == "Nefarious Activity":
        combo_attack_type['values']= ("1 - Channel Jamming - Cluster", 
        	"2 - Channel Jamming - Peer-to-Peer", 
        	"3 - DNS attacks - Cluster", 
        	"4 - DNS attacks - Peer-to-Peer", 
        	"5 - Injection Attacks - Control Systems", 
        	"6 - Injection Attacks - End-point Systems", 
        	"7 - Malicious Code - End-point Systems")
        combo_attack_type.current(0) #set the selected item
    elif combo_attack_category.get() == "Eavesdropping, Interception and Hijacking":
        combo_attack_type['values']= ("8 - Replay of Messages - Cluster", 
        	"9 - Replay of Messages - Peer-to-Peer")
        combo_attack_type.current(0) #set the selected item
    elif combo_attack_category.get() == "None":
        combo_attack_type['values']= ("None")
        combo_attack_type.current(0) #set the selected item






string_attack_category = StringVar()
string_attack_category.trace('w',on_attack_category_change)
lbl_attack_category = Label(window, text="   Attack Category\n", background="#D6E2F3", foreground="#000280")
lbl_attack_category.grid(sticky="W", column=0, row=6)
combo_attack_category = Combobox(window, textvar=string_attack_category, width=35)

combo_attack_category['values']= ("None","Nefarious Activity", "Eavesdropping, Interception and Hijacking")




combo_attack_category.grid(column=1, row=6)







lbl_attack_type = Label(window, text="   Attack Type\n", background="#D6E2F3", foreground="#000280")
lbl_attack_type.grid(sticky="W", column=0, row=8)
combo_attack_type = Combobox(window, width=35)


combo_attack_type.grid(column=1, row=8)






#Check Process is running or not
def is_running(pid):        
    try:
        os.kill(pid, 0)
    except OSError:
        return False

    return True

def run():
    messagebox.showinfo("Message", "The simulation is running")
    string_code = 'python attack_broker.py ' + database_path+combo_smartgrid_model.get().replace(" ", "_") + '/ '+ combo_attack_type.get()[0:1]

    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    os.system(string_code)

    messagebox.showinfo("Message", "The simulation has been finished")
    os.chdir(database_path+combo_smartgrid_model.get().replace(" ", "_") + '/')
    os.system('mv baseprice_clearedprice_clearedquantity.csv ' + 'price_' +combo_attack_type.get().replace(" ", "_").replace("-", "")+'_'+ current_time + '.csv')
   
    os.system('mv totalload.csv ' + 'totalload_' +combo_attack_type.get().replace(" ", "_").replace("-", "")+'_'+ current_time + '.csv')

    os.chdir("..")
    os.chdir("..")





def result():
    Lb_files.delete(0, END)
    path = database_path+combo_smartgrid_model.get().replace(" ", "_") + '/'
    extension = 'csv'
    print(os.getcwd())
    os.chdir(path)
    file_list = glob.glob('*.{}'.format(extension))
    #print(file_list)
    j = 0
    if combo_application.get() == "Demand/Response (DR)":
        for i in range(len(file_list)):
            if(file_list[i][0]=="t"):
                #print(file_list[i].find('totalload'))
                Lb_files.insert(j, file_list[i])
                j = j+1
    elif combo_application.get() == "Dynamic Pricing (DP)":
        for i in range(len(file_list)):
            if(file_list[i][0]=="p"):
                #print(file_list[i].find('baseprice'))
                Lb_files.insert(j, file_list[i])
                j = j+1
    else:
        for i in range(len(file_list)):
            if(file_list[i][0]=="p" or file_list[i][0]=="t"):
                Lb_files.insert(j, file_list[i])
                j = j+1
    os.chdir("..")
    os.chdir("..")



btn_run = Button(window, text="Run Simulation", command=run)
btn_run.grid(column=0, row=10)


btn_result= Button(window, text="Load Results", command=result)
btn_result.grid(column=1, row=10)


lbl_result = Label(window, text="\nSimulation Results", font=("Times", 18), background="#D6E2F3", foreground="#000280")

lbl_result.grid(column=0, row=11, columnspan=2)
lbl_files = Label(window, text="Output Files", background="#D6E2F3", foreground="#000280")
lbl_files.grid(column=0, row=12)




Lb_files = Listbox(window, width=35, selectmode=MULTIPLE, height = 10)
Lb_files.grid(row=12, column=1)



def show():
    plot_price = "null:"
    plot_totalload = "null:"
    selection = Lb_files.curselection()
    for i in selection:
        print(i)
        if(Lb_files.get(i)[0]=='t'):
            plot_totalload += Lb_files.get(i)+':'
        elif(Lb_files.get(i)[0]=='p'):
            plot_price += Lb_files.get(i)+':'


    os.system('python3 plot_result.py '+ database_path+combo_smartgrid_model.get().replace(" ", "_") + '/ '+ plot_price +' '+ plot_totalload)


btn_show = Button(window, text="Show Charts", command=show)
btn_show.grid(column=1, row=13)





window.mainloop()

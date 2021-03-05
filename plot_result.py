import tkinter as tk
from tkinter.ttk import *
from tkinter import ttk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os
import sys
import matplotlib
import numpy as np
import pandas as pd
from matplotlib import interactive
import matplotlib.ticker as plticker

 
os.chdir(sys.argv[1])
print("Plot Result")
print(sys.argv[2].split(':')) #Price
print(sys.argv[3].split(':')) #Total Load
print(len(sys.argv[2].split(':')))
print(len(sys.argv[3].split(':')))

root_name = sys.argv[1].replace("/", " ").replace("_", " ")[8:] + " Simulation Result"

root= tk.Tk() 
root.title(root_name)

lbl = Label(root, text=root_name, font=("Times", 18), foreground="#000280")
lbl.pack()

def plot_price(file_list):

    figure1 = plt.Figure(figsize=(6,5), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    legend_list = []


    figure2 = plt.Figure(figsize=(6,5), dpi=100)
    ax2 = figure2.add_subplot(111)
    bar2 = FigureCanvasTkAgg(figure2, root)
    bar2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)






    for i in range(1, len(file_list)-1):
        data_loading= pd.read_csv(str(file_list[i]), delimiter=',', skiprows=9,names=["timestamp","capacity_reference_bid_price","current_market.clearing_price","current_market.clearing_quantity"])
        data_loading.head(5)
        #print(data_loading)
        if i == 1:
            my_xticks = data_loading["timestamp"]
            with open(str(file_list[i])) as f:
                row_count = sum(1 for line in f) - 9
                y_1 = []
                for k in range(0, row_count):
                    y_1.append(my_xticks.values[k][11:19])
        ax1.plot(y_1, 'current_market.clearing_price', data=data_loading, linewidth = 4)
        ax2.plot(y_1, 'current_market.clearing_quantity', data=data_loading, linewidth = 4)
        legend_list.append(str(file_list[i]).replace('.csv',''))


        
    
    ax1.set_title('Clearing Price')
    
    plt.setp(ax1.get_xticklabels(), rotation=45, horizontalalignment='right')
    ax1.xaxis.set_major_locator(loc)
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Price $')




    ax2.set_title('Clearing Quantity')

    plt.setp(ax2.get_xticklabels(), rotation=45, horizontalalignment='right')
    ax2.xaxis.set_major_locator(loc)
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Price $')






   


def plot_total_load(file_list):

    figure2 = plt.Figure(figsize=(6,5), dpi=100)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, root)
    line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    legend_list = []

    for i in range(1, len(file_list)-1):
        data_loading= pd.read_csv(str(file_list[i]), delimiter=',', skiprows=9,names=["timestamp","power_out_real"])
        data_loading.head(5)

        if i == 1:
            my_xticks = data_loading["timestamp"]
            with open(str(file_list[i])) as f:
                row_count = sum(1 for line in f) - 9
                y_1 = []
                for k in range(0, row_count):
                    y_1.append(my_xticks.values[k][11:19])
        ax2.plot(y_1, 'power_out_real', data=data_loading, linewidth = 4)
        legend_list.append(str(file_list[i]).replace('.csv',''))
    
   
    ax2.set_title('Total Load')
    
    plt.setp(ax2.get_xticklabels(), rotation=45, horizontalalignment='right')
    ax2.xaxis.set_major_locator(loc)
    ax2.set_xlabel('Time')
    ax2.set_ylabel('kWh')


loc = plticker.MultipleLocator(base=100) # this locator puts ticks at regular intervals
if(len(sys.argv[2].split(':'))>2):
    plot_price(sys.argv[2].split(':'))
if(len(sys.argv[3].split(':'))>2):
    plot_total_load(sys.argv[3].split(':'))

root.mainloop()
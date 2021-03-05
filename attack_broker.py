import json
import shutil
import os
import sys
import fileinput
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import subprocess
import sys
from subprocess import check_output
import time


filter = "JSON file (*.json)|*.json|All Files (*.*)|*.*||"
with open('attack_library.json', 'r') as f:
    distros_dict = json.load(f)

path = "Database/"


def print_function():
    print("------------------------------------------")
    print("Welcome to Smart Grid Simulation System!")
    print("------------------------------------------")
    print("Please select Attack ID from:  ")
    for x in range(len(distros_dict['object'])):
        print("------------------------------------------")
        print('Attack ID:  ' + str(distros_dict['object'][x]["attack_id"]))
        print('Category Name:  ' + str(distros_dict['object'][x]["category_name"]))

        print('Attack Type: ' + str(distros_dict['object'][x]["name"]))

        print("------------------------------------------")
        


def readfile(index):
    for x in range(len(distros_dict['object'])):
        if distros_dict['object'][x]["attack_id"]==str(index):
            print("\n \n------------------------------------------")
            print("You selected Attack ID: " + str(distros_dict['object'][x]["attack_id"]))
            print('- Category Name:  ' + str(distros_dict['object'][x]["category_name"]))
            print('- Attack Type: ' + str(distros_dict['object'][x]["name"]))
            print('- Description:  ' + str(distros_dict['object'][x]["attack_type"][0]["description"]))
            print('- Attack Component:  ' + str(distros_dict['object'][x]["attack_component"][0]["component_name"]))
            print('- Start Time:  ' + str(distros_dict['object'][x]["attack_schedule"][0]["start_time"]))
            print('- End Time: ' + str(distros_dict['object'][x]["attack_schedule"][0]["end_time"]))
            
            filepath = str(distros_dict['object'][x]["attack_component"][0]["file"])
            file_out = str("run_" + filepath)
            affected_value = distros_dict['object'][x]["attack_type"][0]["affected_value"][0]
            print('- Affected Value: ')
            for key, value in affected_value.items():
                print('\t- ' + str(key) + " = " + str(value))
                config(filepath, file_out, key, value)


def config(filepath, file_out, key, value):
    f = open(file_out,'r')
    filedata = f.read()
    f.close()
    if filepath == "ns-3.cc":
        newdata = filedata.replace("//Flag", "//Flag"+ "\n \t" + key + " = " + str(value) + ";//")
    else:
        newdata = filedata.replace(key,key + " " + str(value) + ";//")
    f = open(file_out,'w')
    f.write(newdata)
    f.close()



#Check Process is running or not
def is_running(pid):        
    try:
        os.kill(pid, 0)
    except OSError:
        return False

    return True

def main():
    os.system('clear')
    os.chdir(sys.argv[1])
    os.remove("run_ns-3.cc")
    os.remove("run_GridLab-D.glm")
    time.sleep(1)
    shutil.copyfile("ns-3.cc", "run_ns-3.cc")
    shutil.copyfile("GridLab-D.glm", "run_GridLab-D.glm")
    print_function()

    readfile(sys.argv[2])


    p1 = subprocess.Popen('./compile-ns3.sh run_ns-3.cc', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, executable='/bin/bash')

    p1.wait()
    time.sleep(2)
    p2 = subprocess.Popen('./run.sh', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, executable='/bin/bash')
    time.sleep(2)
    child = subprocess.Popen('pgrep xterm', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, executable='/bin/bash')
    pid = int(child.communicate()[0].split('\n')[0])
    print("The Simulation is running!")
    print("Process PID: "+str(pid))
    while is_running(pid):
        time.sleep(1)
    print("Finished!")


if __name__ == '__main__':
    main()

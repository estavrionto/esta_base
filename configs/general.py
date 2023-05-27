#!/usr/bin/env python3
import os
import sys
import csv
import subprocess
import json
# import argparse
# parser = argparse.ArgumentParser(description='some useful functions')
# # adding the required arguments using argparse
# # parser.add_argument( '-i', '--input_file', help='Input file', metavar='<FASTA-file>',  required=True, type=str )
# # parser.add_argument( '-f', '--input_fold', help='Input FASTA file', metavar='<input fold>',default=70 ,type=int )
# args = parser.parse_args()
def QuestionYesNo(Question):
    answer = input(Question)
    if answer in ['y','Y','yes']:return 'y'
    elif answer in ['n', 'N', 'no']:return 'n'
    else:
        print('enter either y or n')
        return(QuestionYesNo(Question))

def LISTtoFILE(List, name):
    with open(name, 'wt') as fo:
        for i in List:
            fo.write(i)

def FILEtoLIST(FileName):
    with open(FileName) as fo:
        return list(fo)


def printLIST(LIST):
    for i in LIST:print(i)

def execute(Command):
    return subprocess.check_output(Command,shell=True,universal_newlines=True)

def SVtoLIST(_SVfile,Delimiter):
    with open(_SVfile, 'r') as fo:
            reader = csv.reader(fo, delimiter=Delimiter)
            return list(reader)

def LISTto_SV(LIST,Delimiter, _SVfile):
    with open(_SVfile, 'w') as fo:
        writer = csv.writer(fo, delimiter = Delimiter)
        writer.writerows(LIST)

def CopyFile(InFilePath, CopyPath):
    execute('cp '+InFilePath+' '+CopyPath)

def print_i3(text):
    execute("notify-send '"+text+"'")

def prtex(Command):
    print(execute(Command))

def i3_msg(text):
    execute('i3-msg '+text)

def i3_json(command):
    all_commmands = ['run_command', 'get_workspaces', 'get_outputs', 'get_tree', 'get_marks', 'get_bar_config', 'get_binding_modes', 'get_version', 'get_config']
    all_json_commmands = all_commmands
    i3_msg = 'i3-msg -t '
    if command in all_json_commmands:
        ars =  execute(i3_msg+command)
        return json.loads(ars[:-1])
    else:
        print('not valid command')
        return None

def json_dict_viewer(VAR,LIST = []):
    if type(VAR) is dict:
        for i in VAR:
            tLIST = LIST.copy()
            tLIST.append(i)
            json_dict_viewer(VAR[i],tLIST)
    elif type(VAR) is list:
        for j,i in enumerate(VAR):
            tLIST = LIST.copy()
            tLIST.append('list_'+str(j))
            # print('list')
            json_dict_viewer(i,tLIST)
    else:
        for i in LIST:
            print(i,end=' > ')
        print(VAR)

def i3_get_active_class(VAR = i3_json('get_tree')):
    if type(VAR) is dict:
        try:
            if VAR['focused'] == True:
                # print(VAR['focused'])
                return VAR['window_properties']['class']
        except:
            pass
        for i in VAR:
            # print(VAR)
            # tLIST = LIST.copy()
            # tLIST.append(i)
            r = i3_get_active_class(VAR[i])
            if r != None:
                return r
    elif type(VAR) is list:
        for i in VAR:
            # tLIST = LIST.copy()
            # tLIST.append('list_'+str(j))
            # print('list')
            r = i3_get_active_class(i)
            if r != None:
                return r
    else:
        pass



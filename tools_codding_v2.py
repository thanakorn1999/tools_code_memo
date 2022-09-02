
import pyperclip
import keyboard
import json
import pandas as pd
import re

def load_data_excel():
    data = pd.read_excel('./memo/memo.xlsx')
    data = data.dropna()
    message_json = data['message'].values.tolist()
    command_list = data['command'].values.tolist()
    new_command_list =[]
    # for mac
    for command in command_list:
        text = command
        if '!' in text:
            text = re.sub('!', '1', text)
        if '@' in text:
            text = re.sub('@', '2', text)
        if '#' in text:
            text = re.sub('#', '3', text)
        if '$' in text:
            text = re.sub('$', '4', text)
        if '%' in text:
            text = re.sub('%', '5', text)
        new_command_list.append(text)
    

    command_list=new_command_list
    print(command_list)
    return command_list,message_json


history ="01234567"

def write(replacement,command):
    global history
    history ="01234567"
    for n in range(len(command)+1):
        # for windows
        # keyboard.send('\b') 
        # for mac
        keyboard.send('delete')
        
    pyperclip.copy(replacement)
    # for windows
    # keyboard.send("command+v")
    # for mac
    keyboard.send("command+v")


def check_map_command(history):
    global command_list,message_json
    # keyboard.wait()
    for index,command in enumerate(command_list) :
        if command in history :
            print('true',command,history)
            write(message_json[index],command_list[index])

def released(release):
    if(len(release))==1:
        global history
        history=history[1:]+release
        print(history)
    # elif release=='space':
    # elif release=='command':
    elif release=='right shift':
    # elif release=='ƒ':
        check_map_command(history)
    else :
        print(release)
    

def mainv2(command_list,message_json,history):
    
    # for index,command in enumerate(command_list):
    #     # keyboard.add_abbreviation(command, message_json[index])
    # keyboard.add_abbreviation(command, lambda: keyboard.write('foobar'))
    keyboard.on_release(lambda e: released(e.name))

        # 

# [1:]
    # keyboard.add_abbreviation('@@', 'my.long.email@example.com')
    keyboard.wait()


command_list,message_json =load_data_excel()

# command_list,message_json =load_data()

mainv2(command_list,message_json,history)

import pyperclip
import keyboard
import pandas as pd
import re
from sys import platform
if platform =='win32':
    import win32api
    win32api.LoadKeyboardLayout('00000409',1) # to switch to english
    cm_copy ="ctrl+v"
    cm_del ="\b"
elif platform =='darwin':
    cm_copy ="command+v"
    cm_del ="delete"

def chang_command_mac(command_list):
    new_command_list =[]
    for command in command_list:
        text = command
        if '!' in text:
            text = re.sub('!', '1', text)
        if '@' in text:
            text = re.sub('@', '2', text)
        if '#' in text:
            text = re.sub('#', '3', text)
        # if '$' in text:
        #     text = re.sub('$', '4', text)
        if '%' in text:
            text = re.sub('%', '5', text)
        if '_' in text:
            text = re.sub('_', '-', text)
        new_command_list.append(text)

    print(new_command_list)
    return new_command_list

def load_data_excel(platform):
    data = pd.read_excel('./memo/memo.xlsx')
    data = data.dropna()
    #? need to update : sort
    message_json = data['message'].values.tolist()
    command_list = data['command'].values.tolist()

    if platform == 'darwin':
        command_list = chang_command_mac(command_list)

    return command_list, message_json

def write(replacement,command):
    global history, cm_copy, cm_del
    history ="0123456"
    #? need to update : find
    for n in range(len(command)):
        keyboard.send(cm_del)
    
    pyperclip.copy(replacement)
    keyboard.send(cm_copy)

def check_map_command(history):
    global command_list,message_json

    for index,command in enumerate(command_list) :
        if command in history :
            print('true',command,history)
            write(message_json[index],command_list[index])

def released(release, history):
    global cm_del

    if(len(release))==1:
        history=history[1:]+release
        print(history)
    elif release=='right shift':
        if history=='0123456':
            keyboard.send(cm_del)
        else :
            check_map_command(history)
    else :
        print(release)
        # keyboard.send(cm_del)

def main(history):
    keyboard.on_release(lambda e: released( e.name ,history)) # old logic keyboard.add_abbreviation('@@', 'my.long.email@example.com')
    keyboard.wait()

command_list ,message_json= load_data_excel( platform)  #load data from excel file.
history ="0123456"

main(history) 

import pyperclip
import keyboard
import json
import pandas as pd

def load_data_excel():
    data = pd.read_excel('./memo/memo.xlsx')
    data = data.dropna()
    message_json = data['message'].values.tolist()
    command_list = data['command'].values.tolist()
    return command_list,message_json


history ="012345678910"

def write(replacement,command):
    global history
    history ="012345678910"
    for n in range(len(command)+1):
        keyboard.send('\b')
    pyperclip.copy(replacement)
    keyboard.send("Ctrl+v")

    # Command
    # Ctrl


def check_map_command(history):
    global command_list,message_json
    for index,command in enumerate(command_list) :
        if command in history :
            print('true',command,history)
            write(message_json[index],command_list[index])

def released(release):
    if(len(release))==1:
        global history
        history=history[1:]+release
        print(history)
    elif release=='space':
        check_map_command(history)
    

def mainv2(command_list,message_json,history):
    
    # for index,command in enumerate(command_list):
    #     # keyboard.add_abbreviation(command, message_json[index])
    #     keyboard.add_abbreviation(command, lambda: keyboard.write('foobar'))
    keyboard.on_release(lambda e: released(e.name))

        # 

# [1:]
    # keyboard.add_abbreviation('@@', 'my.long.email@example.com')
    keyboard.wait()


command_list,message_json =load_data_excel()

# command_list,message_json =load_data()

mainv2(command_list,message_json,history)
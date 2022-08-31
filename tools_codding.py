
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

def load_data():
    # f = open('memo.json')
    f = open('./memo/memo_vue.json')
    message_json = json.load(f)
    command_list = list(message_json.keys())
    print(message_json)

    return command_list,message_json

# def main(command_list,message_json):
#     while True:

#         for command in command_list:
#             if(keyboard.is_pressed(command)):
#                 # pyperclip.copy(message_json[command])
#                 # keyboard.write(message_json[command])
#                 print(message_json[command])

def mainv2(command_list,message_json):
    
    # for command in command_list:
    #     keyboard.add_abbreviation(command, message_json[command])
    
    for index,command in enumerate(command_list):
        # keyboard.add_abbreviation(command, message_json[index])
        keyboard.add_abbreviation(command, message_json[index])

        # 


    # keyboard.add_abbreviation('@@', 'my.long.email@example.com')
    keyboard.wait()


command_list,message_json =load_data_excel()

# command_list,message_json =load_data()

mainv2(command_list,message_json)
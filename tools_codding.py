# import pygame
# # https://www.pygame.org/docs/ref/key.html
# import sys
 
# # initialising pygame
# pygame.init()
 
# # creating display
# display = pygame.display.set_mode((300, 300))
# # creating a running loop
# while True:
       
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
#             if event.mod == pygame.KMOD_NONE:
#                 print('No modifier keys were in a pressed state when this '
#                     'event occurred.')
#             else:
#                 # if event.mod & pygame.K_RCTRL and pygame.K_g:
#                 #     print('f() get')
#                 #     print(pygame.key.get_pressed()[pygame.K_RCTRL])
#                 if pygame.key.get_pressed()[pygame.K_g] and pygame.key.get_pressed()[pygame.K_RCTRL]:
#                     print(' c+ ggggg')
#                 # if event.mod & pygame.K_RCTRL:
#                 #     print('Left shift was in a pressed state when this event '
#                 #         'occurred.')
#                 if event.mod & pygame.KMOD_RSHIFT:
#                     print('Right shift was in a pressed state when this event '
#                         'occurred.')
#                 if event.mod & pygame.KMOD_SHIFT:
#                     print('Left shift or right shift or both were in a '
#                         'pressed state when this event occurred.')

import pyperclip
import keyboard

while True:
    # keyboard.add_hotkey("ctrl+alt+p", lambda: print("CTRL+ALT+P Pressed!"))
    # keyboard.add_hotkey("a", lambda: print("A Pressed!"))
    if keyboard.is_pressed('ctrl+g+space'):
        switch('ctrl+g+space')
        
def switch(type_input):
    if type_input == 'ctrl+g+space':
        print('ctrl+g+space')
        copy_get()
        return "You can become a web developer."
    elif type_input ==  'ctrl+g+space':
        return "You can become a backend developer."
  
  
def copy_get():
    pyperclip.copy('The text to be copied to the clipboard.')

def copy_post():
    pyperclip.copy('The text to be copied to the clipboard.')

def copy_row():
    pyperclip.copy('The text to be copied to the clipboard.')

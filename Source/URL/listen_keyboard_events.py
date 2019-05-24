import sys
import pyperclip
from pynput import keyboard
import time

def url_compare(url):

    #url = 'https://spot.wooribank.com/pot/Dream?withyou=bp' + '\n'
    f = open("test.txt", 'r', encoding='UTF8')
    while 1:
        k = f.readline()
        if not k: break
        if url.replace('#loading', '') + "\n" == k or url + "\n"== k:
            return "This URL is matching"
    return "There is no match"



flag_c = 0
input = []
def get_key_name(key):
    if isinstance(key, keyboard.KeyCode):
        return key.char
    else:
        return str(key)


def on_press(key):
    global flag_c
    key_name = get_key_name(key)
    #print('Key {} pressed.'.format(key_name))

    if (key_name == 'Key.enter'):
        url = ''.join(input)
        print(url)
        print(url_compare(url))
        input.clear()
        #sys.exit()
    elif (key_name == 'Key.backspace'):
        input.remove(input[-1])
    elif (key_name == 'Key.ctrl_l'):
        flag_c = 1;
    elif (key_name == 'c' and flag_c == 1):
        time.sleep(0.5)
        url = pyperclip.paste()
        print(url)
        print(url_compare(url))
        flag_c = 0
    else:
        input.append(key_name)

def on_release(key):
    key_name = get_key_name(key)
    #print('Key {} released.'.format(key_name))

    if key_name == 'Key.esc':
        print('Exiting...')
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()





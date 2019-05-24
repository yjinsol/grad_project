import pyperclip
import time
from pynput import keyboard
from selenium import webdriver
import socket
import os
import sys

def url_compare(url):

    #url = 'https://spot.wooribank.com/pot/Dream?withyou=bp' + '\n'
    f = open(r"C:\Users\yjs12\PycharmProjects\grad_project\dist\program/test.txt", 'r', encoding='UTF8')
    while 1:
        k = f.readline()
        if not k: break
        if url.replace('#loading', '') + "\n" == k or url + "\n"== k:
            return "This URL is matching...Starting image comparison"
    return "There is no match...This is a fake site."

# TCP client example
# 받은 파일 저장 경로 폴더
src = r"C:\Users\yjs12\PycharmProjects\grad_project/test/test.png"

def transfer(img_name):
    capture_file_name = r"C:\Users\yjs12\PycharmProjects\grad_project\test/" + img_name
    # 아래에는 저장 코드가 들어가야 한다.
    # save

    # 3 저장된 파일 보내기

    # img 가져오기 보낼 (파일경로/이름)
    file = open(capture_file_name, "rb")
    img_size = os.path.getsize(capture_file_name)
    img = file.read(img_size)  # 저장된 이미
    file.close()

    # 서버 연결
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("220.67.124.105", 5002))

    # url 전송
    client_socket.send(img_name.encode())
    # 이미지 전송
    client_socket.sendall(img)


    # 서버와 연결 종료
    client_socket.close()
    print("Finish SendAll")
    #sys.exit()



def capture_crawler_user_and_tranfer(url):
    print("Wait a few seconds....")
    driver_path = r'C:\Users\yjs12\Downloads\chromedriver.exe'

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1440x2192')
    options.add_argument('disable-gpu')

    driver = webdriver.Chrome(driver_path, chrome_options=options)
    #driver.get('http://192.168.182.128')
    if url[:8] != 'https://':
        url = "https://" + url
    #print(url)
    driver.get(url)
    st = ""
    st += url[8:]
    st = st.replace("/", "!")
    st = st.replace("?", "@")
    st = st.replace(":", "%")
    st = st.replace(".", "$")
    dir_path = r"C:\Users\yjs12\PycharmProjects\grad_project/test/"
    img_name = st + "_" + "test" + ".png"
    driver.save_screenshot(dir_path + img_name)
    transfer(img_name)

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
        url_result = url_compare(url)
        print("===>" + url_result + "\n")
        if(url_result == 'This URL is matching...Starting image comparison'):
            capture_crawler_user_and_tranfer(url)
            print("Press 'Esc' to exit the program.")
        input.clear()
        #sys.exit()
    elif (key_name == 'Key.backspace'):
        if len(input) > 0:
            input.remove(input[-1])
    elif (key_name == 'Key.ctrl_l'):
        flag_c = 1
    elif (key_name == 'c' and flag_c == 1):
        time.sleep(0.5)
        url = pyperclip.paste()
        print(url)
        url_result = url_compare(url)
        print("===>" + url_result)
        if (url_result == 'This URL is matching...Starting image comparison'):
            capture_crawler_user_and_tranfer(url)
            print("Press 'Esc' to exit the program.")
        flag_c = 0
    elif (key_name == 'a' and flag_c == 1):
        flag_c = 0
        pass
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





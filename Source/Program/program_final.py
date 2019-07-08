import pyperclip
import time
from pynput import keyboard
from selenium import webdriver
import socket
import os
import sys
import wx
import base64
import hashlib

# TCP client example

port = 5003
flag = 0
# 서버 연결
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("220.67.124.105", port))

def transfer(url, img_name):
    global recv
    if url:
        while True:
            if url:
                client_socket.send(url.encode())
            else:
                continue
            recv = client_socket.recv(1024).decode()
            break
        return recv

    elif img_name:
        capture_file_name = r"/home/usergpu2/PycharmProjects/untitled4/user_image/" + img_name
        #capture_file_name = r"/home/usergpu2/바탕화면/rcv_img/otalk$kbstar$com!quics@page=omember&QSL=F#loading_test.png"
        # 아래에는 저장 코드가 들어가야 한다.
        # save

        # 3 저장된 파일 보내기

        # img 가져오기 보낼 (파일경로/이름)
        file = open(capture_file_name, "rb")
        img_size = os.path.getsize(capture_file_name)
        img = file.read(img_size)  # 저장된 이미
        file.close()

        # 이미지 전송
        client_socket.sendall(img)

        # 서버와 연결 종료 (이미지 보내고 종료)
        client_socket.close()
        print("Finish Test Image SendAll\n")

        # 서버 연결
        resp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        resp_socket.connect(("220.67.124.105", port))

        recv = resp_socket.recv(1024).decode()
        print("<Image Similarity using tensorflow>")
        print(recv)

        # 서버와 연결 종료 (이미지 유사도 받은 후 종료)
        resp_socket.close()
        print("Finish Similarity ResponseAll\n")




def capture_crawler_user_and_tranfer(url):
    print("\nWait a few seconds....")
    driver_path = r'/home/usergpu2/chrome/chromedriver'

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
    dir_path = r"/home/usergpu2/PycharmProjects/untitled4/user_image/"
    img_name = st + "_" + "test" + ".png"
    driver.refresh()
    time.sleep(1)
    driver.save_screenshot(dir_path + img_name)
    transfer(None, img_name)
    global flag
    flag = 1

class Frame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500, 250))
        self.panel = wx.Panel(self)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

        # 버튼 생성
        self.btn = wx.Button(self.panel, -1, 'Compare', (200, 30))
        self.btn2 = wx.Button(self.panel, -1, 'Close', (200, 175))

        # 텍스트 박스 생성
        self.txt = wx.TextCtrl(self.panel, -1, size=(150, 20), pos=(170, 0))
        self.txt.SetValue('Input your url')

        # 텍스트 라벨 생성
        self.some_text = wx.StaticText(self.panel, size=(140, 110), pos=(10, 60))
        self.some_text.SetLabel('Waiting')

        # self.some_text2 = wx.StaticText(self.panel, size=(140, 150), pos=(10, 120))
        # self.some_text2.SetLabel('result')

        # 버튼 클릭 시 이벤트 연결
        self.Bind(wx.EVT_BUTTON, self.URL_compare, self.btn)
        self.Bind(wx.EVT_BUTTON, self.OnClose, self.btn2)
        self.Centre()
        self.Show()
        # sizer = wx.BoxSizer(wx.VERTICAL)
        # sizer.Add(self.btn)
        # sizer.Add(self.txt)
        #
        # self.panel.SetSizer(sizer)



    def URL_compare(self, e):
        url = self.txt.GetValue()
        url_result = transfer(url, None)
        self.enc = url_result + "\n"
        self.some_text.SetLabel(self.enc)
        if (url_result == 'This URL is matching...Starting image comparison'):
            capture_crawler_user_and_tranfer(url)
            self.fin = recv
            self.some_text.SetLabel(recv)

            # time.sleep(5)
            # self.OnClose(None)

    def OnClose(self, event):
        global flag
        if flag == 0:
            client_socket.send(''.encode())
        self.Close(True)

    def OnCloseWindow(self, e):
        global flag
        if flag == 0:
            client_socket.send(''.encode())
        self.Destroy()

app = wx.App()
frame = Frame(None, 'HufsDetector')
app.MainLoop()




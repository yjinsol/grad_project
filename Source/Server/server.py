# TCP server example

from socket import *
import socket
import os
import time
import sys

# 이미지 파일 저장경로
src = r"C:\Users\yjs12\PycharmProjects\grad_project/"


def fileName():
    dte = time.localtime()
    Year = dte.tm_year
    Mon = dte.tm_mon
    Day = dte.tm_mday
    WDay = dte.tm_wday
    Hour = dte.tm_hour
    Min = dte.tm_min
    Sec = dte.tm_sec
    imgFileName = src + str(Year) + '_' + str(Mon) + '_' + str(Day) + '_' + str(Hour) + '_' + str(Min) + '_' + str(
        Sec) + '.png'
    return imgFileName


# 서버 소켓 오픈
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("192.168.0.66", 5005))
server_socket.listen(5)

print("TCPServer Waiting for client on port 5000")

cnt = 0
while True:

    # 클라이언트 요청 대기중 .
    client_socket, address = server_socket.accept()
    # 연결 요청 성공
    print("I got a connection from ", address)

    data = None

    # Data 수신
    while True:
        img_data = client_socket.recv(1024)
        data = img_data
        if img_data:
            while img_data:
                print("recving Img...")
                img_data = client_socket.recv(1024)
                data += img_data
            else:
                break

    # 받은 데이터 저장
    # 이미지 파일 이름은 현재날짜/시간/분/초.jpg
    img_fileName = fileName()
    img_file = open(img_fileName, "wb")
    print("finish img recv")
    print(sys.getsizeof(data))
    img_file.write(data)
    img_file.close()
    print("Finish ")
    cnt += 1
    if(cnt == 6): break



client_socket.close()
print("SOCKET closed... END")
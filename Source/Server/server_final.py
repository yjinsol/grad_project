# TCP server example

from socket import *
import socket
from os import rename
import time
import sys
import numpy as np
import tensorflow as tf
import os
from pathlib import Path
from PIL import Image
import imagehash



port = 5003
modelFullPath = '/home/usergpu2/kbbank_label/output_graph.pb'                                      # 읽어들일 graph 파일 경로
labelsFullPath = '/home/usergpu2/kbbank_label/output_labels.txt'                                   # 읽어들일 labels 파일 경로


def create_graph():
    """저장된(saved) GraphDef 파일로부터 graph를 생성하고 saver를 반환한다."""
    # 저장된(saved) graph_def.pb로부터 graph를 생성한다.
    with tf.gfile.FastGFile(modelFullPath, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')


def run_inference_on_image():
    answer = None

    if not tf.gfile.Exists(imagePath):
        tf.logging.fatal('File does not exist %s', imagePath)
        return answer

    image_data = tf.gfile.FastGFile(imagePath, 'rb').read()

    # 저장된(saved) GraphDef 파일로부터 graph를 생성한다.
    create_graph()

    with tf.Session() as sess:
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        predictions = sess.run(softmax_tensor,
                               {'DecodeJpeg/contents:0': image_data})
        predictions = np.squeeze(predictions)

        top_k = predictions.argsort()[-5:][::-1]  # 가장 높은 확률을 가진 5개(top 5)의 예측값(predictions)을 얻는다.
        f = open(labelsFullPath, 'rb')
        lines = f.readlines()
        labels = [str(w).replace("\n", "") for w in lines]
        top5_scores = []
        for node_id in top_k:
            human_string = labels[node_id]
            score = predictions[node_id]
            top5_scores.append((human_string, score))
            print ('%s (score = %.5f)' % (human_string, score))
        return ('%s (score = %.5f)' % top5_scores[0])


        answer = labels[top_k[0]]
        return answer


#if __name__ == '__main__':
    #run_inference_on_image()

def url_compare(url):

    #url = 'https://www.kbstar.com/'
    f = open("/home/usergpu2/kbbank_label/URLlist.txt", 'r', encoding='UTF8')
    if url[-8:] == '#loading':
        url = url[:-8]
    if len(url)>=9 and url[8] == 'b':
        url = url[:8] + url[9:]

    print(url)
    while 1:
        k = f.readline()
        url.replace('#loading', '')
        if not k: break
        if url + "\n" == k or url + "&QSL=F\n" == k:
            return "This URL is matching...Starting image comparison"
    return "There is no match...This is a fake site."


# 이미지 파일 저장경로
src = r"/home/usergpu2/kbbank_recv_img"
src2 = r"/home/usergpu2/바탕화면/rcv_img"


def name_convert(url_data):
    st = ""
    st += url_data[8:]
    st = st.replace("/", "!")
    st = st.replace("?", "@")
    st = st.replace(":", "%")
    st = st.replace(".", "$")

    img_name = st + "_" + "test" + ".png"
    return img_name


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


def test_img_similarity():
    global imagePath
    imagePath = src + "/" + name_convert(url_data)
    similarity_str = run_inference_on_image()
    similarity = float(similarity_str[-8:-1])
    print("test: " + str(similarity))

    return str(similarity)


def origin_img_similarity(test_imgName):
    global imagePath
    print(test_imgName)
    test_imgName = test_imgName[:-9]
    if test_imgName[-8:] == '#loading':
        test_imgName = test_imgName[:-8]
    if test_imgName[0] == 'b':
        test_imgName = test_imgName[1:]
    print(test_imgName)
    dir = "/home/usergpu2/kbbank_capture/" + test_imgName
    #dir = "/home/usergpu2/test/" + test_imgName
    directory = Path(dir)
    if not directory.exists():
        dir = "/home/usergpu2/kbbank_capture/" + test_imgName + "&QSL=F"
        #dir = "/home/usergpu2/test/" + test_imgName + "&QSL=F"

        print(test_imgName+"&QSL=F")
    file_list = os.listdir(dir)
    similarity = []
    for file in file_list:
        if file[-4:] == '.png':
            imagePath = dir + "/" + file
            similarity_str = run_inference_on_image()
            similarity.append(float(similarity_str[-8:-1]))
    print(len(similarity))
    print("origin: " + str(max(similarity)))
    return str(max(similarity))

def ImageHash(test_imgName):
    global state
    test_img = test_imgName
    # test Hash
    test_dir = src + "/" + test_img
    test_hash = imagehash.dhash(Image.open(test_dir))
    print("test: " + str(test_hash))

    # origin Hash
    test_imgName = test_imgName[:-9]
    if test_imgName[-8:] == '#loading':
        test_imgName = test_imgName[:-8]
    if test_imgName[0] == 'b':
        test_imgName = test_imgName[1:]

    dir = "/home/usergpu2/kbbank_capture/" + test_imgName
    #dir = "/home/usergpu2/test/" + test_imgName
    directory = Path(dir)
    if not directory.exists():
        dir = "/home/usergpu2/kbbank_capture/" + test_imgName + "&QSL=F"
        #dir = "/home/usergpu2/test/" + test_imgName + "&QSL=F"

    file_list = os.listdir(dir)
    hamming_distance = []
    for file in file_list:
        if file[-4:] == '.png':
            org_dir = dir + "/" + file
            org_hash = imagehash.dhash(Image.open(org_dir))
            print(org_hash)
            hamming_distance.append(abs(org_hash-test_hash))
            if abs(org_hash - test_hash) == 0:
                print(file)
                #state = 0
                #return "ImageHash Result...Hamming distance is 0. It is original site."
                return "It is original site"
    #return "ImageHash Result... It is fake site."
    return "It is fake site...Hamming distance is " + str(min(hamming_distance))
    #state = 1
            #return str(max(similarity_hash))


# 서버 소켓 오픈
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", port))
server_socket.listen(5)

print("TCPServer Waiting for client on port " + str(port))
flag = 0

while True:

    # 클라이언트 요청 대기중 .
    client_socket, address = server_socket.accept()
    # 연결 요청 성공
    print("I got a connection from ", address)

    data = None

    # Data 수신
    while True:
        if flag == 0:
            url_data = client_socket.recv(1024).decode()
            #print(url_data)
            if url_data == '':
                client_socket.close()
                break
            url_result = url_compare(url_data)
            client_socket.send((url_result).encode())
            if url_result == "This URL is matching...Starting image comparison":
                flag = 1
            #break
        elif flag == 1:
            img_data = client_socket.recv(1024)
            data = img_data
            if img_data == '':
                client_socket.close()
                break
            if img_data:
                print("recving Img...")
                while img_data:
                    img_data = client_socket.recv(1024)
                    data += img_data
                else:
                    flag = 2
                    # 받은 데이터 저장
                    # 이미지 파일 이름은 현재날짜/시간/분/초.jpg
                    img_file = open(src + "/" + name_convert(url_data), "wb")
                    print("finish img recv")
                    print(sys.getsizeof(data))
                    img_file.write(data)
                    img_file.close()
                    print("Finish ")
                    #print(run_inference_on_image())
                    break
        elif flag == 2:
            test_compare_result = test_img_similarity()
            origin_compare_result = origin_img_similarity(name_convert(url_data))
            hash_result = ImageHash(name_convert(url_data))
            #if abs(test_compare_result - origin_compare_result) < 5:


            result = ("Test image similarity: " + test_compare_result + "\n" + "Origin image similarity: " + origin_compare_result + "\n" + "ImageHash similarity: " + hash_result).encode()
            #result = hash_result.encode()

            client_socket.send(result)
            flag = 0
            break


# client_socket.shutdown()
client_socket.close()
print("SOCKET closed... END")






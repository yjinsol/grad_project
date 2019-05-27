# TCP server example

from socket import *
import socket
from os import rename
import time
import sys
import numpy as np
import tensorflow as tf



modelFullPath = '/tmp/output_graph.pb'                                      # 읽어들일 graph 파일 경로
labelsFullPath = '/tmp/output_labels.txt'                                   # 읽어들일 labels 파일 경로


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
        for node_id in top_k:
            human_string = labels[node_id]
            score = predictions[node_id]
            return ('%s (score = %.5f)' % (human_string, score))


        answer = labels[top_k[0]]
        return answer


#if __name__ == '__main__':
    #run_inference_on_image()

def url_compare(url):

    #url = 'https://www.kbstar.com/'
    f = open("test.txt", 'r', encoding='UTF8')
    while 1:
        k = f.readline()
        if not k: break
        if url.replace('#loading', '') + "\n" == k or url + "\n" == k or url[:8]+"b"+url[8:] == k:
            return "This URL is matching...Starting image comparison"
    return "There is no match...This is a fake site."

# 이미지 파일 저장경로
src = r"/home/usergpu2/바탕화면/rcv_img"


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


#def test_img_similarity():






#def origin_img_similarity():




# 서버 소켓 오픈
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", 5001))
server_socket.listen(5)

print("TCPServer Waiting for client on port 5000")
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
            print(url_data)
            url_result = url_compare(url_data)
            client_socket.send((url_result).encode())
            if url_result == "This URL is matching...Starting image comparison":
                flag = 1
            #break
        elif flag == 1:
            img_data = client_socket.recv(1024)
            data = img_data

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
                    img_path = src + "/" + name_convert(url_data)
                    imagePath = img_path
                    print("finish img recv")
                    print(sys.getsizeof(data))
                    img_file.write(data)
                    img_file.close()
                    print("Finish ")
                    #print(run_inference_on_image())
                    break
        elif flag == 2:
            client_socket.send((run_inference_on_image()).encode())
            flag = 0


# client_socket.shutdown()
client_socket.close()
print("SOCKET closed... END")






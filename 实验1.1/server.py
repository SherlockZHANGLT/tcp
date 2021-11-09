from socket import *
import random
#服务端通过调用socket创建套接字来启动服务器
serverSocket=socket(AF_INET,SOCK_DGRAM)
#服务器调用 bind( ) 指定服务器的套接字地址
serverSocket.bind(('',8887))
while True:
    rand=random.randint(0,10)
    #服务端调用recvfrom()等待接收数据，此时阻塞
    message,address=serverSocket.recvfrom(1024)
    #成功接收消息后继续运行
    print(message)
    message=message.upper()
    #模拟丢失30%的客户端数据包
    if rand<4:
        continue
    #服务器接收到客户端发来的数据后，调用sendto()向客户发送应答数据
    serverSocket.sendto(message,address)
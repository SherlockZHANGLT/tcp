from socket import *
import sys,threading

def web_mul_server(ip, port,num):
    # 服务器端通过调用socket()创建套接字来启动一个服务器
    serverSocket = socket(AF_INET,SOCK_STREAM)
    server_address = (ip, port)#接收传入的ip地址与端口号
    #服务器调用bind()绑定指定服务器的套接字地址（IP 地址 + 端口号）
    serverSocket.bind(server_address)
 
    # 服务器调用listen()做好侦听准备，同时规定好请求队列的长度
    Length=1024
    try:
        serverSocket.listen(1)
    except socket.error:
        print("fail to listen on port %s" % error)
        sys.exit(1)

    while True:
        print("server "+str(num)+" ready to server...")
        #服务器进入阻塞状态，等待客户的连接请求
        #服务器通过accept来接收连接请求，并获得客户的 socket 地址
        connectionSocket, addr = serverSocket.accept()
        break

    while True:
        try:
            #通过TCP 套接字接收 HTTP 请求
            message = connectionSocket.recv(Length)
            msg_de = message.decode('utf-8')
            print('file msg from '+msg_de)
            #收到客户端断开连接消息
            if msg_de == 'disconnect':break
            #从服务器的文件系统读取客户端请求的文件
            client_num=message.split()[0]
            client_num=client_num.decode('utf-8')
            filename=message.split()[1]
            f=open(filename[0:])
            #被请求文件存在，创建一个由被请求的文件组成的“请求成功”HTTP 响应报文
            output=(msg_de+' from '+client_num+' has been successfully received.--server '+str(num)).encode('utf-8')
            #通过 TCP 连接将响应报文发回客户端
            connectionSocket.send(output)
        except IOError:
            #被请求文件不存在，创建“请求目标不存在”HTTP 响应报文
            output=('The request has failed.').encode('utf-8')
            #通过 TCP 连接将响应报文发回客户端
            connectionSocket.send(output)
 
    print("finish test, close connect")
    #通过close()关闭套接字
    connectionSocket.close()
    serverSocket.close()
 
 
 
if __name__=='__main__':
    t1=threading.Thread(target=web_mul_server,args=('127.0.0.1',6000,1))
    t2=threading.Thread(target=web_mul_server,args=('127.0.0.1',7000,2))
    t3=threading.Thread(target=web_mul_server,args=('127.0.0.1',8000,3))
    t1.start()
    t2.start()
    t3.start()

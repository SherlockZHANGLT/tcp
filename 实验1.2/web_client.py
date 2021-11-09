from socket import *
 
def web_client(ip,port):
    #在客户端通过调用socket()创建套接字
    clientSocket = socket(AF_INET,SOCK_STREAM)
    failed_count = 0
    while True:
        try:
            print("start connect to server ")
            #客户端调用connect()和服务器建立连接
            clientSocket.connect((ip,port))
            break
        except socket.error:
            failed_count += 1
            print("fail to connect to server %d times" % failed_count)
            if failed_count == 100: return
 
    #连接成功后发送消息
    while True:
        print("connect success")
        receive_count = 0
        while True:
            if receive_count%2==0:
                msg = 'iloveu.txt'#存在的文档消息请求
            else:
                msg='1.txt'#不存在的文档消息请求
            #使用send()发送消息
            clientSocket.send(msg.encode('utf-8'))
                        
            msg = clientSocket.recv(1024)
            print('msg from server :'+msg.decode('utf-8'))
 
            receive_count+= 1
            #一共发送14次消息，随后告知服务器将要断开连接
            if receive_count==14:
                msg = 'disconnect'
                clientSocket.send(msg.encode('utf-8'))
                break
        break
    #通过close关闭套接字
    clientSocket.close()
        
if __name__=='__main__':
    web_client('127.0.0.1',6000)
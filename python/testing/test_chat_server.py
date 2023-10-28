#!/usr/bin/python3
import socket
import mopp

class ChatClient:
    wpm = 23
    bufferSize = 1024
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    def __init__(self, wpm=23, ip="127.0.0.1", port=7373):
        self.m = mopp.mopp(wpm=wpm)
        self.serverAddressPort = (ip, port)

    def send_receive(self, msg):
        f=self.m.str2mopp(msg)
        bytesToSend = str.encode(f)
        self.UDPClientSocket.sendto(bytesToSend, self.serverAddressPort)
        msgFromServer = self.UDPClientSocket.recvfrom(self.bufferSize)
        mm = msgFromServer[0].decode("utf-8", errors='ignore')

        m1 = self.m.decodePacket(mm)
        m2 = self.m.mopp2str(mm)
        print (self.m.rx_serial, self.m.rx_wpm, m1, m2)

#c = ChatClient()
c = ChatClient(ip="49.12.102.144")
c.send_receive("hi")
c.send_receive("hello")
c.send_receive("bye")

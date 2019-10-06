from socket import *
from threading import Thread
import os

def atende (conn, cliente):
        data = conn.recv(4096)
        conn.send(str.encode("nome do arquivo recebido","UTF-8"))
        arquivo = open("1"+data.decode("UTF-8") , "w")
        while True:
                data = conn.recv(4096)
                if data.decode("UTF-8") == '':
                        arquivo.close()
                        conn.close
                        break
                arquivo.write(data.decode("UTF-8"))

s = socket ()

host = "0.0.0.0"
porta = 8753
s.bind ((host, porta))
s.listen (10)
nthr = 0

while True:
        (conn,cliente) = s.accept ()
        print ("Recebi a conexao de "+str(cliente))
        nthr += 1
        print ("Criando thread "+str(nthr))
        t = Thread(target=atende,args=(conn, cliente,))
        t.start()


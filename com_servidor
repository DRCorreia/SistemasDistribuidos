from socket import *
from threading import Thread

def atende (conn, cliente):
        conn.settimeout(10.00)
        while True:
                try:
                        data = conn.recv (4096)
                except:
                        print ("Erro na conexão com o cliente "+str(cliente))
                        break


                print (str(cliente)+" me mandou "+data.decode("utf-8") )

                try:
                        aux=int(data.decode("utf-8")) + 1
                        conn.send(str.encode(str(aux)))
                except:
                        break

        print ("Fim da conexao com "+str(cliente))
        conn.close

s = socket ()
host = "127.0.0.1"
porta = 8753
s.bind ((host, porta))
s.listen (100)
nthr = 0

while True:
        (conn, cliente) = s.accept ()

        print ("Recebi a conexao de "+str(cliente))
        nthr += 1
        print ("Criando thread "+str(nthr))
        t = Thread(target=atende,args=(conn, cliente,))
        t.start()





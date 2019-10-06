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

                if data.decode("utf-8")[0].lower() == 'v':
                        conn.send(str.encode("Outono","utf-8"))
                if data.decode("utf-8")[0].lower() == 'o':
                        conn.send(str.encode("Inverno","utf-8"))
                if data.decode("utf-8")[0].lower() == 'i':
                        conn.send(str.encode("Primavera","utf-8"))
                if data.decode("utf-8")[0].lower() == 'p':
                        conn.send(str.encode("Verao","utf-8"))



        print ("Fim da conexao com "+str(cliente))
        conn.close

s = socket ()
host = "0.0.0.0"
porta = 8754
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

from socket import  *

s = socket ()

host="127.0.0.1"
porta=8753
arquivo=input("Insira o nome do arquivo:")
ref_arquivo=open(arquivo,"r")
s.connect((host, porta))
s.send(str.encode(arquivo,"UTF-8"))
mensagem=s.recv(8192)
print(mensagem.decode("UTF-8"))
while True:
        linha = ref_arquivo.readline()
        if(linha==''):
                break
        s.send (linha.encode("UTF-8"))
ref_arquivo.close()
frase=''
s.send(frase.encode("UTF-8"))
s.close()

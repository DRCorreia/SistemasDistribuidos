from socket import  *

s = socket ()


servidor="0.0.0.0"
porta=8754
s.connect((servidor, porta))

while True:
    minhastr = input("Digite o que será enviado: ")

    if (minhastr == ""):
        break
    meusbytes=str.encode (minhastr, "UTF-8")
    s.send (meusbytes)
    data = s.recv (8192)
    print (data.decode("utf-8"))

s.close ()



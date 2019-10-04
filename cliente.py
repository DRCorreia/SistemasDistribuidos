from socket import  *

s = socket ()
status = True
while(status == True):
   print ("Insira um frase ou digite 1 para sair")
   palavra=input()
   if palavra == "1":
      status = False
   else:
    frase=str.encode (palavra, "UTF-8")
    s.connect(("3.87.204.50", 8752))
    s.send (frase)
    data = s.recv (4096)

s.close ()




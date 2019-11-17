import requests
import urllib.parse

api="http://ec2-34-224-31-3.compute-1.amazonaws.com/cliente/"
nome = input("Digite o nome do cliente: ")
url = api+nome
dados=requests.get(url).json()
print(dados)

api = "http://ec2-34-224-31-3.compute-1.amazonaws.com/pedido/"
url = api+str(dados[0]["customerid"])
print(url)
dados=requests.get(url).json()
print(dados)

total=0
for i in dados:
        total += i['Total']
print("o total de pedidos foi de :%.2f"%(total))

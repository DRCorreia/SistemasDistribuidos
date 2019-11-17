import requests
import urllib.parse

api="https://geocoder.api.here.com/6.2/geocode.json?"
endereco = input("De o endereço: ")
url = api+urllib.parse.urlencode ({"app_id":"z3jUJ93RWM6R8WvmQJBu", "app_code":"Yy6EHVWBPuj8D3inXod29w", "searchtext":endereco})
dados=requests.get(url).json()

if dados["Response"]["View"] == []:
        print("Endereço inválido!")
        exit()

local1 = dados["Response"]["View"][0]["Result"][0]["Location"]["DisplayPosition"]
print (local1)
endereco2 = input("De o endereço 2: ")
url2 = api+urllib.parse.urlencode ({"app_id":"z3jUJ93RWM6R8WvmQJBu", "app_code":"Yy6EHVWBPuj8D3inXod29w", "searchtext":endereco2})
dados2=requests.get(url2).json()
if dados2["Response"]["View"] == []:
        print("Endereço inválido!")
        exit()

local2 = dados2["Response"]["View"][0]["Result"][0]["Location"]["DisplayPosition"]
print (local2)

api_rota="https://route.api.here.com/routing/7.2/calculateroute.json?"
url_rota = api_rota+urllib.parse.urlencode ({"app_id":"z3jUJ93RWM6R8WvmQJBu", "app_code":"Yy6EHVWBPuj8D3inXod29w", "waypoint0":str(local1["Latitude"])+','+str(local1["Longitude"]),"waypoint1":str(local2["Latitude"])+','+str(local2["Longitude"]), "mode":"fastest;car;traffic:enabled", "departure":"now" })
print (url_rota)
print (url_rota)
print (url_rota)
dados_rota=requests.get(url_rota).json()
print (dados_rota)
print("******************************************************")

data =requests.get(url_rota).json()
traveltime = data["response"]["route"][0]["leg"][0]["travelTime"]
print("Tempo de chegada: %s"%(traveltime))

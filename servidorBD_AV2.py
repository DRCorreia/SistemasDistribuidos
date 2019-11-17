import mysql.connector
from flask import Flask
import json
from flask_jsonpify import jsonify

app = Flask(__name__) # __name__ variável do sistema que indica o nome do módulo ou 'main'

@app.route("/cliente/<nome>")
def imprime_cliente (nome=None):
        conn = mysql.connector.connect (host='sistemasdistribuidos.c9aa3shrbfs3.us-east-1.rds.amazonaws.com', user='admin',
passwd='mariojoao',port='3306', database='chinook')
        cursor = conn.cursor()
        id = "select customerid from customers where firstname=\'"+nome+"\'"
        print(id)
        query = cursor.execute(id)
        row_headers=[x[0] for x in cursor.description]
        print (row_headers)
        records = cursor.fetchall()
        print (records)
        result = [dict(zip(tuple (row_headers) ,i)) for i in records] #estrutura do json
        print (result)
        jret = jsonify(result)
        print (jret)
        conn.close()
        return jret

@app.route("/pedido/<id>")
def imprime_valores(id=None):
        conn = mysql.connector.connect (host='sistemasdistribuidos.c9aa3shrbfs3.us-east-1.rds.amazonaws.com', user='admin',
passwd='mariojoao',port='3306', database='chinook')
        cursor = conn.cursor() #cursor pra executar a query
        valores = "select Total from invoices where customerid=\'"+id+"\'"
        print(valores)
        query = cursor.execute(valores)
        row_headers=[x[0] for x in cursor.description]
        print (row_headers)
        records = cursor.fetchall()
        print (records)
        #doideira em decimal
        result = [dict(zip(tuple (row_headers) ,[float(i[0])])) for i in records] #estrutura do json
        print (result)
        jret = jsonify(result)
        print (jret)
        conn.close()
        return jret



app.run(host='0.0.0.0', port='80')

# Sera usado o seguinte video como referencia do projeto:
# https://www.youtube.com/watch?v=GMppyAPbLYk&list=LL&index=5&t=2362s

''' Instalando as Bibliotecas necessarias:

 instalar todas as bibllilotecas contidas no arquivo requirements.tx
  executar comando pelo terminal e dentro da pasta..
'pip install -r requirements.txt'

 '''

# Importando as bibliotecas
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {"tim" : {"age" : 19, "gender" : "male"},
         "bill" : {"age" : 70,"gender" : "male"}}

class HelloWorld(Resource):
    def get(self, name):
        return names[name]

    def post(self):
        return {"data":"Posted"}

api.add_resource(HelloWorld, "/helloworld/<string:name>")


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, Response, json, request
from dbHelp import DataHelp

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
# пользователь обращается к АПИ
# получение всех данных
# получение данных по году, году и месяцу или бизнесу
# ДЗ
# добавить данные
# изменить данные
# удалить данные
API_PREFIX='/api/v1'
@app.route(API_PREFIX, methods=['GET'])

def test():
    return 'API is working!'

@app.route(API_PREFIX+"/search", methods=['GET'])
def search():
    try:
        if len(request.args) > 0 :
            args = dict(request.args)
            if "selected_fields" in args:
                sfield = args.pop('selected_fields')
                sfield = sfield.split(',')
            result = db.search_data(selection=sfield,**args)
        else:
            result = db.read_all_data()
    except Exception as e:
        print(str(e))
        return Response("[]",status=400)  
    print(json.dumps(result))
    response = Response(json.dumps(result, ensure_ascii=False).encode('utf8'), content_type="application/json; charset=utf-8")
    return response
@app.route(API_PREFIX+"/add", methods=['POST'])
def add():
    records = request.json
    if db.checkExistFromDict(**records):
        response = {"error": "Record already exists!"}
    else:
        db.insert_into_query(**records)
        response = {"success": "Record created!"}
    return response

db = DataHelp()

app.run(debug='on')
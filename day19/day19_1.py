from pprint import pprint
from flask import Flask, json, request, Response

app=Flask("test")

@app.route("/bot", methods=['GET'])
def test():
    print(request)
    return '["Api works!"]'

@app.route("/api/v1/test", methods=['GET'])
def api_all():
    pprint(request.args)
    if 'id' in request.args:
        id = int(request.args["id"])
        p = {}
        p["id"] = id
        return json.dumps(p)
    return Response("[]",status=400)

app.run(port=5054)
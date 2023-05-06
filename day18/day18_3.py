import json
from superclassapi import GetFromApi, RequestType

baseurl = "https://datausa.io/api"
method = "data"
params = {"drilldown": "State", "measures": "Population", "year": "2018"}
g = (
    GetFromApi(baseUrl=baseurl)
    .addMethodAndParams(["data"], parameters=params)
    .AddBodyParams("login", "pedro")
    .AddBodyParams("password", "pasquale")
    .GetDataFromApi()
)


if g.error:
    print(g.errorMessage)
p = g.result.json()
if isinstance(p, dict):
    print(p)

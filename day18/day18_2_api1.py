from pprint import pprint
from superclassapi import GetFromApi, RequestType

baseUrl = "https://api.restful-api.dev"

h = GetFromApi(baseUrl)

data = {
      "year": 2019,
      "price": 699.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "color": "silver"
   }

#r = h.addMethodAndParams(['objects'], id=[3,5,10,11] ).GetDataFromApi().GetResultAsList()
#r = h.addMethodAndParams(['objects','ff80818187d7e8710187d8a11990000d'] ).GetDataFromApi(RequestType.DELETE).GetResultAsDict()
#h.addMethodAndParams(['objects'] ).AddBodyParams(key="name", value="Apple MacBook Pro 16")
#r = h.AddBodyParams("data", data).GetDataFromApi(RequestType.PUT).GetResultAsDict()
r = h.addMethodAndParams(['objects'] ).GetDataFromApi().GetResultAsList()
pprint(r)

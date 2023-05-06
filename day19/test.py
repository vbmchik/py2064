from superclassapi import GetFromApi

g = GetFromApi(baseUrl="http://localhost:5054")\
    .addMethodAndParams(["/api/v1/test"],  name='Michael')\
    .GetDataFromApi()
if g.error:
    print(g.errorMessage)
else:
    print(g.result.json())
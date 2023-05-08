from superclassapi import GetFromApi
from superclassapi import RequestType

# https://api.nationalize.io/?name[]=michael&name[]=matthew&name[]=jane
g = (
    GetFromApi(baseUrl="https://api.nationalize.io")
    .addMethodAndParams([""], name='michael')
    .GetDataFromApi(requestType=RequestType.GET)
)
if g.error:
    print(g.errorMessage)
else:
    print(g.result.json())

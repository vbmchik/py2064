
from superclassapi import GetFromApi, RequestType

g = GetFromApi(baseUrl="http:/sdfdsf")\
    .addMethodAndParams(['order'], id=[1,2,3])\
        .AddBodyParams("login", "pedro")\
            .AddBodyParams("password","pasquale")\
                .GetDataFromApi(RequestType.POST)\
                    .GetResultAsList()
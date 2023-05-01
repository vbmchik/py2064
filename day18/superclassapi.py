from enum import Enum
import json
import requests

class RequestType(Enum):
    GET = 1
    POST = 2
    PUT = 3
    PATCH = 4
    DELETE = 5

class GetFromApi():
    
    def __init__(self, baseUrl) -> None:
        self.baseUrl = baseUrl
        self.body = {}
        
    def addMethodAndParams(self, method: list(), **parameters ):
        self.URL = self.baseUrl
        if self.baseUrl[-1] != '/':
            self.URL += "/"
        for m in method:
            m.replace("/","")
        self.URL = self.URL + '/'.join(method)
        if not len(parameters):
            return self
        pslist = []
        for key in parameters:
            if isinstance(parameters[key], list):
                for p in parameters[key]:
                    pslist.append(f"{key}={p}")
            else:
                pslist.append(f"{key}={parameters[key]}")
        #paramstring = list(map(lambda x: f"{x[0]}={x[1]}",pslist))
        query = '&'.join(pslist)
        self.URL += '?'+query
        self.body = {}
        return self
    
    def AddBodyParams(self, key: str, value: str):
        self.body[key] = value
        return self
    
    def GetDataFromApi(self, requestType=RequestType.GET):
        headers = {"Accept": 'application/json'}
        if requestType == RequestType.GET:
            self.result = requests.get(self.URL, headers=headers)
        if requestType == RequestType.POST:   
            headers["Content-Type"] = 'application/json' 
            self.result = requests.post(url=self.URL, headers=headers, data=json.dumps(self.body))
        if requestType == RequestType.PUT:   
            headers["Content-Type"] = 'application/json' 
            self.result = requests.put(url=self.URL, headers=headers, data=json.dumps(self.body))
        if requestType == RequestType.PATCH:   
            headers["Content-Type"] = 'application/json' 
            self.result = requests.patch(url=self.URL, headers=headers, data=json.dumps(self.body))
        if requestType == RequestType.DELETE:
            self.result = requests.delete(self.URL, headers=headers)
        return self
    
    def GetResultAsDict(self):
        return dict(self.result.json())
    
    def GetResultAsList(self):
        return list(self.result.json())

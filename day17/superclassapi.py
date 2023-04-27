import requests

class GetFromApi():
    
    def __init__(self, baseUrl) -> None:
        self.baseUrl = baseUrl
        
    def setFullUrl(self, method: str, **parameters ):
        self.URL = self.baseUrl
        if self.baseUrl[-1] != '/':
            self.URL += "/"
        self.URL = self.URL + method
        if not len(parameters):
            return self
        paramstring = list(map(lambda x: f"{x[0]}={x[1]}",parameters.items()))
        query = '&'.join(paramstring)
        self.URL += '?'+query
        return self
        
    def GetDataFromApi(self):
        headers = {"Accept": 'application/json'}
        self.result = requests.get(self.URL, headers=headers)
        return self
    
    def GetResultAsDict(self):
        return dict(self.result.json())

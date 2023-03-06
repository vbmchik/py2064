import json

def printJson(object):
    return json.dumps(object)

def string2object(st):
    if st == None:
        return None
    return json.loads(st)


beasts = list()

beasts.append({
    "name": "One",
    "color": "White",
    "series": ["1", "2", "3"]
})

beasts.append({
    "name": "two",
    "color": "black",
    "series": [1, 3, 4]
})

try:
    with open('day3/text.json') as file_object:
        contents = file_object.read()
    contents = None
    fin = string2object(contents)
    print(contents)
except FileNotFoundError:
    print("No such file exists!")
except IOError:
    print("Cannot read / write file maybe disk is corrupted")
except Exception as e:
    print("Something wrong!", repr(e))
finally:
    print("finaly")
print("hellloooooooo!")

def fil(x):
    return x > 0


l = [1, -2, 3, -5, 4, 5, -2]


lplus = list(filter(lambda x: x > -3 and x < 4, l))
lplus1 = list(filter(fil, l))
print(lplus)


lpeople = [
    {
        "name" : "Ann",
        "age" : 28
    },
    {
        "name": "Felix",
        "age": 121
    },
    {
        "name": "Sheyla",
        "age": 32
    },
    {
        "name": "Jacob",
        "age": 6
    },
    {
        "name": "Roald",
        "age": 44
    }
]

newlist = list(filter(lambda x: x['age']<40 and len(x['name'])>3,lpeople))
print(newlist)
dd = {
    "Name": "John",
    "Secondary name": "Smith",
    "Age": 75
}

x, y = (2,3)
print(x,y)
# [(),(),(),...,() ]
for key in dd:
    print(dd[key])
    
for key, value in dd.items():
    print(f'{key}, {value}')
    
for item in dd.items():
    print(item)


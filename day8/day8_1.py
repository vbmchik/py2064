file = open('beasts.txt', "r")
result = file.read()
file.close()

print(result)

try:
    file = open('beasts.txt1', "r")
    result = file.read()
except FileNotFoundError as notfound:
    print("Your file cannot be found please correct your path")
except IOError as iooerror:
    print("Attention file cannot be readed! Please contact your administrator")
except Exception as e:
    print(e)
finally:
    file.close()
    
with open("beasts.py") as bfile:
    result = file.read()
print(result)

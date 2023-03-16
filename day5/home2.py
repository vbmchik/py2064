from home1 import stringsSort


with open('advs.txt', 'r') as shfile:
    text = shfile.read().lower()

clearer = stringsSort(text)
print(clearer)

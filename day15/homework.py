import sys
from dbHelp import DataHelp

dataHelp = DataHelp()

def inputImp(question):
    p = input(question+"\t")
    if p == '.':
        print('Operation cancelled!')
        sys.exit()
    try:
        n = int(p)
    except:
        print('Please enter integer number, nothing more!')
        return(inputImp(question))
    return n

print("Hello! This is income data processing unit!")
print('You will be asked for values to enter!')
print('for exit just enter .')

while True:
    year = inputImp('Enter year:')
    month = inputImp('Enter month:')
    business = inputImp('Enter business:')
    income = inputImp('Enter income')
    
    if dataHelp.checkExist(year,month,business):
        print('We already have a record for those business and date')
        y = input('Do you want to replace existing record? input y/n')
        if y !='y':
            print("Going to next input ") 
        else:
            dataHelp.replace_data(year, month, business, income)
            print('Record updated')
    else:
        dataHelp.insert_into_query(year=year, month=month, business=business, income=income)
        print('Record created')
    
    print(year, month, business, income)
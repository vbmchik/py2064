try:
    with open('day3/text.json') as file_object:
        for line in file_object:
            print(line)      
  
except FileNotFoundError:
    print("No such file exists!")
except IOError:
    print("Cannot read / write file maybe disk is corrupted")
except Exception as e:
    print("Something wrong!", repr(e))
finally:
    print("finaly")


try:
    with open('day3/text.json') as file_object:
        lines = file_object.readlines()

except FileNotFoundError:
    print("No such file exists!")
except IOError:
    print("Cannot read / write file maybe disk is corrupted")
except Exception as e:
    print("Something wrong!", repr(e))
finally:
    print("finaly")

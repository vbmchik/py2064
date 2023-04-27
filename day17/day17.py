import math

class Test:
    a = 1
    b = 2
    c = 3
   
    
    def testclass():
        print("from class")
    
    def __init__(self, b=3) -> None:
        self.a = 8 
        self.b = b
        self.c = -1
    
    def test(self):
        print('from object ' + str(self.b))
        
t = Test(7)
y = Test(3)
g = Test(5)

print(t.a, t.b, t.c)
print(Test.a, Test.b, Test.c)
print(math.sqrt(16))
Test.testclass()
t.test()
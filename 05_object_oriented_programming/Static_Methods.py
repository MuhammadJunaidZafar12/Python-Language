class Math:
    def __init__(self, num):
        self.num = num

    def addtonum(self,n):
        self.num = self.num + n

    @staticmethod
    def add(a1, b1):
        return a1 + b1

a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)
print(Math.add(2, 7))
print(a.add(7, 2))
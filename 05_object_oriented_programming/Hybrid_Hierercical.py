#Hybrid
class BaseClass:
    pass

class Derived1(BaseClass):
    pass

class Derived2(BaseClass):
    pass

class Derived3(Derived1, Derived2):
    pass

#Hiererchical Inheritance

class BaseClass:
    pass

class D1(BaseClass):
    pass

class D2(BaseClass):
    pass

class D3(D2):
    pass
from Parent1 import p1
from Parent2 import p2

class c(p1,p2):
    def __init__(self, name,no):
        super().__init__(name)
        super().__init__(no)
        print("c const")
    def ptr(self):
        print("Im from child ptr")
    def call_p2_show(self):
        return p2.show(self)
    
obj=c("raj",20)
obj.xyz()
obj.abc()
obj.ptr()
obj.show()
obj.call_p2_show()






















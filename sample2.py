a = 10
def demo():
    # local variable
    print(a)
demo()
class demo:
    a = 10
    def demo1(self):
        b=20
        return b
obj = demo()
print(obj.demo1())

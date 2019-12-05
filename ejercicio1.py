def greet(name):
    print("Hello", name)
greet("Fer")

def run(num):
    if num>=0 and num<10:
        for x in (0, num):
            print("running")
greet("Hansel")
greet("Grettel")
run(1)
run(2)
run(3)
run(4)
run(5)

def perceptron(a,b,c,d):
    if (a*b+c*d)>20:
        print("1")
    else:
        print(0)
perceptron(1,5,1,5)
perceptron(1,10,1,5)
perceptron(1,5,1,10)




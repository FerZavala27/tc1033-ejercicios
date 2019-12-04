def greet(name):
    print("Hello", name)
greet("Fer")

def run(num):
    if num>=0 and num<10:
        for x in (0, num):
            print("running")
greet("Hansel","Grettel")
run(1,2,3,4,5)

def perceptron(a, b, c, d):
    if (a*b+c*d)>20:
        print("1")
    else:
        print(0)
preceptron(1, 2, 3, 4)

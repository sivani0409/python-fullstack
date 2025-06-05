#all operation functions
def add( x , y):
    result = x + y
    return result 

def sub(x , y):
    return x - y

def mul(x , y):
    return x * y

def div(x , y):
    return x / y


#main code

number_1 = int(input())

while True:
    op = input()

    if op == "=":
        print("End of calculation result = ",number_1)
        break

    number_2 = int(input())
    
    if op == "+":
        number_1 = add(number_1 , number_2)
    elif op == "-":
        number_1 = sub(number_1 , number_2)
    elif op == "*":
        number_1 = mul(number_1 , number_2)
    elif op == "/":
        number_1 = div(number_1 , number_2)

    print(number_1)



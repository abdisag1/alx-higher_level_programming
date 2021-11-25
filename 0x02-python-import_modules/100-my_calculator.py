#!/usr/bin/python3
if __name__ == "__main__":  
    import sys
    from calculator_1 import add, sub, mul, div
    n= (sys.argv)
    arglen = (len(sys.argv))-1
    if arglen != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    op = sys.argv[2]
    oplist =["+","-","*","/"]
    opcheck = op in oplist

       
    a = int(sys.argv[1])
    b = int(sys.argv[3])
   # <a> <operator> <b> = <result>  a =b = oper(a,b)
    if (op == oplist[0]):
        result = add(a,b)
    elif (op == oplist[1]):
        result = sub(a, b)
    elif(op == oplist[2]):
        result = mul(a, b)
    elif(op == oplist[3]):
        result = div(a,b)
    else:
         print("Unknown operator. Available operators: +, -, * and")
    
         exit(1)
    print("{} {} {} = {}".format(a, op, b, result))

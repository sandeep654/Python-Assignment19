#Write a python program to create a function that finds a maximum of four numbers
def fournum():
    x=[10,20,22,4]
    greatestnum=x[0]
    print(x)
    for e in x:
        if e>greatestnum:
            greatestnum=e
    print("Maximum no is ",greatestnum)
    return x
fournum()
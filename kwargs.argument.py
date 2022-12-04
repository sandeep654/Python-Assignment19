#Write a python program to create a function which expects kwargs arguments.
def func(*ar,**argu):
    print(ar)
    print(argu)
    print(type(argu))
func(16,"I am learning python ","programming language",first_name="mysirg")
def metodo1(arg1, arg2, arg3):
    print("arg1: {}".format(arg1))
    print("arg2: {}".format(arg2))
    print("arg3: {}".format(arg3))

kwargs = {"arg3": 3, "arg2": "two"}
metodo1(1, **kwargs)

"""
def metodo2(arg1, arg2, arg3, **kwargs):
	print(kwargs)
	print("arg1: {}".format(arg1))
	print("arg2: {}".format(arg2))
	print("arg3: {}".format(arg3))

kwargs = {"arg3": 3, "arg2": "two", "arg1": "two"}
metodo2(**kwargs)

"""

"""
def metodo3(arg1=0, arg2=1, arg3=4, **kwargs):
	print(kwargs)
	print("arg1: {}".format(arg1))
	print("arg2: {}".format(arg2))
	print("arg3: {}".format(arg3))

metodo3(arg1=1, arg2=2, arg3=3, arg4=4)
"""
# WARNING
#!!! DO NOT USE THIS CODE WITHOUT MY PERMISSION !!!
#! If you would like to use this code, please ask me at this email: ohvanadiumjam@gmail.com

#* title of this project: Measure the Length
def useful(value): # a function
    value = len(str(value))
    result = print(value)
    return result

code = None
take_input = input("\033[95m" + "Enter. " + "\033[0m") # Enter (a) value(s) to measure.
if len(take_input) == 0:
    code = 204 # No value code
    print("\033[36m" + "No value, " + "\033[33m" + "code:" + str(code) + "\033[0m")
elif len(take_input) > 100:
    code = 414 # Too long that can't do any thing.
    print("\033[31m" + "ERR, " + "\033[33m" + " code" + str(code) + "\033[0m")
else:
    code = 200
    str(useful(take_input))
    print("\033[33m" + "code " + str(code) + "\033[0m")


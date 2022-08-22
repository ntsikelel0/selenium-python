'''for exceptions we can either
use raise Exception
or assert'''



#here we use try except and use customized error messsage
items = 0
try:
    2 / items

except:
    print("Come here if there is an error in the try block")


#here we use try except and use python error messsage
items1 = 0
try:
    2 / items1

except Exception as e:
    print(e)


#here we use try except and use python error messsage
items1 = 0
try:
    2 / items1

except Exception as e:
    print(e)

finally:
    print("This gets executed whether or not there is an error in the try block")


#here we use raise Exception
items2 = 1
if items2 != 2:
    raise Exception("items not added to cart")


#here we use assert
items3 = 1
assert (items3 == 2)
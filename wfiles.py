#remember to always clse a file after opening it this way
f = open('myfile.txt')
contents = f.readlines()
print(contents)
f.close()

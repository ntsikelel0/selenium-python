#this is just another way to open a file - this does not require the close() method

with open('myfile.txt', 'r') as f:
    c = f.readlines()
    rc = reversed(c)
    print(c)
    print(rc)
    with open('myfile.txt', 'w') as w:
        for l in rc:
            w.write(l)
s = "this is some string for n.sonjic@gmail.com "

spl = s.split(".")
strp = s.strip()

print(spl)
print(type(strp))
if type(strp) == str:
    print("Oh Yes!")
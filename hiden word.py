a = input("enter your random text: ")
b = input("Your word: ")
a = a.lower().replace(" ","")
b = b.lower().replace(" ","")
find = a.find(b)
if find >= 0:
    print("yes")
else:
    print("no")
a1 = input("first text: ")
a2 = input("Second text: ")
a1 = a1.lower().replace(" ","")
a2 = a2.lower().replace(" ","")
count = 0
if len(a1) == len(a2):
    for a in a1:
        for b in a2:
            if a == b:
                count +=1
    if len(a1) == count:
        print("anagram")
else:
    print("not anagrams")
        
    
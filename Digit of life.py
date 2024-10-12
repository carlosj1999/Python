a = input("Enter your DOB(YYYYMMDD): ")
a = str(a)
sum1 = 0
sum2 = 0
for i in a:
    sum1 += int(i)
for last in str(sum1):
    sum2 += int(last)
print(sum2)
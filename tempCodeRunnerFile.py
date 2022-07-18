num=input()
num=num.split(" ")
num1=list(map(int,num))

num1.sort()

if (num[0]+num[1])<num[2]:
    print("-1")
else:
    if num[0]==num[1] and num[0]==num[2]:
        print("1")
    elif num[0]==num[1] or num[1]==num[2] or num[0]==num[2]:
        print("2")
    else:
        print("3")
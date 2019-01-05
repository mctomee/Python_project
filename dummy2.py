#Lista elemek konkatenálása
words = ["Hello", "world", "!"]
x=input("Hanyszor irja ki?")
i=1
while i<=int(x):
    print("\n"+str(i)+"."+words[0]+" "+words[1]+"  "+words[2]*3)
    i=i+1
print("Competed!")
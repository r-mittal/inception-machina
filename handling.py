
try:
    i = 0/0
    print(i)

    f = open("abc.txt")

    #for x in f:
     #   print(x)
except ZeroDivisionError:
    print("divided by zer0")
except Exception:

    print("file not found")
    
#handlingreertingesfd

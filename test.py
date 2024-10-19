num = int (input ('how many item did you buy ?'))
if 0 < num < 10:
    print ("you can not have discount")
elif 10 <= num < 20 :
    print("you can have 19%  discount")
elif 20 <= num < 30:
    print("you can have 30%  discount")
else :
    print("you can have 70%  discount")

import random 
import json
name = input("enter your name = ")
print("WELCOME TO MY CAB APP",name)
rider = ["raju","monu","sonu","mohit","rohit"]

def booking():
    limit = int(input("enter how much ride you want :-"))
    index = 1
    total = 0
    dict = {}
    while index <= limit:
        distance = int(input("enter how much far you will go distance in km = "))
        place = input("enter any place name = ")
        driver = random.choice(rider)
        print(driver,"this driver is available")
        if driver in rider:
            print("which driver you choice",driver,"he is on that destination",place)
            money = distance*5
            total += money
            print(index,"ride money = ",money)
        else:
            print("driver is not available")
        print(limit,"ride your total amount = ",total)
        dict[driver] = money
        index += 1
    print(dict,"this is all ride data")
    max = 0
    for key in dict:
        if dict[key] > max:
            max = dict[key]
    with open("rider.json","w") as f:
        json.dump(dict,f,indent=4)
    print(key,"this driver is earn more money",max)
def cancel():
    print("thanks for visit my Rider sharing app  and you cancel the cab safely.")
def main():
    options = int(input("for booking click option  :1  and for canceling click option 2 :"))
    if options == 1:
        booking()
        print("thanks to visit my cab app","\U0001F929")
    else:
        cancel()
main()
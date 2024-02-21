year=int(input("Enter year to check whether its leap or not"))
if year%4==0:
    if year %100==0:
        if year % 400==0:
            print("leap year")
        else:
            print("not a leap year")
    else:
        print("leap year")
else:
    print("not a leap year")
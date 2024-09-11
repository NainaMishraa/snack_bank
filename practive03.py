while True:
    num = int(input("Enter a positive number: "))
    """if num>0:
        print("Thankyou!") 
        break
    else:
        print("Please enter a positive number")
        continue"""
    
    if num>0:
        print("Thankyou!")
        break 
    elif num<0 or num==0:
        print("Please enter a positive number")
        
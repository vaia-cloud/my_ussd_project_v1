ussd = input("Enter USSD  Code: ")
if ussd == "111":
    trans = input(
        "1. Data \n"
        "2. Airtime \n"
        "3. Borrow \n"
        "4. Transfer \n"
        "Select Transaction:"
    )
    if trans == "1":
        pass
    elif trans == "2":
        pass
    elif trans == "3":
        pass
    elif trans == "4":
        transfer = input(
            "1. transfer airtime \n"
            "2. transfer data \n"
        )
        if transfer == "1":
            tel = input("Enter phone number: ")
            if len(tel) == 11 and tel.isnumeric() and (tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[0:3] == "091"):
                amt = input(f"Enter amount to credit {tel}: ")
                if float(amt) >= 50 and float(amt) <= 10000 and amt.isnumeric():
                    print(f"{tel} has been credited with {amt} successfully")
                else:
                    print(f"Invalid {amt} entered")
            else:
                print(f"{tel} is invalid")

        elif transfer == "2":
            pass
        else:
            print("Invalid Transfer Option")
    else:
        print("Invalid Transaction Selection")
else:
    print("Invalid USSD Code")


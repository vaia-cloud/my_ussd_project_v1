
def transferAirtime():
    tel = input("Enter Telephone Number: ")
    if len(tel) == 11:
        pass
    elif tel == "#":
        transfer()
    elif tel == "00":
        mainmenu()
    else:
        print(
            "Invalid Phone Number \n"
            "Try Again \n"
        )
        transferAirtime()
def transfer():
    entry = input(
        "1. Transfer Data \n"
        "2. Transfer Airtime \n"
        "#. Previous \n"
        "0. Exit \n"
        "00. Main Menu \n"
    )
    if entry == '1':
        pass
    elif entry == '2':
        pass
    elif entry == '#':
        mainmenu()
    elif entry == '0':
        print("Exiting...")
    elif entry == '00':
        mainmenu()
    else:
        print("Invalid Option")
        transfer()
def mainmenu():
    trans = input(
        '1. Data \n'
        '2. Airtime \n'
        '3. Transfer \n'
        '4. Borrow \n'
        '0. Exit \n'
    )
    if trans == '1':
        pass
    elif trans == '2':
        pass
    elif trans == '3':
        transfer()
    elif trans == '4':
        pass
    elif trans == '0':
        print("Exiting....")
    else:
        print("Invalid Option")
        mainmenu()

ussd = input("Enter USSD Code: ")
if ussd == '111':
    mainmenu()
else:
    print("Invalid USSD Code")
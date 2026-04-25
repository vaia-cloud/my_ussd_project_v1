def dailyPlan9():
    daily50 = input(
        "You will be charged N50 for the purchase of 20MB+3Mins+1 Tune Jolly Combo. \n"
        "Select: \n"
        "1. Proceed (Auto-renew) \n"
        "2. Proceed (One-off) \n"
        "3. Buy for Others \n"
        "0. Back \n"
    )

def dailyPlan8():
    daily25 = input(
        "You will pay N25 for 20MB WhatsApp Daily Plan. To proceed, \n"
        "Select: \n"
        "1. Auto-Renew \n"
        "2. One-Off \n"
        "0. Back \n"
    )
    if daily25 == "1":
        print(
            "Activation of 20MB Daily plan at N25 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details"
        )
    elif daily25 == "2":
        print(
            "Activation of 20MB Daily plan at N25 was successful and auto renewal is turned off."
        )
    elif daily25 == "0":
        daybundle()
    else:
        print(
            "Invalid Selection \n"
            "Try Again \n"
        )
        dailyPlan8()
def dailyPlan7():
    daily6 = input(
        "Get 3.5GB Daily Plan for N1000. To proceed, \n"
        "Select: \n"
        "1. Auto-Renew \n"
        "2. One-Off \n"
        "3. Buy for a Friend \n"
        "4. Redeem Promo Code \n"
        "0. Back\n"
    )
    if daily6 == "1":
        print(
            "Activation of 3.5GB Daily plan at N1000 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details"
        )
    elif daily6 == "2":
        print(
            "Activation of 3.5GB Daily plan at N1000 was successful and auto renewal is turned off."
        )
    elif daily6 == "3":
        tel = input("Enter recipient's number:")
        if len(tel) == 11 and tel.isnumeric() and (
                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
            0:3] == "091"):
            print("3.5GB Gift Data was complete")
        else:
            print(f"{tel} is not a valid number.")
    elif daily6 == "4":
        code = input("Enter your coupon code:")
        if code == "12345678":
            print("Dear customer, Coupon information not available")
        else:
            print("Coupon Information not available")
    elif daily6 == "0":
        daybundle()
def dailyPlan6():
    daily5 = input(
        "Get 2.5GB Daily Plan for N750. To proceed, \n"
        "Select: \n"
        "1. Auto-Renew \n"
        "2. One-Off \n"
        "3. Buy for a Friend \n"
        "4. Redeem Promo Code \n"
        "0. Back\n"
    )
    if daily5 == "1":
        print(
            "Activation of 2.5GB Daily plan at N750 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details"
        )
    elif daily5 == "2":
        print(
            "Activation of 2.5GB Daily plan at N750 was successful and auto renewal is turned off."
        )
    elif daily5 == "3":
        tel = input("Enter recipient's number:")
        if len(tel) == 11 and tel.isnumeric() and (
                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
            0:3] == "091"):
            print("2.5GB Gift Data was complete")
        else:
            print(f"{tel} is not a valid number.")
    elif daily5 == "4":
        code = input("Enter your coupon code:")
        if code == "12345678":
            print("Dear customer, Coupon information not available")
        else:
            print("Coupon Information not available")
    elif daily5 == "0":
        daybundle()
def dailyPlan5():
    daily4 = input(
        "Get 1GB Daily Plan for N500. To proceed, \n"
        "Select: \n"
        "1. Auto-Renew \n"
        "2. One-Off \n"
        "3. Buy for a Friend \n"
        "4. Redeem Promo Code \n"
        "0. Back\n"
    )
    if daily4 == "1":
        print(
            "Activation of 1GB Daily plan at N500 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details"
        )
    elif daily4 == "2":
        print(
            "Activation of 1GB Daily plan at N500 was successful and auto renewal is turned off."
        )
    elif daily4 == "3":
        tel = input("Enter recipient's number:")
        if len(tel) == 11 and tel.isnumeric() and (
                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
            0:3] == "091"):
            print("1GB Gift Data was complete")
        else:
            print(f"{tel} is not a valid number.")
    elif daily4 == "4":
        code = input("Enter your coupon code:")
        if code == "12345678":
            print("Dear customer, Coupon information not available")
        else:
            print("Coupon Information not available")
    elif daily4 == "0":
        daybundle()
def dailyPlan4():
    daily3 = input(
        "Get 500MB Daily Plan for N350. To proceed, \n"
        "Select: \n"
        "1. Auto-Renew \n"
        "2. One-Off \n"
        "3. Buy for a Friend \n"
        "4. Redeem Promo Code \n"
        "0. Back\n"
    )
    if daily3 == "1":
        print(
            "Activation of 500MB Daily plan at N350 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details"
        )
    elif daily3 == "2":
        print(
            "Activation of 500MB Daily plan at N350 was successful and auto renewal is turned off."
        )
    elif daily3 == "3":
        tel = input("Enter recipient's number:")
        if len(tel) == 11 and tel.isnumeric() and (
                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
            0:3] == "091"):
            print("500MB Gift Data was complete")
        else:
            print(f"{tel} is not a valid number.")
    elif daily3 == "4":
        code = input("Enter your coupon code:")
        if code == "12345678":
            print("Dear customer, Coupon information not available")
        else:
            print("Coupon Information not available")
    elif daily3 == "0":
        daybundle()
def dailyPlan3():
    daily200 = input(
        "Get 230MB Daily Plan for N200. To proceed, \n"
        "Select: \n"
        "1. Auto-Renew \n"
        "2. One-Off \n"
        "3. Buy for a Friend \n"
        "4. Redeem Promo Code \n"
        "0. Back\n"
    )
    if daily200 == "1":
        print(
            "Activation of 230MB Daily plan at N200 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details"
        )
    elif daily200 == "2":
        print(
            "Activation of 230MB Daily plan at N200 was successful and auto renewal is turned off."
        )
    elif daily200 == "3":
        tel = input("Enter recipient's number:")
        if len(tel) == 11 and tel.isnumeric() and (
                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
            0:3] == "091"):
            print("230MB Gift Data was complete")
        else:
            print(f"{tel} is not a valid number.")
    elif daily200 == "4":
        code = input("Enter your coupon code:")
        if code == "12345678":
            print("Dear customer, Coupon information not available")
        else:
            print("Coupon Information not available")
    elif daily200 == "0":
        daybundle()
def dailyPlan2():
    daily100 = input(
        "Get 110MB Daily Plan for N100. To proceed, \n"
        "Select: \n"
        "1. Auto-Renew \n"
        "2. One-Off \n"
        "3. Buy for a Friend \n"
        "4. Redeem Promo Code \n"
        "0. Back\n"
    )
    if daily100 == "1":
        print(
            "Activation of 110MB Daily plan at N100 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details"
        )
    elif daily100 == "2":
        print(
            "Activation of 110MB Daily plan at N100 was successful and auto renewal is turned off."
        )
    elif daily100 == "3":
        tel = input("Enter recipient's number:")
        if len(tel) == 11 and tel.isnumeric() and (
                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
            0:3] == "091"):
            print("110MB Gift Data was complete")
        else:
            print(f"{tel} is not a valid number.")
    elif daily100 == "4":
        code = input("Enter your coupon code:")
        if code == "12345678":
            print("Dear customer, Coupon information not available")
        else:
            print("Coupon Information not available")
    elif daily100 == "0":
        daybundle()
def dailyPlan1():
    daily75 = input(
        "You will pay N75 for 75MB Daily Plan. To proceed, select: \n"
        "1. Auto-Renew \n"
        "2. One-Off \n"
        "3. Buy for a Friend \n"
        "4. Redeem Promo Code \n"
        "0. Back\n"
    )
    if daily75 == "1":
        print(
            "Activation of 75MB Daily plan at N75 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details"
        )
    elif daily75 == "2":
        print(
            "Activation of 75MB Daily plan at N75 was successful and auto renewal is turned off."
        )
    elif daily75 == "3":
        tel = input("Enter recipient's number:")
        if len(tel) == 11 and tel.isnumeric() and (
                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
            0:3] == "091"):
            print("110MB Gift Data was complete")
        else:
            print(f"{tel} is not a valid number.")
    elif daily75 == "4":
        code = input("Enter your coupon code:")
        if code == "12345678":
            print("Dear customer, Coupon information not available")
        else:
            print("Coupon Information not available")
    elif daily75 == "0":
        daybundle()
    else:
        print(
            "Invalid Selection \n"
            "Please Try again \n"
        )
        dailyPlan1()
def nextDataPlan():
    nextplan = input(
        "8. Video Packs \n"
        "9. Chat with Zigi \n"
        "10.VAS \n"
        "0. Back \n"
    )
    if nextplan == "8":
        pass
    elif nextplan == "9":
        pass
    elif nextplan == "10":
        pass
    elif nextplan == "0":
        dataPlan()
    else:
        print(
            "Invalid Selection \n"
            "Please Input again \n"
        )
        nextDataPlan()
def daybundle():
    daily = input(
        "1. N75 = 75MB \n"
        "2. N100 = 110MB \n"
        "3. N200 = 230MB \n"
        "4. N350 = 500MB\n"
        "5. N500 = 1GB \n"
        "6. N750 = 2.5GB \n"
        "7. N1000 = 3.5GB \n"
        "8. N25 = 20MB WhatsApp \n"
        "9. N50 Jolly Combo Offer \n"
        "0. Back \n"
        "00.Mainmenu \n"
    )
    if daily == "1":
        dailyPlan1()
    elif daily == "2":
        dailyPlan2()
    elif daily == "3":
        pass
    elif daily == "4":
        pass
    elif daily == "5":
        pass
    elif daily == "6":
        pass
    elif daily == "7":
        pass
    elif daily == "8":
        pass
    elif daily == "9":
        pass
    elif daily == "0":
        dataPlan()
    elif daily == "00":
        menu()
def dataplan2():
    bundles= input(
        "Buy Data Plans \n"
        "1. Daily \n"
        "2. 2-3 Days \n"
        "3. Weekly \n"
        "4. Monthly \n"
        "5. 2months + \n"
        "6. Social Bundles \n"
        "7. Broadband \n"
        "8. Binge bundles \n"
        "9. Family Share \n"
        "10.Hot Deals \n"
        "99.Next \n"
        "0. Back \n"
    )
    if bundles == "1":
        daybundle()
    elif bundles == "2":
        pass
    elif bundles == "3":
        pass
    elif bundles == "4":
        pass
    elif bundles == "5":
        pass
    elif bundles == "6":
        pass
    elif bundles == "7":
        pass
    elif bundles == "8":
        pass
    elif bundles == "9":
        pass
    elif bundles == "10":
        pass
    elif bundles == "99":
        pass
    elif bundles == "0":
        dataPlan()
def hot():
    newxtravalue= input(
        "New Xtravalue Plans \n"
        "1. N500 - 600MB+2mins+2SMS. Valid 7 days\n "
        "2. N1500 - 1.8GB+6mins+5SMS. Valid 30days \n"
        "3. N3,000 - 5.5GB+8mins+7SMS. Valid 30 Days \n"
        "0. Back \n"
    )
    if newxtravalue == "1":
        pass
    elif newxtravalue == "2":
        pass
    elif newxtravalue == "3":
        pass
    elif newxtravalue == "4":
        pass
    else:
        print(
            "Invalid Selection \n"
            "Please try again \n"
        )
        hot()
def dataPlan():
    data = input(
        "1. Data Plans \n"
        "2. Enjoy 4.5GB for N1000 \n"
        "3. Enjoy 20GB for N4,500 \n"
        "4. Voice Offers \n"
        "5. XtraValue \n"
        "6. Roaming/ Int'l \n"
        "7. Gift Data \n"
        "99.Next \n"
    )
    if data == "1":
        dataplan2()
    elif data == "2":
        pass
    elif data == "3":
        pass
    elif data == "4":
        pass
    elif data == "5":
        pass
    elif data == "6":
        pass
    elif data == "7":
        pass
    elif data == "99":
        nextDataPlan()
    else:
        print(
            "Invalid Option \n"
            "Please try again"
        )
        dataPlan()
def menu():
    mainmenu = input(
        "Our Codes have changed. For \n"
        "1. Data Plan 312 \n"
        "2. Recharge 311 \n"
        "3. Borrow Airtime 303 \n"
        "4. Data Balance 323 \n"
        "5. Account Balance 310 \n"
        "6. MTN Share 321 \n"
        "7. VAS 305 \n"
        "8. NIN 996 \n"
    )
    if mainmenu == "1":
        dataPlan()
    elif mainmenu == "2":
        pass
    elif mainmenu == "3":
        pass
    elif mainmenu == "4":
        pass
    elif mainmenu == "5":
        pass
    elif mainmenu == "6":
        pass
    elif mainmenu == "7":
        pass
    elif mainmenu == "8":
        pass
    else:
        print(
            "Invalid Option \n"
            "Please Try Again"
        )
        menu()
ussd = input("Enter USSD code here: ")
if ussd == '*301#':
    menu()
else:
    print("Invalid USSD code")
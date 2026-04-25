ussd= input("Enter ussd code:")
if ussd == "*301#":
    sel= input("Our codes have changed. For: \n"
          "1. Data Plans 312 \n"
          "2. Recharge 311 \n"
          "3. Borrow airtime 303 \n"
          "4. Data balance 323 \n"
          "5. Account Balance 310\n"
          "6. MTN Share 321 \n"
          "7. VAS 305 \n"
          "8. NIN 996 \n Input Your Selection:"
    )
    if sel == "1":
        data= input("1. Data Plans \n"
                    "2. Enjoy 4.5GB for N1000 \n"
                    "3. Enjoy 20GB for N4500 \n"
                    "4. Voice offers \n"
                    "5. XtraValue \n"
                    "6. Roaming/Int'l \n"
                    "7. Gift Data \n"
                    "99.Next\n"
                    "Select your transaction:"
        )
        if data == "1":
            plans= input("Buy Data Plans \n"
                         "1. Daily \n"
                         "2. 2-3 Days \n"
                         "3. weekly \n"
                         "4. Monthly \n"
                         "5. 2 Months+ \n"
                         "6. Social Bundles \n"
                         "7. Broadband \n"
                         "8. Binge Bundle \n"
                         "9. Family Share \n"
                         "10.Hot Deals \n"
                         "99.Next \n"
                         "Select your Plan:")
            if plans == "1":
                daily= input("1. N75 = 75MB \n"
                             "2. N100 = 110MB \n"
                             "3. N200 = 230MB \n"
                             "4. N350 = 500MB\n"
                             "5. N500 = 1GB \n"
                             "6. N750 = 2.5GB \n"
                             "7. N1000 = 3.5GB \n"
                             "8. N25 = 20MB WhatsApp \n"
                             "9. N50 Jolly Combo Offer \n"
                             "Select your daily plan:")
                if daily == "1":
                    actv = input("You will pay N75 for 75MB Daily Plan. to proceed, select:\n"
                                "1. Auto-Renew \n"
                                "2. One-Off \n"
                                "3. Buy for a Friend \n"
                                "4. Redeem Promo Code \n"
                                "Select:")
                    if actv == "1":
                        print("Activation of 75MB Daily plan at N75 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv == "2":
                        paym= input("kindly Select payment type \n"
                                    "1. Airtime \n"
                                    "2. MoMo PSB Wallet \n"
                                    "Select:")
                        if paym == "1":
                            paym2 = input("Activation of 75MB Daily failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                         "99. Next \n"
                                         "Select:")
                            if paym2 == "99":
                                pass
                            else:
                                print(f"Invalid Selection {paym2}")
                        elif paym == "2":
                            momo= input("Dear Olabisi Victoria, you are buying MTN 75MB Daily Plan data bundle for N75 valid till 01/04/2026 for 2349164900946 \n"
                                        "Please enter your MoMo Pin to confirm:")
                            if momo == "00000000":
                                pass
                            else:
                                print("Invalid pin")
                    elif actv == "3":
                        tel = input("Enter recipient's number:")
                        if len(tel) == 11 and tel.isnumeric() and (
                                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
                            0:3] == "091"):
                            pass
                        else:
                            print(f"{tel} is not a valid number.")
                    elif actv == "4":
                        code= input("Enter your coupon code:")
                        if code == "12345678":
                            pass
                        else:
                            print("Dear customer, Coupon information not available")
                    else:
                        print(f"Invalid Selection {actv}")
                elif daily == "2":
                    actv2= input("Get 110MB Daily for N100. To proceed, Select:\n"
                                 "1. Auto-Renew \n"
                                "2. One-Off \n"
                                "3. Buy for a Friend \n"
                                "4. Redeem Promo Code \n"
                                "Select:")
                    if actv2 == "1":
                        print(
                            "Activation of 110MB Daily plan at N100 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv2 == "2":
                        payt = input("kindly Select payment type \n"
                                     "1. Airtime \n"
                                     "2. MoMo PSB Wallet \n"
                                     "Select:")
                        if payt == "1":
                            redr= input("Activation of 110MB Daily failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                         "99. Next \n"
                                         "Select:")
                            if redr == "99":
                                pass
                            else:
                                print(f"Invalid Selection {redr}")
                        elif payt == "2":
                            momo2 = input(
                                "Dear Vaia Joseph, you are buying MTN 110MB Daily Plan data bundle for N100 valid till 01/04/2026 for 2349164900946 \n"
                                "Please enter your MoMo Pin to confirm:")
                            if momo2 == "00000000":
                                pass
                            else:
                                print("Invalid pin")
                        else:
                            print(f"Invalid Selection {payt}")
                    elif actv2 == "3":
                        tel = input("Enter recipient's number:")
                        if len(tel) == 11 and tel.isnumeric() and (
                                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
                            0:3] == "091"):
                            pass
                        else:
                            print(f"{tel} is not a valid number.")
                    elif actv2 == "4":
                        code2 = input("Enter your coupon code:")
                        if code2 == "12345678":
                            pass
                    else:
                        print(f"Invalid Selection {actv2}")
                elif daily == "3":
                    actv3= input("Get 230MB Daily for N200. To proceed, Select:\n"
                                 "1. Auto-Renew \n"
                                "2. One-Off \n"
                                "3. Buy for a Friend \n"
                                "4. Redeem Promo Code \n"
                                "Select:")
                    if actv3 == "1":
                        print(
                            "Activation of 230MB Daily plan at N200 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv3 == "2":
                        payt2= input("kindly Select payment type \n"
                                     "1. Airtime \n"
                                     "2. MoMo PSB Wallet \n"
                                     "Select:"
                                     )
                        if payt2 == "1":
                            redr2= input("Activation of 230MB Daily failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                         "99. Next \n"
                                         "Select:")
                            if redr2 == "99":
                                pass
                            else:
                                print(f"Invalid Selection {redr2}")
                        elif payt2 == "2":
                            momo2 = input(
                                "Dear Vaia Joseph, you are buying MTN 230MB Daily Plan data bundle for N200 valid till 01/04/2026 for 2349164900946 \n"
                                "Please enter your MoMo Pin to confirm:")
                            if momo2 == "00000000":
                                pass
                            else:
                                print("Invalid pin")
                        else:
                            print(f"Invalid Selectiom {payt2}")
                    elif actv3 == "3":
                        tel = input("Enter recipient's number:")
                        if len(tel) == 11 and tel.isnumeric() and (
                                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
                            0:3] == "091"):
                            tel2= input("Confirm recipient's number:")
                            if len(tel2) == 11 and tel2.isnumeric() and (
                                    tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                0:3] == "090" or tel2[
                                        0:3] == "091"):
                                pass
                            else:
                                print(f"{tel2} is not a valid number")
                        else:
                            print(f"{tel} is not a valid number.")
                    elif actv3 == "4":
                        code2 = input("Enter your coupon code:")
                        if code2 == "12345678":
                            pass
                    else:
                        print(f"Invalid selection {actv3}")
                elif daily == "4":
                    actv4= input("Get 500MB Daily for N350. To proceed, Select:\n"
                                 "1. Auto-Renew \n"
                                "2. One-Off \n"
                                "3. Buy for a Friend \n"
                                "4. Redeem Promo Code \n"
                                "Select:"
                                 )
                    if actv4 == "1":
                        print(
                            "Activation of 500MB Daily plan at N350 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv4 =="2":
                        payt3 = input("kindly Select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                        if payt3 == "1":
                            redr3 = input(
                                "Activation of 500MB Daily failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                "99. Next \n"
                                "Select:")
                            if redr3 == "99":
                                pass
                            else:
                                print(f"Invalid Selection {redr3}")
                        elif payt3 == "2":
                            momo3 = input(
                                "Dear Vaia Joseph, you are buying MTN 230MB Daily Plan data bundle for N200 valid till 01/04/2026 for 2349164900946 \n"
                                "Please enter your MoMo Pin to confirm:")
                            if momo3 == "00000000":
                                pass
                            else:
                                print("Invalid pin")
                        else:
                            print(f"Invalid Selection {payt3}")
                    elif actv4 =="3":
                        tel = input("Enter recipient's number:")
                        if len(tel) == 11 and tel.isnumeric() and (
                                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
                            0:3] == "091"):
                            tel2 = input("Confirm recipient's number:")
                            if len(tel2) == 11 and tel2.isnumeric() and (
                                    tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                0:3] == "090" or tel2[
                                        0:3] == "091"):
                                pass
                            else:
                                print(f"{tel2} is not a valid number")
                    elif actv4 =="4":
                        code2 = input("Enter your coupon code:")
                        if code2 == "12345678":
                            pass
                    else:
                        print(f"Invalid Selection {actv4}")
                elif daily == "5":
                    actv5= input("Get 2.5GB Daily for N750. To proceed, Select:\n"
                                 "1. Auto-Renew \n"
                                "2. One-Off \n"
                                "3. Buy for a Friend \n"
                                "4. Redeem Promo Code \n"
                                "Select:")
                    if actv5 == "1":
                        print(
                            "Activation of 2.5GB Daily plan at N750 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv5 == "2":
                        payta = input("kindly Select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                        if payta == "1":
                            redra = input(
                                "Activation of 2.5GB Daily failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                "99. Next \n"
                                "Select:")
                            if redra == "99":
                                pass
                            else:
                                print(f"Invalid Selection {redra}")
                    elif actv5 == "3":
                        tel = input("Enter recipient's number:")
                        if len(tel) == 11 and tel.isnumeric() and (
                                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
                            0:3] == "091"):
                            tel2 = input("Confirm recipient's number:")
                            if len(tel2) == 11 and tel2.isnumeric() and (
                                    tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                0:3] == "090" or tel2[
                                        0:3] == "091"):
                                pass
                            else:
                                print(f"{tel2} is not a valid number")
                    elif actv5 == "4":
                        code2 = input("Enter your coupon code:")
                        if code2 == "12345678":
                            pass
                    else:
                        print(f"Invalid Selection {actv5}")
                elif daily == "6":
                    actv6= input("Get 3.5GB Daily for N1000. To proceed, Select:\n"
                                 "1. Auto-Renew \n"
                                "2. One-Off \n"
                                "3. Buy for a Friend \n"
                                "4. Redeem Promo Code \n"
                                "Select:")
                    if actv6 == "1":
                        print(
                            "Activation of 3.5GB Daily plan at N1000 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv6 == "2":
                        payta = input("kindly Select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                        if payta == "1":
                            redra = input(
                                "Activation of 3.5GB Daily failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                "99. Next \n"
                                "Select:")
                            if redra == "99":
                                pass
                            else:
                                print(f"Invalid Selection {redra}")
                    elif actv6 == "3":
                        tel = input("Enter recipient's number:")
                        if len(tel) == 11 and tel.isnumeric() and (
                                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
                            0:3] == "091"):
                            tel2 = input("Confirm recipient's number:")
                            if len(tel2) == 11 and tel2.isnumeric() and (
                                    tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                0:3] == "090" or tel2[
                                        0:3] == "091"):
                                pass
                            else:
                                print(f"{tel2} is not a valid number")
                    elif actv6 == "4":
                        code2 = input("Enter your coupon code:")
                        if code2 == "12345678":
                            pass
                    else:
                        print(f"Invalid Selection {actv6}")
                elif daily == "7":
                    actv7= input("You will pay N25 for 20MB WhatsApp Daily Plan. To proceed, Select:\n"
                                "1. Auto-Renew \n"
                                "2. One-Off \n"
                                "Select:"
                    )
                    if actv7 == "1":
                        print(
                            "Activation of 20MB Daily plan at N25 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv7 == "2":
                        payta = input("kindly Select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                        if payta == "1":
                            redra = input(
                                "Activation of 20MB Daily failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                "99. Next \n"
                                "Select:")
                            if redra == "99":
                                pass
                            else:
                                print(f"Invalid Selection {redra}")
                    else:
                        print(f"Invalid Selection {actv7}")
                elif daily == "8":
                    actv8= input("You will be charged N50 for the purchase of 20MB+3Mins+1 Tune Jolly Combo \n"
                                 "select"
                                 "1. Proceed(Auto-Renew) \n"
                                "2. Proceed(One-Off) \n"
                                "3. Buy for others \n"
                                 )
                    if actv8 == "1":
                        print(
                            "Activation of 3.5GB Daily plan at N1000 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv8 == "2":
                        payta = input("kindly Select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                        if payta == "1":
                            redra = input(
                                "Activation of 20MB Daily failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                "99. Next \n"
                                "Select:")
                            if redra == "99":
                                pass
                            else:
                                print(f"Invalid Selection {redra}")
                    elif actv8 == "3":
                        tel = input("Enter recipient's number:")
                        if len(tel) == 11 and tel.isnumeric() and (
                                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
                            0:3] == "091"):
                            tel2 = input("Confirm recipient's number:")
                            if len(tel2) == 11 and tel2.isnumeric() and (
                                    tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                0:3] == "090" or tel2[
                                        0:3] == "091"):
                                pass
                            else:
                                print(f"{tel2} is not a valid number")
                    else:
                        print(f"Invalid Selection {actv8}")
                else:
                    print(f"Invalid Selection {daily}")
            elif plans == "2":
                tdays= input("1. N600 = 1.5GB \n"
                             "2. 750 = 2GB \n"
                             "3. N900 = 2.5GB \n"
                             "4. N1000 = 3.2GB \n"
                             "5. N1200 = 4GB \n"
                             "6. N1500 = 5.5GB \n"
                             "7. N1800 = 7GB \n"
                             "8. N100 Jolly Combo Offer"
                )
                if tdays == "1":
                    actv8 = input("Get 1.5GB+100MB YT Music for N600. to proceed, select:\n"
                                 "1. Auto-Renew \n"
                                 "2. One-Off \n"
                                 "3. Buy for a Friend \n"
                                 "4. Redeem Promo Code \n"
                                 "Select:")
                    if actv8 == "1":
                        print(
                            "Activation of 1.5GB at N600 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv8 == "2":
                        paym = input("kindly Select payment type \n"
                                     "1. Airtime \n"
                                     "2. MoMo PSB Wallet \n"
                                     "Select:")
                        if paym == "1":
                            paym2 = input(
                                "Activation of 1.5GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                "99. Next \n"
                                "Select:")
                            if paym2 == "99":
                                pass
                            else:
                                print(f"Invalid Selection {paym2}")
                        elif paym == "2":
                            momo = input(
                                "Dear Olabisi Victoria, you are buying MTN 1.5GB data bundle for N600 valid till 01/04/2026 for 2349164900946 \n"
                                "Please enter your MoMo Pin to confirm:")
                            if momo == "00000000":
                                pass
                            else:
                                print("Invalid pin")
                    elif actv8 == "3":
                        tel = input("Enter recipient's number:")
                        if len(tel) == 11 and tel.isnumeric() and (
                                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
                            0:3] == "091"):
                            pass
                        else:
                            print(f"{tel} is not a valid number.")
                    elif actv8 == "4":
                        code = input("Enter your coupon code:")
                        if code == "12345678":
                            pass
                        else:
                            print("Dear customer, Coupon information not available")
                    else:
                        print(f"Invalid Selection {actv8}")
                elif tdays == "2":
                    actv2 = input("You will pay N750 for 2.5GB 2-Day Plan. To proceed, Select:\n"
                                  "1. Auto-Renew \n"
                                  "2. One-Off \n"
                                  "3. Buy for a Friend \n"
                                  "4. Redeem Promo Code \n"
                                  "Select:")
                    if actv2 == "1":
                        print(
                            "Activation of 2.5GB 2-Day plan at N750 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv2 == "2":
                        payt = input("kindly Select payment type \n"
                                     "1. Airtime \n"
                                     "2. MoMo PSB Wallet \n"
                                     "Select:")
                        if payt == "1":
                            redr = input(
                                "Activation of 2.5GB Daily failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                "99. Next \n"
                                "Select:")
                            if redr == "99":
                                pass
                            else:
                                print(f"Invalid Selection {redr}")
                        elif payt == "2":
                            momo2 = input(
                                "Dear Vaia Joseph, you are buying MTN 2.5GB 2-Day Plan data bundle for N750 valid till 01/04/2026 for 2349164900946 \n"
                                "Please enter your MoMo Pin to confirm:")
                            if momo2 == "00000000":
                                pass
                            else:
                                print("Invalid pin")
                        else:
                            print(f"Invalid Selection {payt}")
                    elif actv2 == "3":
                        tel = input("Enter recipient's number:")
                        if len(tel) == 11 and tel.isnumeric() and (
                                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
                            0:3] == "091"):
                            pass
                        else:
                            print(f"{tel} is not a valid number.")
                    elif actv2 == "4":
                        code2 = input("Enter your coupon code:")
                        if code2 == "12345678":
                            pass
                    else:
                        print(f"Invalid Selection {actv2}")
                elif tdays == "3":
                    actv3 = input("You will pay N900 for 2.5GB 2-Day Plan. To proceed, Select:\n"
                                  "1. Auto-Renew \n"
                                  "2. One-Off \n"
                                  "3. Buy for a Friend \n"
                                  "4. Redeem Promo Code \n"
                                  "Select:")
                    if actv3 == "1":
                        print(
                            "Activation of 2.5GB Daily plan at N900 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv3 == "2":
                        payt2 = input("kindly Select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                        if payt2 == "1":
                            redr2 = input(
                                "Activation of 2.5GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                "99. Next \n"
                                "Select:")
                            if redr2 == "99":
                                pass
                            else:
                                print(f"Invalid Selection {redr2}")
                        elif payt2 == "2":
                            momo2 = input(
                                "Dear Vaia Joseph, you are buying MTN 2.5GB 2-Day Plan data bundle for N200 valid till 01/04/2026 for 2349164900946 \n"
                                "Please enter your MoMo Pin to confirm:")
                            if momo2 == "00000000":
                                pass
                            else:
                                print("Invalid pin")
                        else:
                            print(f"Invalid Selection {payt2}")
                    elif actv3 == "3":
                        tel = input("Enter recipient's number:")
                        if len(tel) == 11 and tel.isnumeric() and (
                                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
                            0:3] == "091"):
                            tel2 = input("Confirm recipient's number:")
                            if len(tel2) == 11 and tel2.isnumeric() and (
                                    tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                0:3] == "090" or tel2[
                                        0:3] == "091"):
                                pass
                            else:
                                print(f"{tel2} is not a valid number")
                        else:
                            print(f"{tel} is not a valid number.")
                    elif actv3 == "4":
                        code2 = input("Enter your coupon code:")
                        if code2 == "12345678":
                            pass
                    else:
                        print(f"Invalid selection {actv3}")
                elif tdays == "4":
                    actv4 = input("You will pay N1000 for 3.2GB 2-Day Plan. To proceed, Select:\n"
                                  "1. Auto-Renew \n"
                                  "2. One-Off \n"
                                  "3. Buy for a Friend \n"
                                  "Select:"
                                  )
                    if actv4 == "1":
                        print(
                            "Activation of 3.2GB 2-Day plan at N1000 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv4 == "2":
                        payt3 = input("kindly Select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                        if payt3 == "1":
                            redr3 = input(
                                "Activation of 3.2GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                "99. Next \n"
                                "Select:")
                            if redr3 == "99":
                                pass
                            else:
                                print(f"Invalid Selection {redr3}")
                        elif payt3 == "2":
                            momo3 = input(
                                "Dear Vaia Joseph, you are buying MTN 3.2GB 2-Day Plan data bundle for N1000 valid till 01/04/2026 for 2349164900946 \n"
                                "Please enter your MoMo Pin to confirm:")
                            if momo3 == "00000000":
                                pass
                            else:
                                print("Invalid pin")
                        else:
                            print(f"Invalid Selection {payt3}")
                    elif actv4 == "3":
                        tel = input("Enter recipient's number:")
                        if len(tel) == 11 and tel.isnumeric() and (
                                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
                            0:3] == "091"):
                            tel2 = input("Confirm recipient's number:")
                            if len(tel2) == 11 and tel2.isnumeric() and (
                                    tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                0:3] == "090" or tel2[
                                        0:3] == "091"):
                                pass
                            else:
                                print(f"{tel2} is not a valid number")
                    else:
                        print(f"Invalid Selection {actv4}")
                elif tdays == "5":
                    actv5 = input("Get 4GB 2-Day for N1200. To proceed, Select:\n"
                                  "1. Auto-Renew \n"
                                  "2. One-Off \n"
                                  "3. Buy for a Friend \n"
                                  "Select:"
                    )
                    if actv5 == "1":
                        print(
                            "Activation of 4GB 2-Day plan at N1200 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv5 == "2":
                        payta = input("kindly Select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                        if payta == "1":
                            redra = input(
                                "Activation of 4GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                "99. Next \n"
                                "Select:")
                            if redra == "99":
                                pass
                            else:
                                print(f"Invalid Selection {redra}")
                        elif payta == "2":
                            momo3 = input(
                                "Dear Vaia Joseph, you are buying MTN 4GB 2-Day Plan data bundle for N1200 valid till 01/04/2026 for 2349164900946 \n"
                                "Please enter your MoMo Pin to confirm:")
                            if momo3 == "00000000":
                                pass
                            else:
                                print("Invalid pin")
                    elif actv5 == "3":
                        tel = input("Enter recipient's number:")
                        if len(tel) == 11 and tel.isnumeric() and (
                                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
                            0:3] == "091"):
                            tel2 = input("Confirm recipient's number:")
                            if len(tel2) == 11 and tel2.isnumeric() and (
                                    tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                0:3] == "090" or tel2[
                                        0:3] == "091"):
                                pass
                            else:
                                print(f"{tel2} is not a valid number")
                    else:
                        print(f"Invalid Selection {actv5}")
                elif tdays == "6":
                    actv6 = input("Get 5.5GB 2-Days Plan for N1500. To proceed, Select:\n"
                                  "1. Auto-Renew \n"
                                  "2. One-Off \n"
                                  "3. Buy for a Friend \n"
                                  "Select:")
                    if actv6 == "1":
                        print(
                            "Activation of 5.5GB 2-Day plan at N1500 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv6 == "2":
                        payta = input("kindly Select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                        if payta == "1":
                            redra = input(
                                "Activation of 5.5GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                "99. Next \n"
                                "Select:")
                            if redra == "99":
                                pass
                            else:
                                print(f"Invalid Selection {redra}")
                        elif payta == "2":
                            momo3 = input(
                                "Dear Vaia Joseph, you are buying MTN 5.5GB 2-Day Plan data bundle for N1500 valid till 01/04/2026 for 2349164900946 \n"
                                "Please enter your MoMo Pin to confirm:")
                            if momo3 == "00000000":
                                pass
                            else:
                                print("Invalid pin")
                    elif actv6 == "3":
                        tel = input("Enter recipient's number:")
                        if len(tel) == 11 and tel.isnumeric() and (
                                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
                            0:3] == "091"):
                            tel2 = input("Confirm recipient's number:")
                            if len(tel2) == 11 and tel2.isnumeric() and (
                                    tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                0:3] == "090" or tel2[
                                        0:3] == "091"):
                                pass
                            else:
                                print(f"{tel2} is not a valid number")
                    else:
                        print(f"Invalid Selection {actv6}")
                elif tdays == "7":
                    actv7 = input("Get 7GB 2-Days Plan for 1800. To proceed, Select:\n"
                                  "1. Auto-Renew \n"
                                  "2. One-Off \n"
                                  "Select:"
                                  )
                    if actv7 == "1":
                        print(
                            "Activation of 7GB 2-Day plan at N1800 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv7 == "2":
                        payta = input("kindly Select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                        if payta == "1":
                            redra = input(
                                "Activation of 7GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                "99. Next \n"
                                "Select:")
                            if redra == "99":
                                pass
                            else:
                                print(f"Invalid Selection {redra}")
                    else:
                        print(f"Invalid Selection {actv7}")
                elif tdays == "8":
                    actv8 = input("You will be charged N100 for the purchase of 50MB+7Mins+1 Tune Jolly Combo \n"
                                  "select"
                                  "1. Proceed(Auto-Renew) \n"
                                  "2. Proceed(One-Off) \n"
                                  "3. Buy for others \n"
                                  )
                    if actv8 == "1":
                        print(
                            "Y'ello! You are not eligible for this offer. Thank you!")
                    elif actv8 == "2":
                        print(
                            "Y'ello! You are not eligible for this offer. Thank you!")
                    elif actv8 == "3":
                        print(
                            "Y'ello! You are not eligible for this offer. Thank you!")
                    else:
                        print(f"Invalid Selection {actv8}")
                else:
                    print(f"Invalid Selection {tdays}")
            elif plans == "3":
                weekly= input("1. N500 = 500MB \n"
                              "2. N500 = 600MB+2+mins \n"
                              "3. N800 = 1GB \n"
                              "4. N1000 = 1.5GB \n"
                              "5. N1500 = 3.5GB \n"
                              "6. N2500 = 6GB \n"
                              "7. N5000 = 20GB \n"
                              "8. N3500 = 11GB \n"
                              "99. Next"
                              )
                if weekly == "1":
                    actv8 = input("Get 500MB+1GB YT Night+100MB YT Music for N500. to proceed, select:\n"
                                 "1. Auto-Renew \n"
                                 "2. One-Off \n"
                                 "3. Buy for a Friend \n"
                                 "4. Redeem Promo Code \n"
                                 "Select:")
                    if actv8 == "1":
                        print(
                            "Activation of 500MB+1GB at N500 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv8 == "2":
                        paym = input("kindly Select payment type \n"
                                     "1. Airtime \n"
                                     "2. MoMo PSB Wallet \n"
                                     "Select:")
                        if paym == "1":
                            paym2 = input(
                                "Activation of 500MB+1GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                "99. Next \n"
                                "Select:")
                            if paym2 == "99":
                                pass
                            else:
                                print(f"Invalid Selection {paym2}")
                        elif paym == "2":
                            momo = input(
                                "Dear Olabisi Victoria, you are buying MTN 500MB+1GB data bundle for N500 valid till 01/04/2026 for 2349164900946 \n"
                                "Please enter your MoMo Pin to confirm:")
                            if momo == "00000000":
                                pass
                            else:
                                print("Invalid pin")
                    elif actv8 == "3":
                        tel = input("Enter recipient's number:")
                        if len(tel) == 11 and tel.isnumeric() and (
                                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
                            0:3] == "091"):
                            pass
                        else:
                            print(f"{tel} is not a valid number.")
                    elif actv8 == "4":
                        code = input("Enter your coupon code:")
                        if code == "12345678":
                            pass
                        else:
                            print("Dear customer, Coupon information not available")
                    else:
                        print(f"Invalid Selection {actv8}")
                elif weekly == "2":
                    actv2 = input("Buy XtraData500 @N500 & get 600MB+2mins+2SMS, valid for 7 days. You will be moved to XtraValue Plan . To proceed, Select:\n"
                                  "1. Auto-Renew \n"
                                  "2. One-Off \n"
                                  "Select:")
                    if actv2 == "1":
                        print(
                            "Activation of XtraData 500 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv2 == "2":
                        print("Y'ello! Activation of XtraData 500 failed due to insufficient balance. Dial *904# to recharge from your bank account")
                    else:
                        print(f"Invalid Selection {actv2}")
                elif weekly == "3":
                    actv3 = input("Get 1GB+1GB YT Night+100MB YT Music for N800. To proceed, Select:\n"
                                  "1. Auto-Renew \n"
                                  "2. One-Off \n"
                                  "3. Buy for a Friend \n"
                                  "4. Redeem Promo Code \n"
                                  "Select:")
                    if actv3 == "1":
                        print(
                            "Activation of 1GB weekly plan at N800 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv3 == "2":
                        payt2 = input("kindly Select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                        if payt2 == "1":
                            redr2 = input(
                                "Activation of 1GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                "99. Next \n"
                                "Select:")
                            if redr2 == "99":
                                pass
                            else:
                                print(f"Invalid Selection {redr2}")
                        elif payt2 == "2":
                            momo2 = input(
                                "Dear Vaia Joseph, you are buying MTN 1GB Weekly Plan data bundle for N800 valid till 01/04/2026 for 2349164900946 \n"
                                "Please enter your MoMo Pin to confirm:")
                            if momo2 == "00000000":
                                pass
                            else:
                                print("Invalid pin")
                        else:
                            print(f"Invalid Selection {payt2}")
                    elif actv3 == "3":
                        tel = input("Enter recipient's number:")
                        if len(tel) == 11 and tel.isnumeric() and (
                                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
                            0:3] == "091"):
                            tel2 = input("Confirm recipient's number:")
                            if len(tel2) == 11 and tel2.isnumeric() and (
                                    tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                0:3] == "090" or tel2[
                                        0:3] == "091"):
                                pass
                            else:
                                print(f"{tel2} is not a valid number")
                        else:
                            print(f"{tel} is not a valid number.")
                    elif actv3 == "4":
                        code2 = input("Enter your coupon code:")
                        if code2 == "12345678":
                            pass
                    else:
                        print(f"Invalid selection {actv3}")
                elif weekly == "4":
                    actv4 = input("Get 1.5GB+1GB YT Night+100MB YT Music for N1000. To proceed, Select:\n"
                                  "1. Auto-Renew \n"
                                  "2. One-Off \n"
                                  "3. Buy for a Friend \n"
                                  "Select:"
                                  )
                    if actv4 == "1":
                        print(
                            "Activation of 2.5GB weekly  plan at N1000 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv4 == "2":
                        payt3 = input("kindly Select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                        if payt3 == "1":
                            redr3 = input(
                                "Activation of 2.5GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                "99. Next \n"
                                "Select:")
                            if redr3 == "99":
                                pass
                            else:
                                print(f"Invalid Selection {redr3}")
                        elif payt3 == "2":
                            momo3 = input(
                                "Dear Vaia Joseph, you are buying MTN 2.5GB weekly Plan data bundle for N1000 valid till 01/04/2026 for 2349164900946 \n"
                                "Please enter your MoMo Pin to confirm:")
                            if momo3 == "00000000":
                                pass
                            else:
                                print("Invalid pin")
                        else:
                            print(f"Invalid Selection {payt3}")
                    elif actv4 == "3":
                        tel = input("Enter recipient's number:")
                        if len(tel) == 11 and tel.isnumeric() and (
                                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
                            0:3] == "091"):
                            tel2 = input("Confirm recipient's number:")
                            if len(tel2) == 11 and tel2.isnumeric() and (
                                    tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                0:3] == "090" or tel2[
                                        0:3] == "091"):
                                pass
                            else:
                                print(f"{tel2} is not a valid number")
                    else:
                        print(f"Invalid Selection {actv4}")
                elif weekly == "5":
                    actv5 = input("Get 3.5GB weekly Plan for N1500. To proceed, Select:\n"
                                  "1. Auto-Renew \n"
                                  "2. One-Off \n"
                                  "3. Buy for a Friend \n"
                                  "Select:"
                    )
                    if actv5 == "1":
                        print(
                            "Activation of 3.5 weekly plan at N1500 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv5 == "2":
                        payta = input("kindly Select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                        if payta == "1":
                            redra = input(
                                "Activation of 3.5GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                "99. Next \n"
                                "Select:")
                            if redra == "99":
                                pass
                            else:
                                print(f"Invalid Selection {redra}")
                        elif payta == "2":
                            momo3 = input(
                                "Dear Vaia Joseph, you are buying MTN 3.5GB weekly Plan data bundle for N1200 valid till 01/04/2026 for 2349164900946 \n"
                                "Please enter your MoMo Pin to confirm:")
                            if momo3 == "00000000":
                                pass
                            else:
                                print("Invalid pin")
                    elif actv5 == "3":
                        tel = input("Enter recipient's number:")
                        if len(tel) == 11 and tel.isnumeric() and (
                                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
                            0:3] == "091"):
                            tel2 = input("Confirm recipient's number:")
                            if len(tel2) == 11 and tel2.isnumeric() and (
                                    tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                0:3] == "090" or tel2[
                                        0:3] == "091"):
                                pass
                            else:
                                print(f"{tel2} is not a valid number")
                    else:
                        print(f"Invalid Selection {actv5}")
                elif weekly == "6":
                    actv6 = input("Get 5GB weekly Plan for N2500. To proceed, Select:\n"
                                  "1. Auto-Renew \n"
                                  "2. One-Off \n"
                                  "3. Buy for a Friend \n"
                                  "Select:")
                    if actv6 == "1":
                        print(
                            "Activation of 6GB weekly plan at N2500 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv6 == "2":
                        payta = input("kindly Select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                        if payta == "1":
                            redra = input(
                                "Activation of 6GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                "99. Next \n"
                                "Select:")
                            if redra == "99":
                                pass
                            else:
                                print(f"Invalid Selection {redra}")
                        elif payta == "2":
                            momo3 = input(
                                "Dear Vaia Joseph, you are buying MTN 6GB weekly Plan data bundle for N1500 valid till 01/04/2026 for 2349164900946 \n"
                                "Please enter your MoMo Pin to confirm:")
                            if momo3 == "00000000":
                                pass
                            else:
                                print("Invalid pin")
                    elif actv6 == "3":
                        tel = input("Enter recipient's number:")
                        if len(tel) == 11 and tel.isnumeric() and (
                                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
                            0:3] == "091"):
                            tel2 = input("Confirm recipient's number:")
                            if len(tel2) == 11 and tel2.isnumeric() and (
                                    tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                0:3] == "090" or tel2[
                                        0:3] == "091"):
                                pass
                            else:
                                print(f"{tel2} is not a valid number")
                    else:
                        print(f"Invalid Selection {actv6}")
                elif weekly == "7":
                    actv7 = input("Get 20GB weekly Plan for 5000. To proceed, Select:\n"
                                  "1. Auto-Renew \n"
                                  "2. One-Off \n"
                                  "3. Buy for a friend \n"
                                  "Select:"
                                  )
                    if actv7 == "1":
                        print(
                            "Activation of 20GB weekly plan at N5000 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv7 == "2":
                        payta = input("kindly Select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                        if payta == "1":
                            redra = input(
                                "Activation of 20GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                "99. Next \n"
                                "Select:")
                            if redra == "99":
                                pass
                            else:
                                print(f"Invalid Selection {redra}")
                    elif actv7 == "3":
                        momo3 = input(
                            "Dear Vaia Joseph, you are buying MTN 20GB weekly Plan data bundle for N5000 valid till 01/04/2026 for 2349164900946 \n"
                            "Please enter your MoMo Pin to confirm:")
                        if momo3 == "00000000":
                            pass
                        else:
                            print("Invalid pin")
                    elif actv7 == "3":
                        tel = input("Enter recipient's number:")
                        if len(tel) == 11 and tel.isnumeric() and (
                                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
                            0:3] == "091"):
                            tel2 = input("Confirm recipient's number:")
                            if len(tel2) == 11 and tel2.isnumeric() and (
                                    tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                0:3] == "090" or tel2[
                                        0:3] == "091"):
                                pass
                            else:
                                print(f"{tel2} is not a valid number")
                    else:
                        print(f"Invalid Selection {actv7}")
                elif weekly == "8":
                    actv8 = input("Get 20GB weekly Plan for 5000. To proceed, Select:\n"
                                  "1. Auto-Renew \n"
                                  "2. One-Off \n"
                                  "3. Buy for a friend \n"
                                  "Select:"
                                  )
                    if actv8 == "1":
                        print(
                            "Activation of 11GB weekly plan at N3500 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv8 == "2":
                        payta = input("kindly Select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                        if payta == "1":
                            redra = input(
                                "Activation of 11GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                "99. Next \n"
                                "Select:")
                            if redra == "99":
                                pass
                            else:
                                print(f"Invalid Selection {redra}")
                    elif actv8 == "3":
                        momo3 = input(
                            "Dear Vaia Joseph, you are buying MTN11GB weekly Plan data bundle for N3500 valid till 01/04/2026 for 2349164900946 \n"
                            "Please enter your MoMo Pin to confirm:")
                        if momo3 == "00000000":
                            pass
                        else:
                            print("Invalid pin")
                    elif actv8 == "3":
                        tel = input("Enter recipient's number:")
                        if len(tel) == 11 and tel.isnumeric() and (
                                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
                            0:3] == "091"):
                            tel2 = input("Confirm recipient's number:")
                            if len(tel2) == 11 and tel2.isnumeric() and (
                                    tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                0:3] == "090" or tel2[
                                        0:3] == "091"):
                                pass
                            else:
                                print(f"{tel2} is not a valid number")
                    else:
                        print(f"Invalid Selection {actv8}")
                else:
                    print(f"Invalid Selection {weekly}")
            elif plans == "4":
                mthly= input("1. N1500 = 1.8GB+6mins \n"
                             "2. N2000 = 2.7GB+2GB \n"
                             "3. N2500 = 3.5GB+2GB \n"
                             "4. N3000 = 6.75GB \n"
                             "5. N3500 = 7GB+2GB \n"
                             "6. N4,500 = 10GB+2GB \n"
                             "7. N5,000 = 14.5GB \n"
                             "99. Next"
                             )
                if mthly == "1":
                    actv9 = input("Buy XtraData 1500 @N1,500 & get 1.8GB+6mins, valid for 30 days. To proceed, select:\n"
                                 "1. Auto-Renew \n"
                                 "2. One-Off \n"
                                 "Select:")
                    if actv9 == "1":
                        print(
                            "Activation of XtraData1500 at N1,500 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv9 == "2":
                        paym = input("kindly Select payment type \n"
                                     "1. Airtime \n"
                                     "2. MoMo PSB Wallet \n"
                                     "Select:")
                        if paym == "1":
                            paym2 = input(
                                "Activation of XtraData1500 failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                "99. Next \n"
                                "Select:")
                            if paym2 == "99":
                                pass
                            else:
                                print(f"Invalid Selection {paym2}")
                        elif paym == "2":
                            momo = input(
                                "Dear Olabisi Victoria, you are buying MTN XtraData for N1500 valid till 01/04/2026 for 2349164900946 \n"
                                "Please enter your MoMo Pin to confirm:")
                            if momo == "00000000":
                                pass
                            else:
                                print("Invalid pin")
                elif mthly == "2":
                    actv10 = input("Get 2.7GB+2mins+2GB All Night+200MB YT Music for N2000. To proceed, Select:\n"
                                  "1. Auto-Renew \n"
                                  "2. One-Off \n"
                                  "3. Buy for a Friend \n"
                                  "4. Redeem Promo Code \n"
                                  "Select:")
                    if actv10 == "1":
                        print(
                            "Activation of 4.7GB monthly plan at N2000 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv10 == "2":
                        payt2 = input("kindly Select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                        if payt2 == "1":
                            redr2 = input(
                                "Activation of 4.7GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                "99. Next \n"
                                "Select:")
                            if redr2 == "99":
                                pass
                            else:
                                print(f"Invalid Selection {redr2}")
                        elif payt2 == "2":
                            momo2 = input(
                                "Dear Vaia Joseph, you are buying MTN 4.7GB monthly Plan data bundle for N2000 valid till 01/04/2026 for 2349164900946 \n"
                                "Please enter your MoMo Pin to confirm:")
                            if momo2 == "00000000":
                                pass
                            else:
                                print("Invalid pin")
                        else:
                            print(f"Invalid Selection {payt2}")
                    elif actv10 == "3":
                        tel = input("Enter recipient's number:")
                        if len(tel) == 11 and tel.isnumeric() and (
                                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
                            0:3] == "091"):
                            tel2 = input("Confirm recipient's number:")
                            if len(tel2) == 11 and tel2.isnumeric() and (
                                    tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                0:3] == "090" or tel2[
                                        0:3] == "091"):
                                pass
                            else:
                                print(f"{tel2} is not a valid number")
                        else:
                            print(f"{tel} is not a valid number.")
                    elif actv10 == "4":
                        code2 = input("Enter your coupon code:")
                        if code2 == "12345678":
                            pass
                        else:
                            print("Unable to fetch coupon details")
                    else:
                        print(f"Invalid selection {actv10}")
                elif mthly == "3":
                    actv11 = input("Get 3.5GB+5mins+2GB All Night+200MB YT Music for N2,500. To proceed, Select:\n"
                                  "1. Auto-Renew \n"
                                  "2. One-Off \n"
                                  "3. Buy for a Friend \n"
                                  "4. Redeem Promo Code \n"
                                  "Select:")
                    if actv11 == "1":
                        print(
                            "Activation of 5.5GB monthly plan at N2,500 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv11 == "2":
                        payt2 = input("kindly Select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                        if payt2 == "1":
                            redr2 = input(
                                "Activation of 5.5GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                "99. Next \n"
                                "Select:")
                            if redr2 == "99":
                                pass
                            else:
                                print(f"Invalid Selection {redr2}")
                        elif payt2 == "2":
                            momo2 = input(
                                "Dear Vaia Joseph, you are buying MTN 5.5GB monthly Plan data bundle for N2,500 valid till 01/04/2026 for 2349164900946 \n"
                                "Please enter your MoMo Pin to confirm:")
                            if momo2 == "00000000":
                                pass
                            else:
                                print("Invalid pin")
                        else:
                            print(f"Invalid Selection {payt2}")
                    elif actv11 == "3":
                        tel = input("Enter recipient's number:")
                        if len(tel) == 11 and tel.isnumeric() and (
                                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
                            0:3] == "091"):
                            tel2 = input("Confirm recipient's number:")
                            if len(tel2) == 11 and tel2.isnumeric() and (
                                    tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                0:3] == "090" or tel2[
                                        0:3] == "091"):
                                pass
                            else:
                                print(f"{tel2} is not a valid number")
                        else:
                            print(f"{tel} is not a valid number.")
                    elif actv11 == "4":
                        code2 = input("Enter your coupon code:")
                        if code2 == "12345678":
                            pass
                        else:
                            print("unable to fetch coupon details")
                    else:
                        print(f"Invalid selection {actv11}")
                elif mthly == "4":
                    actv12 = input("You will pay N3,000 for 6.75GB Value Data Plan. To proceed, Select:\n"
                                  "1. Auto-Renew \n"
                                  "2. One-Off \n"
                                  "3. Redeem Promo code \n"
                                  "Select:"
                                  )
                    if actv12 == "1":
                        print(
                            "Activation of 6.75GB monthly plan at N3000 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv12 == "2":
                        payt3 = input("kindly Select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                        if payt3 == "1":
                            redr3 = input(
                                "Activation of 6.75GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                "99. Next \n"
                                "Select:")
                            if redr3 == "99":
                                pass
                            else:
                                print(f"Invalid Selection {redr3}")
                        elif payt3 == "2":
                            momo3 = input(
                                "Dear Vaia Joseph, you are buying MTN 6.75GB monthly Plan data bundle for N3000 valid till 01/04/2026 for 2349164900946 \n"
                                "Please enter your MoMo Pin to confirm:")
                            if momo3 == "00000000":
                                pass
                            else:
                                print("Invalid pin")
                        else:
                            print(f"Invalid Selection {payt3}")
                    elif actv12 == "3":
                        code2 = input("Enter your coupon code:")
                        if code2 == "12345678":
                            pass
                        else:
                            print("unable to fetch coupon details")
                    else:
                        print(f"Invalid Selection {actv12}")
                elif mthly == "5":
                    actv13 = input("Get 7GB+2GB All Night for N3,500. To proceed, Select:\n"
                                  "1. Auto-Renew \n"
                                  "2. One-Off \n"
                                  "3. Buy for a Friend \n"
                                  "Select:"
                    )
                    if actv13 == "1":
                        print(
                            "Activation of 9GB monthly plan at N3500 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv13 == "2":
                        payta = input("kindly Select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                        if payta == "1":
                            redra = input(
                                "Activation of 9GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                "99. Next \n"
                                "Select:")
                            if redra == "99":
                                pass
                            else:
                                print(f"Invalid Selection {redra}")
                        elif payta == "2":
                            momo3 = input(
                                "Dear Vaia Joseph, you are buying MTN 9GB monthly Plan data bundle for N3500 valid till 01/04/2026 for 2349164900946 \n"
                                "Please enter your MoMo Pin to confirm:")
                            if momo3 == "00000000":
                                pass
                            else:
                                print("Invalid pin")
                    elif actv13 == "3":
                        tel = input("Enter recipient's number:")
                        if len(tel) == 11 and tel.isnumeric() and (
                                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
                            0:3] == "091"):
                            tel2 = input("Confirm recipient's number:")
                            if len(tel2) == 11 and tel2.isnumeric() and (
                                    tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                0:3] == "090" or tel2[
                                        0:3] == "091"):
                                pass
                            else:
                                print(f"{tel2} is not a valid number")
                    else:
                        print(f"Invalid Selection {actv13}")
                elif mthly == "6":
                    actv14 = input("Get 10GB+10mins+2GB All Night+200MB YT Music for N4500. To proceed, Select:\n"
                                  "1. Auto-Renew \n"
                                  "2. One-Off \n"
                                  "3. Buy for a Friend \n"
                                  "4. Redeem Promo Code \n"
                                  "Select:")
                    if actv14 == "1":
                        print(
                            "Activation of 12GB monthly plan at N4500 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv14 == "2":
                        payta = input("kindly Select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                        if payta == "1":
                            redra = input(
                                "Activation of 12GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                "99. Next \n"
                                "Select:")
                            if redra == "99":
                                pass
                            else:
                                print(f"Invalid Selection {redra}")
                        elif payta == "2":
                            momo3 = input(
                                "Dear Vaia Joseph, you are buying MTN 12GB monthly Plan data bundle for N4500 valid till 01/04/2026 for 2349164900946 \n"
                                "Please enter your MoMo Pin to confirm:")
                            if momo3 == "00000000":
                                pass
                            else:
                                print("Invalid pin")
                    elif actv14 == "3":
                        tel = input("Enter recipient's number:")
                        if len(tel) == 11 and tel.isnumeric() and (
                                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
                            0:3] == "091"):
                            tel2 = input("Confirm recipient's number:")
                            if len(tel2) == 11 and tel2.isnumeric() and (
                                    tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                0:3] == "090" or tel2[
                                        0:3] == "091"):
                                pass
                            else:
                                print(f"{tel2} is not a valid number")
                    elif actv14 == "4":
                        code2 = input("Enter your coupon code:")
                        if code2 == "12345678":
                            pass
                        else:
                            print("unable to fetch coupon details")
                    else:
                        print(f"Invalid Selection {actv14}")
                elif mthly == "7":
                    actv15 = input("You will pay N5,000 for 14.5GB Value Data Plan. To proceed, Select:\n"
                                   "1. Auto-Renew \n"
                                   "2. One-Off \n"
                                   "3. Redeem Promo Code \n"
                                   "Select:"
                    )
                    if actv15 == "1":
                        print(
                            "Activation of 14.5GB monthly plan at N5000 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv15 == "2":
                        payta = input("kindly Select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                        if payta == "1":
                            redra = input(
                                "Activation of 14.5GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                "99. Next \n"
                                "Select:")
                            if redra == "99":
                                pass
                            else:
                                print(f"Invalid Selection {redra}")
                    elif actv15 == "3":
                        tel = input("Enter recipient's number:")
                        if len(tel) == 11 and tel.isnumeric() and (
                                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[0:3] == "090" or tel[
                            0:3] == "091"):
                            tel2 = input("Confirm recipient's number:")
                            if len(tel2) == 11 and tel2.isnumeric() and (
                                    tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                0:3] == "090" or tel2[
                                        0:3] == "091"):
                                pass
                            else:
                                print(f"{tel2} is not a valid number")
                    elif actv15 == "4":
                        code2 = input("Enter your coupon code:")
                        if code2 == "12345678":
                            pass
                        else:
                            print("unable to fetch coupon details")
                    else:
                        print(f"Invalid Selection {actv15}")
                elif mthly == "99":
                    mthly2 = input("8. N5,500 = 12.5GB+36mins \n"
                                  "9. N6,500 = 16.5GB+2GB \n"
                                  "10. N7,500 = 20GB+4GB \n"
                                  "11. N5,500 =12.5GB+2GB \n"
                                  "12. N9,000 = 25GB+4GB \n"
                                  "13. N11,000 = 36GB \n"
                                  "99. Next \n"
                                  "Select"
                    )
                    if mthly2 == "8":
                        actv9 = input(
                            "Buy XtraData5500 @N5500 & get 12.5GB+36mins+15 SMS, valid for 30 days. To proceed, select:\n"
                            "1. Auto-Renew \n"
                            "2. One-Off \n"
                            "Select:")
                        if actv9 == "1":
                            print(
                                "Activation of XtraData5500 at N5500 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                        elif actv9 == "2":
                            paym = input("kindly Select payment type \n"
                                         "1. Airtime \n"
                                         "2. MoMo PSB Wallet \n"
                                         "Select:")
                            if paym == "1":
                                paym2 = input(
                                    "Activation of XtraData5500 failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                    "99. Next \n"
                                    "Select:")
                                if paym2 == "99":
                                    pass
                                else:
                                    print(f"Invalid Selection {paym2}")
                            elif paym == "2":
                                momo = input(
                                    "Dear Olabisi Victoria, you are buying MTN XtraData for N5500 valid till 01/04/2026 for 2349164900946 \n"
                                    "Please enter your MoMo Pin to confirm:")
                                if momo == "00000000":
                                    pass
                                else:
                                    print("Invalid pin")
                    elif mthly2 == "9":
                        actv10 = input("Get 16.5GB+10mins+2GB All Night+300MB YT Music for N6,500. To proceed, Select:\n"
                                       "1. Auto-Renew \n"
                                       "2. One-Off \n"
                                       "3. Buy for a Friend \n"
                                       "4. Redeem Promo Code \n"
                                       "Select:")
                        if actv10 == "1":
                            print(
                                "Activation of 18.5GB monthly plan at N6500 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                        elif actv10 == "2":
                            payt2 = input("kindly Select payment type \n"
                                          "1. Airtime \n"
                                          "2. MoMo PSB Wallet \n"
                                          "Select:"
                                          )
                            if payt2 == "1":
                                redr2 = input(
                                    "Activation of 18.5GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                    "99. Next \n"
                                    "Select:")
                                if redr2 == "99":
                                    pass
                                else:
                                    print(f"Invalid Selection {redr2}")
                            elif payt2 == "2":
                                momo2 = input(
                                    "Dear Vaia Joseph, you are buying MTN 18.5GB monthly Plan data bundle for N2000 valid till 01/04/2026 for 2349164900946 \n"
                                    "Please enter your MoMo Pin to confirm:")
                                if momo2 == "00000000":
                                    pass
                                else:
                                    print("Invalid pin")
                            else:
                                print(f"Invalid Selection {payt2}")
                        elif actv10 == "3":
                            tel = input("Enter recipient's number:")
                            if len(tel) == 11 and tel.isnumeric() and (
                                    tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                                0:3] == "090" or tel[
                                        0:3] == "091"):
                                tel2 = input("Confirm recipient's number:")
                                if len(tel2) == 11 and tel2.isnumeric() and (
                                        tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                    0:3] == "090" or tel2[
                                            0:3] == "091"):
                                    pass
                                else:
                                    print(f"{tel2} is not a valid number")
                            else:
                                print(f"{tel} is not a valid number.")
                        elif actv10 == "4":
                            code2 = input("Enter your coupon code:")
                            if code2 == "12345678":
                                pass
                            else:
                                print("Unable to fetch coupon details")
                        else:
                            print(f"Invalid selection {actv10}")
                    elif mthly2 == "10":
                        actv11 = input("Get 20GB+4GB All Night for N7,500. To proceed, Select:\n"
                                       "1. Auto-Renew \n"
                                       "2. One-Off \n"
                                       "3. Buy for a Friend \n"
                                       "4. Redeem Promo Code \n"
                                       "Select:")
                        if actv11 == "1":
                            print(
                                "Activation of 24GB monthly plan at N7,500 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                        elif actv11 == "2":
                            payt2 = input("kindly Select payment type \n"
                                          "1. Airtime \n"
                                          "2. MoMo PSB Wallet \n"
                                          "Select:"
                                          )
                            if payt2 == "1":
                                redr2 = input(
                                    "Activation of 24GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                    "99. Next \n"
                                    "Select:")
                                if redr2 == "99":
                                    pass
                                else:
                                    print(f"Invalid Selection {redr2}")
                            elif payt2 == "2":
                                momo2 = input(
                                    "Dear Vaia Joseph, you are buying MTN 24GB monthly Plan data bundle for N7,500 valid till 01/04/2026 for 2349164900946 \n"
                                    "Please enter your MoMo Pin to confirm:")
                                if momo2 == "00000000":
                                    pass
                                else:
                                    print("Invalid pin")
                            else:
                                print(f"Invalid Selection {payt2}")
                        elif actv11 == "3":
                            tel = input("Enter recipient's number:")
                            if len(tel) == 11 and tel.isnumeric() and (
                                    tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                                0:3] == "090" or tel[
                                        0:3] == "091"):
                                tel2 = input("Confirm recipient's number:")
                                if len(tel2) == 11 and tel2.isnumeric() and (
                                        tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                    0:3] == "090" or tel2[
                                            0:3] == "091"):
                                    pass
                                else:
                                    print(f"{tel2} is not a valid number")
                            else:
                                print(f"{tel} is not a valid number.")
                        elif actv11 == "4":
                            code2 = input("Enter your coupon code:")
                            if code2 == "12345678":
                                pass
                            else:
                                print("unable to fetch coupon details")
                        else:
                            print(f"Invalid selection {actv11}")
                    elif mthly2 == "11":
                        actv12 = input("Get 12.5GB+2GB All Night+300MB YT Music for N5,500. To proceed, Select:\n"
                                       "1. Auto-Renew \n"
                                       "2. One-Off \n"
                                       "3. Buy for a Friend \n"
                                       "Select:"
                                       )
                        if actv12 == "1":
                            print(
                                "Activation of 12.5GB monthly plan at N5,500 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                        elif actv12 == "2":
                            payt3 = input("kindly Select payment type \n"
                                          "1. Airtime \n"
                                          "2. MoMo PSB Wallet \n"
                                          "Select:"
                                          )
                            if payt3 == "1":
                                redr3 = input(
                                    "Activation of 12.5GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                    "99. Next \n"
                                    "Select:")
                                if redr3 == "99":
                                    pass
                                else:
                                    print(f"Invalid Selection {redr3}")
                            elif payt3 == "2":
                                momo3 = input(
                                    "Dear Vaia Joseph, you are buying MTN 12.5GB monthly Plan data bundle for N3000 valid till 01/04/2026 for 2349164900946 \n"
                                    "Please enter your MoMo Pin to confirm:")
                                if momo3 == "00000000":
                                    pass
                                else:
                                    print("Invalid pin")
                            else:
                                print(f"Invalid Selection {payt3}")
                        elif actv12 == "3":
                            tel = input("Enter recipient's number:")
                            if len(tel) == 11 and tel.isnumeric() and (
                                    tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                                0:3] == "090" or tel[
                                        0:3] == "091"):
                                tel2 = input("Confirm recipient's number:")
                                if len(tel2) == 11 and tel2.isnumeric() and (
                                        tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                    0:3] == "090" or tel2[
                                            0:3] == "091"):
                                    pass
                                else:
                                    print(f"{tel2} is not a valid number")
                        if actv12 == "1":
                            print(
                                "Activation of 12.5GB monthly plan at N5,500 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                        elif actv12 == "2":
                            payt3 = input("kindly Select payment type \n"
                                          "1. Airtime \n"
                                          "2. MoMo PSB Wallet \n"
                                          "Select:"
                                          )
                            if payt3 == "1":
                                redr3 = input(
                                    "Activation of 12.5GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                    "99. Next \n"
                                    "Select:")
                                if redr3 == "99":
                                    pass
                                else:
                                    print(f"Invalid Selection {redr3}")
                            elif payt3 == "2":
                                momo3 = input(
                                    "Dear Vaia Joseph, you are buying MTN 12.5GB monthly Plan data bundle for N3000 valid till 01/04/2026 for 2349164900946 \n"
                                    "Please enter your MoMo Pin to confirm:")
                                if momo3 == "00000000":
                                    pass
                                else:
                                    print("Invalid pin")
                            else:
                                print(f"Invalid Selection {payt3}")
                        elif actv12 == "3":
                            tel = input("Enter recipient's number:")
                            if len(tel) == 11 and tel.isnumeric() and (
                                    tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                                0:3] == "090" or tel[
                                        0:3] == "091"):
                                tel2 = input("Confirm recipient's number:")
                                if len(tel2) == 11 and tel2.isnumeric() and (
                                        tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                    0:3] == "090" or tel2[
                                            0:3] == "091"):
                                    pass
                                else:
                                    print(f"{tel2} is not a valid number")
                            else:
                                print(f"{tel} is not a valid number.")
                        else:
                            print(f"Invalid Selection {actv12}")
                    elif mthly2 == "12":
                        actv13 = input("Get 25GB+4GB All Night for N9,000. To proceed, Select:\n"
                                       "1. Auto-Renew \n"
                                       "2. One-Off \n"
                                       "3. Buy for a Friend \n"
                                       "4. Redeem Promo Code \n"
                                       "Select:")
                        if actv13 == "1":
                            print(
                                "Activation of 29GB monthly plan at N9000 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                        elif actv13 == "2":
                            payt2 = input("kindly Select payment type \n"
                                          "1. Airtime \n"
                                          "2. MoMo PSB Wallet \n"
                                          "Select:"
                                          )
                            if payt2 == "1":
                                redr2 = input(
                                    "Activation of 29GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                    "99. Next \n"
                                    "Select:")
                                if redr2 == "99":
                                    pass
                                else:
                                    print(f"Invalid Selection {redr2}")
                            elif payt2 == "2":
                                momo2 = input(
                                    "Dear Vaia Joseph, you are buying MTN 29GB monthly Plan data bundle for N9000 valid till 01/04/2026 for 2349164900946 \n"
                                    "Please enter your MoMo Pin to confirm:")
                                if momo2 == "00000000":
                                    pass
                                else:
                                    print("Invalid pin")
                            else:
                                print(f"Invalid Selection {payt2}")
                        elif actv13 == "3":
                            tel = input("Enter recipient's number:")
                            if len(tel) == 11 and tel.isnumeric() and (
                                    tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                                0:3] == "090" or tel[
                                        0:3] == "091"):
                                tel2 = input("Confirm recipient's number:")
                                if len(tel2) == 11 and tel2.isnumeric() and (
                                        tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                    0:3] == "090" or tel2[
                                            0:3] == "091"):
                                    pass
                                else:
                                    print(f"{tel2} is not a valid number")
                            else:
                                print(f"{tel} is not a valid number.")
                        elif actv13 == "4":
                            code2 = input("Enter your coupon code:")
                            if code2 == "12345678":
                                pass
                            else:
                                print("unable to fetch coupon details")
                        else:
                            print(f"Invalid Selection {actv13}")
                    elif mthly2 == "13":
                        actv14 = input("Get 36GB for N11,000. To proceed, Select:\n"
                                       "1. Auto-Renew \n"
                                       "2. One-Off \n"
                                       "3. Buy for a Friend \n"
                                       "4. Redeem Promo Code \n"
                                       "Select:")
                        if actv14 == "1":
                            print(
                                "Activation of 36GB monthly plan at N11000 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                        elif actv14 == "2":
                            payta = input("kindly Select payment type \n"
                                          "1. Airtime \n"
                                          "2. MoMo PSB Wallet \n"
                                          "Select:"
                                          )
                            if payta == "1":
                                redra = input(
                                    "Activation of 36GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                    "99. Next \n"
                                    "Select:")
                                if redra == "99":
                                    pass
                                else:
                                    print(f"Invalid Selection {redra}")
                            elif payta == "2":
                                momo3 = input(
                                    "Dear Vaia Joseph, you are buying MTN 36GB monthly Plan data bundle for N11,000 valid till 01/04/2026 for 2349164900946 \n"
                                    "Please enter your MoMo Pin to confirm:")
                                if momo3 == "00000000":
                                    pass
                                else:
                                    print("Invalid pin")
                        elif actv14 == "3":
                            tel = input("Enter recipient's number:")
                            if len(tel) == 11 and tel.isnumeric() and (
                                    tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                                0:3] == "090" or tel[
                                        0:3] == "091"):
                                tel2 = input("Confirm recipient's number:")
                                if len(tel2) == 11 and tel2.isnumeric() and (
                                        tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                    0:3] == "090" or tel2[
                                            0:3] == "091"):
                                    pass
                                else:
                                    print(f"{tel2} is not a valid number")
                        elif actv14 == "4":
                            code2 = input("Enter your coupon code:")
                            if code2 == "12345678":
                                pass
                            else:
                                print("unable to fetch coupon details")
                    elif mthly2 == "99":
                        reder= input("14. N16,000 = 65GB \n"
                                     "15. N18,000 = 75GB \n"
                                     "16. N35,000 = 165GB \n"
                                     "17. N55,000 = 250GB \n"
                                     "Select:"

                        )
                        if reder == "14":
                            actv20 = input(
                                "Get 65GB Monthly Plan for N16,000. To proceed, select:\n"
                                "1. Auto-Renew \n"
                                "2. One-Off \n"
                                "3. Buy for a Friend \n"
                                "4. Redeem Promo Code \n"
                                "Select:")
                            if actv20 == "1":
                                print(
                                    "Activation of 65GB monthly at N16,000 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                            elif actv20 == "2":
                                paym = input("kindly Select payment type \n"
                                             "1. Airtime \n"
                                             "2. MoMo PSB Wallet \n"
                                             "Select:")
                                if paym == "1":
                                    paym2 = input(
                                        "Activation of 65GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                        "99. Next \n"
                                        "Select:")
                                    if paym2 == "99":
                                        print("MMI Complete")
                                    else:
                                        print(f"Invalid Selection {paym2}")
                                elif paym == "2":
                                    momo = input(
                                        "Dear Olabisi Victoria, you are buying MTN Data 65GB for N16,000 valid till 01/04/2026 for 2349164900946 \n"
                                        "Please enter your MoMo Pin to confirm:")
                                    if momo == "00000000":
                                        pass
                                    else:
                                        print("Invalid pin")
                            elif actv20 == "3":
                                tel = input("Enter recipient's number:")
                                if len(tel) == 11 and tel.isnumeric() and (
                                        tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                                    0:3] == "090" or tel[
                                            0:3] == "091"):
                                    tel2 = input("Confirm recipient's number:")
                                    if len(tel2) == 11 and tel2.isnumeric() and (
                                            tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                        0:3] == "090" or tel2[
                                                0:3] == "091"):
                                        pass
                                    else:
                                        print(f"{tel2} is not a valid number")
                                else:
                                    print(f"{tel} is not a valid number.")
                            elif actv20 == "4":
                                code2 = input("Enter your coupon code:")
                                if code2 == "12345678":
                                    pass
                                else:
                                    print("Unable to fetch coupon details")
                            else:
                                print(f"Invalid selection {actv20}")
                        elif reder == "15":
                            actv21 = input(
                                "Get 75GB monthly for N18,000. To proceed, Select:\n"
                                "1. Auto-Renew \n"
                                "2. One-Off \n"
                                "3. Buy for a Friend \n"
                                "4. Redeem Promo Code \n"
                                "Select:"
                            )
                            if actv21 == "1":
                                print(
                                    "Activation of 75GB monthly plan at N18,000 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                            elif actv21 == "2":
                                payt2 = input("kindly Select payment type \n"
                                              "1. Airtime \n"
                                              "2. MoMo PSB Wallet \n"
                                              "Select:"
                                              )
                                if payt2 == "1":
                                    redr2 = input(
                                        "Activation of 75GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                        "99. Next \n"
                                        "Select:")
                                    if redr2 == "99":
                                        pass
                                    else:
                                        print(f"Invalid Selection {redr2}")
                                elif payt2 == "2":
                                    momo2 = input(
                                        "Dear Vaia Joseph, you are buying MTN 18.5GB monthly Plan data bundle for N2000 valid till 01/04/2026 for 2349164900946 \n"
                                        "Please enter your MoMo Pin to confirm:")
                                    if momo2 == "00000000":
                                        pass
                                    else:
                                        print("Invalid pin")
                                elif actv21 == "3":
                                    tel = input("Enter recipient's number:")
                                    if len(tel) == 11 and tel.isnumeric() and (
                                            tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                                        0:3] == "090" or tel[
                                                0:3] == "091"):
                                        tel2 = input("Confirm recipient's number:")
                                        if len(tel2) == 11 and tel2.isnumeric() and (
                                                tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                            0:3] == "090" or tel2[
                                                    0:3] == "091"):
                                            pass
                                        else:
                                            print(f"{tel2} is not a valid number")
                                    else:
                                        print(f"{tel} is not a valid number.")
                                elif actv21 == "4":
                                    code2 = input("Enter your coupon code:")
                                    if code2 == "12345678":
                                        pass
                                    else:
                                        print("Unable to fetch coupon details")
                                else:
                                    print(f"Invalid selection {actv21}")
                        elif reder == "16":
                            actv22 = input("Get 165GB Monthly for N35,000. To proceed, Select:\n"
                                           "1. Auto-Renew \n"
                                           "2. One-Off \n"
                                           "3. Buy for a Friend \n"
                                           "4. Redeem Promo Code \n"
                                           "Select:")
                            if actv22 == "1":
                                print(
                                    "Activation of 165GB monthly plan at N35,000 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                            elif actv22 == "2":
                                payt2 = input("kindly Select payment type \n"
                                              "1. Airtime \n"
                                              "2. MoMo PSB Wallet \n"
                                              "Select:"
                                              )
                                if payt2 == "1":
                                    redr2 = input(
                                        "Activation of 165GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                        "99. Next \n"
                                        "Select:")
                                    if redr2 == "99":
                                        print("MMI Complete!")
                                    else:
                                        print(f"Invalid Selection {redr2}")
                                elif payt2 == "2":
                                    momo2 = input(
                                        "Dear Vaia Joseph, you are buying MTN 165GB monthly Plan data bundle for N35,000 valid till 01/04/2026 for 2349164900946 \n"
                                        "Please enter your MoMo Pin to confirm:")
                                    if momo2 == "00000000":
                                        pass
                                    else:
                                        print("Invalid pin")
                                else:
                                    print(f"Invalid Selection {payt2}")
                            elif actv22 == "3":
                                tel = input("Enter recipient's number:")
                                if len(tel) == 11 and tel.isnumeric() and (
                                        tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                                    0:3] == "090" or tel[
                                            0:3] == "091"):
                                    tel2 = input("Confirm recipient's number:")
                                    if len(tel2) == 11 and tel2.isnumeric() and (
                                            tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                        0:3] == "090" or tel2[
                                                0:3] == "091"):
                                        pass
                                    else:
                                        print(f"{tel2} is not a valid number")
                                else:
                                    print(f"{tel} is not a valid number.")
                            elif actv22 == "4":
                                code2 = input("Enter your coupon code:")
                                if code2 == "12345678":
                                    pass
                                else:
                                    print("unable to fetch coupon details")
                            else:
                                print(f"Invalid selection {actv22}")
                        elif reder == "17":
                            actv23 = input("Get 250GB Monthly for N55,000. To proceed, Select:\n"
                                           "1. Auto-Renew \n"
                                           "2. One-Off \n"
                                           "3. Buy for a Friend \n"
                                           "4. Redeem Promo Code \n"
                                           "Select:")
                            if actv23 == "1":
                                print(
                                    "Activation of 250GB monthly plan at N55,000 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                            elif actv23 == "2":
                                payt2 = input("kindly Select payment type \n"
                                              "1. Airtime \n"
                                              "2. MoMo PSB Wallet \n"
                                              "Select:"
                                              )
                                if payt2 == "1":
                                    redr2 = input(
                                        "Activation of 250GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                        "99. Next \n"
                                        "Select:")
                                    if redr2 == "99":
                                        print("MMI Complete!")
                                    else:
                                        print(f"Invalid Selection {redr2}")
                                elif payt2 == "2":
                                    momo2 = input(
                                        "Dear Vaia Joseph, you are buying MTN 250GB monthly Plan data bundle for N55,000 valid till 01/04/2026 for 2349164900946 \n"
                                        "Please enter your MoMo Pin to confirm:")
                                    if momo2 == "00000000":
                                        pass
                                    else:
                                        print("Invalid pin")
                                else:
                                    print(f"Invalid Selection {payt2}")
                            elif actv23 == "3":
                                tel = input("Enter recipient's number:")
                                if len(tel) == 11 and tel.isnumeric() and (
                                        tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                                    0:3] == "090" or tel[
                                            0:3] == "091"):
                                    tel2 = input("Confirm recipient's number:")
                                    if len(tel2) == 11 and tel2.isnumeric() and (
                                            tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                        0:3] == "090" or tel2[
                                                0:3] == "091"):
                                        pass
                                    else:
                                        print(f"{tel2} is not a valid number")
                                else:
                                    print(f"{tel} is not a valid number.")
                            elif actv23 == "4":
                                code2 = input("Enter your coupon code:")
                                if code2 == "12345678":
                                    pass
                                else:
                                    print("unable to fetch coupon details")
                            else:
                                print(f"Invalid selection {actv23}")
                        else:
                            print(f"Invalid Selection {reder}")
                    else:
                        print(f"Invalid Selection {mthly2}")
                else:
                    print(f"Invalid Selection {mthly}")
            elif plans == "5":
                tmth= input("2months+ \n"
                            "1. N25,000 = 90GB/60Days \n"
                            "2. N40,000 = 150GB/60Days \n"
                            "3. N90,000 = 480GB/90Days \n"
                            "4. N125,000 = 800GB/365Days \n"
                            "Select:"
                )
                if tmth == "1":
                    actv9 = input(
                        "You will pay N25,000 for 90GB 2-month plan. To proceed, select:\n"
                        "1. Auto-Renew \n"
                        "2. One-Off \n"
                        "3. Buy for a Friend \n"
                        "4. Redeem Promo Code \n"
                        "Select:"
                    )
                    if actv9 == "1":
                        print(
                            "Activation of 90GB at N25,000 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv9 == "2":
                        paym = input("kindly Select payment type \n"
                                     "1. Airtime \n"
                                     "2. MoMo PSB Wallet \n"
                                     "Select:")
                        if paym == "1":
                            paym2 = input(
                                "Activation of 90GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                "99. Next \n"
                                "Select:")
                            if paym2 == "99":
                                pass
                            else:
                                print(f"Invalid Selection {paym2}")
                        elif paym == "2":
                            momo = input(
                                "Dear Olabisi Victoria, you are buying MTN Data 90GB for N25,000 valid till 01/04/2026 for 2349164900946 \n"
                                "Please enter your MoMo Pin to confirm:")
                            if momo == "00000000":
                                pass
                            else:
                                print("Invalid pin")
                elif tmth == "2":
                    actv10 = input("You will pay N40,000 for 150GB 2-month plan. To proceed, Select:\n"
                                   "1. Auto-Renew \n"
                                   "2. One-Off \n"
                                   "3. Buy for a Friend \n"
                                   "4. Redeem Promo Code \n"
                                   "Select:")
                    if actv10 == "1":
                        print(
                            "Activation of 150GB 2-month plan at N40,000 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv10 == "2":
                        payt2 = input("kindly Select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                        if payt2 == "1":
                            redr2 = input(
                                "Activation of 150GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                "99. Next \n"
                                "Select:")
                            if redr2 == "99":
                                print("MMI Complete!")
                            else:
                                print(f"Invalid Selection {redr2}")
                        elif payt2 == "2":
                            momo2 = input(
                                "Dear Vaia Joseph, you are buying MTN 150GB 2-month Plan data bundle for N40,000 valid till 01/04/2026 for 2349164900946 \n"
                                "Please enter your MoMo Pin to confirm:")
                            if momo2 == "00000000":
                                pass
                            else:
                                print("Invalid pin")
                        else:
                            print(f"Invalid Selection {payt2}")
                    elif actv10 == "3":
                        tel = input("Enter recipient's number:")
                        if len(tel) == 11 and tel.isnumeric() and (
                                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                            0:3] == "090" or tel[
                                    0:3] == "091"):
                            tel2 = input("Confirm recipient's number:")
                            if len(tel2) == 11 and tel2.isnumeric() and (
                                    tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                0:3] == "090" or tel2[
                                        0:3] == "091"):
                                pass
                            else:
                                print(f"{tel2} is not a valid number")
                        else:
                            print(f"{tel} is not a valid number.")
                    elif actv10 == "4":
                        code2 = input("Enter your coupon code:")
                        if code2 == "12345678":
                            pass
                        else:
                            print("Unable to fetch coupon details")
                    else:
                        print(f"Invalid selection {actv10}")
                elif tmth == "3":
                    actv11 = input("You will pay N90,000 for 480GB 3-month plan. To proceed, Select:\n"
                                   "1. Auto-Renew \n"
                                   "2. One-Off \n"
                                   "3. Buy for a Friend \n"
                                   "4. Redeem Promo Code \n"
                                   "Select:")
                    if actv11 == "1":
                        print(
                            "Activation of 480GB 3-month plan at N90,000 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv11 == "2":
                        payt2 = input("kindly Select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                        if payt2 == "1":
                            redr2 = input(
                                "Activation of 480GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                "99. Next \n"
                                "Select:")
                            if redr2 == "99":
                                print("MMI Complete!")
                            else:
                                print(f"Invalid Selection {redr2}")
                        elif payt2 == "2":
                            momo2 = input(
                                "Dear Vaia Joseph, you are buying MTN 480GB 3-month Plan data bundle for N90,000 valid till 01/04/2026 for 2349164900946 \n"
                                "Please enter your MoMo Pin to confirm:")
                            if momo2 == "00000000":
                                pass
                            else:
                                print("Invalid pin")
                        else:
                            print(f"Invalid Selection {payt2}")
                    elif actv11 == "3":
                        tel = input("Enter recipient's number:")
                        if len(tel) == 11 and tel.isnumeric() and (
                                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                            0:3] == "090" or tel[
                                    0:3] == "091"):
                            tel2 = input("Confirm recipient's number:")
                            if len(tel2) == 11 and tel2.isnumeric() and (
                                    tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                0:3] == "090" or tel2[
                                        0:3] == "091"):
                                pass
                            else:
                                print(f"{tel2} is not a valid number")
                        else:
                            print(f"{tel} is not a valid number.")
                    elif actv11 == "4":
                        code2 = input("Enter your coupon code:")
                        if code2 == "12345678":
                            pass
                        else:
                            print("unable to fetch coupon details")
                    else:
                        print(f"Invalid selection {actv11}")
                elif tmth == "4":
                    actv11 = input("You will pay N125,000 for 800GB 1-year plan. To proceed, Select:\n"
                                   "1. Auto-Renew \n"
                                   "2. One-Off \n"
                                   "3. Buy for a Friend \n"
                                   "4. Redeem Promo Code \n"
                                   "Select:")
                    if actv11 == "1":
                        print(
                            "Activation of 800GB 1-year plan at N125,000 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                    elif actv11 == "2":
                        payt2 = input("kindly Select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                        if payt2 == "1":
                            redr2 = input(
                                "Activation of 800GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                "99. Next \n"
                                "Select:")
                            if redr2 == "99":
                                print("MMI Complete!")
                            else:
                                print(f"Invalid Selection {redr2}")
                        elif payt2 == "2":
                            momo2 = input(
                                "Dear Vaia Joseph, you are buying MTN 800GB 1-year Plan data bundle for N125,000 valid till 01/04/2026 for 2349164900946 \n"
                                "Please enter your MoMo Pin to confirm:")
                            if momo2 == "00000000":
                                pass
                            else:
                                print("Invalid pin")
                        else:
                            print(f"Invalid Selection {payt2}")
                    elif actv11 == "3":
                        tel = input("Enter recipient's number:")
                        if len(tel) == 11 and tel.isnumeric() and (
                                tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                            0:3] == "090" or tel[
                                    0:3] == "091"):
                            tel2 = input("Confirm recipient's number:")
                            if len(tel2) == 11 and tel2.isnumeric() and (
                                    tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                0:3] == "090" or tel2[
                                        0:3] == "091"):
                                pass
                            else:
                                print(f"{tel2} is not a valid number")
                        else:
                            print(f"{tel} is not a valid number.")
                    elif actv11 == "4":
                        code2 = input("Enter your coupon code:")
                        if code2 == "12345678":
                            pass
                        else:
                            print("unable to fetch coupon details")
                    else:
                        print(f"Invalid selection {actv11}")
                else:
                    print(f"Invalid Selection {tmth}")
            elif plans == "6":
                social= input("1. Whatsapp \n"
                              "2. Facebook \n"
                              "3. Instagram \n"
                              "4. TikTok \n"
                              "5. Ayoba \n"
                              "6. All Socials Bundle \n"
                              "Select"
                )
                if social == "1":
                    whaap= input("WhatsApp \n"
                                 "1. Daily @ N25 for 20MB \n"
                                 "2. Weekly @ N50 for 40MB \n"
                                 "3. Monthly @ N150 for 120MB \n"
                                 "Select:"
                    )
                    if whaap == "1":
                        whaap1= input("You will pay N25 for 20MB WhatsApp Daily Plan. To Proceed, Select: \n"
                                      "1. Auto-Renew \n"
                                      "2. One-Off Purchase \n"
                                      "3. Buy for a Friend \n"
                                      "Select:"
                        )
                    elif whaap == "2":
                        whaap2= input("You will pay N50 for 40MB WhatsApp Weekly Plan. To Proceed, Select: \n"
                                      "1. Auto-Renew \n"
                                      "2. One-Off Purchase \n"
                                      "3. Buy for a Friend \n"
                                      "Select:"
                                      )
                        if whaap2 == "1":
                            print(
                                "Activation of 12.5GB monthly plan at N5,500 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                        elif whaap2 == "2":
                            payt3 = input("kindly Select payment type \n"
                                          "1. Airtime \n"
                                          "2. MoMo PSB Wallet \n"
                                          "Select:"
                                          )
                            if payt3 == "1":
                                redr3 = input(
                                    "Activation of 12.5GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                    "99. Next \n"
                                    "Select:")
                                if redr3 == "99":
                                    pass
                                else:
                                    print(f"Invalid Selection {redr3}")
                            elif payt3 == "2":
                                momo3 = input(
                                    "Dear Vaia Joseph, you are buying MTN 12.5GB monthly Plan data bundle for N3000 valid till 01/04/2026 for 2349164900946 \n"
                                    "Please enter your MoMo Pin to confirm:")
                                if momo3 == "00000000":
                                    pass
                                else:
                                    print("Invalid pin")
                            else:
                                print(f"Invalid Selection {payt3}")
                        elif whaap2 == "3":
                            tel = input("Enter recipient's number:")
                            if len(tel) == 11 and tel.isnumeric() and (
                                    tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                                0:3] == "090" or tel[
                                        0:3] == "091"):
                                tel2 = input("Confirm recipient's number:")
                                if len(tel2) == 11 and tel2.isnumeric() and (
                                        tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                    0:3] == "090" or tel2[
                                            0:3] == "091"):
                                    pass
                                else:
                                    print(f"{tel2} is not a valid number")
                        else:
                            print(f"Invalid Selection {whaap2}")
                    elif whaap == "3":
                        whaap3= input("You will pay N150 for 120MB WhatsApp Monthly Plan. To Proceed, Select: \n"
                                      "1. Auto-Renew \n"
                                      "2. One-Off Purchase \n"
                                      "3. Buy for a Friend \n"
                                      "Select:"
                        )
                        if whaap3 == "1":
                            print(
                                "Activation of 12.5GB monthly plan at N5,500 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                        elif whaap3 == "2":
                            payt3 = input("kindly Select payment type \n"
                                          "1. Airtime \n"
                                          "2. MoMo PSB Wallet \n"
                                          "Select:"
                                          )
                            if payt3 == "1":
                                redr3 = input(
                                    "Activation of 12.5GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                    "99. Next \n"
                                    "Select:")
                                if redr3 == "99":
                                    pass
                                else:
                                    print(f"Invalid Selection {redr3}")
                            elif payt3 == "2":
                                momo3 = input(
                                    "Dear Vaia Joseph, you are buying MTN 12.5GB monthly Plan data bundle for N3000 valid till 01/04/2026 for 2349164900946 \n"
                                    "Please enter your MoMo Pin to confirm:")
                                if momo3 == "00000000":
                                    pass
                                else:
                                    print("Invalid pin")
                            else:
                                print(f"Invalid Selection {payt3}")
                        elif whaap3 == "3":
                            tel = input("Enter recipient's number:")
                            if len(tel) == 11 and tel.isnumeric() and (
                                    tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                                0:3] == "090" or tel[
                                        0:3] == "091"):
                                tel2 = input("Confirm recipient's number:")
                                if len(tel2) == 11 and tel2.isnumeric() and (
                                        tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                    0:3] == "090" or tel2[
                                            0:3] == "091"):
                                    pass
                                else:
                                    print(f"{tel2} is not a valid number")
                        else:
                            print(f"Invalid Selection {whaap3}")
                    else:
                        print(f"Invalid Selection {whaap}")
                elif social == "2":
                    fbook= input("Facebook \n"
                                 "1. Daily @ N25 for 20MB \n"
                                 "2. Weekly @ N50 for 40MB \n"
                                 "3. Monthly @ N150 for 120MB \n"
                                 "Select:"
                    )
                    if fbook == "1":
                        fbook1= input("You will pay N25 for 20MB Facebook Daily Plan. To Proceed, Select: \n"
                                      "1. Auto-Renew \n"
                                      "2. One-Off Purchase \n"
                                      "3. Buy for a Friend \n"
                                      "Select:"
                        )
                        if fbook1 == "1":
                            print(
                                "Activation of 12.5GB monthly plan at N5,500 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                        elif fbook1 == "2":
                            payt3 = input("kindly Select payment type \n"
                                          "1. Airtime \n"
                                          "2. MoMo PSB Wallet \n"
                                          "Select:"
                                          )
                            if payt3 == "1":
                                redr3 = input(
                                    "Activation of 12.5GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                    "99. Next \n"
                                    "Select:")
                                if redr3 == "99":
                                    pass
                                else:
                                    print(f"Invalid Selection {redr3}")
                            elif payt3 == "2":
                                momo3 = input(
                                    "Dear Vaia Joseph, you are buying MTN 12.5GB monthly Plan data bundle for N3000 valid till 01/04/2026 for 2349164900946 \n"
                                    "Please enter your MoMo Pin to confirm:")
                                if momo3 == "00000000":
                                    pass
                                else:
                                    print("Invalid pin")
                            else:
                                print(f"Invalid Selection {payt3}")
                        elif fbook1 == "3":
                            tel = input("Enter recipient's number:")
                            if len(tel) == 11 and tel.isnumeric() and (
                                    tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                                0:3] == "090" or tel[
                                        0:3] == "091"):
                                tel2 = input("Confirm recipient's number:")
                                if len(tel2) == 11 and tel2.isnumeric() and (
                                        tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                    0:3] == "090" or tel2[
                                            0:3] == "091"):
                                    pass
                                else:
                                    print(f"{tel2} is not a valid number")
                    elif fbook == "2":
                        fbook2= input("You will pay N50 for 40MB Facebook Weekly Plan. To Proceed, Select: \n"
                                      "1. Auto-Renew \n"
                                      "2. One-Off Purchase \n"
                                      "3. Buy for a Friend \n"
                                      "Select:"
                        )
                        if fbook2 == "1":
                            print(
                                "Activation of 12.5GB monthly plan at N5,500 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                        elif fbook2 == "2":
                            payt3 = input("kindly Select payment type \n"
                                          "1. Airtime \n"
                                          "2. MoMo PSB Wallet \n"
                                          "Select:"
                                          )
                            if payt3 == "1":
                                redr3 = input(
                                    "Activation of 12.5GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                    "99. Next \n"
                                    "Select:")
                                if redr3 == "99":
                                    pass
                                else:
                                    print(f"Invalid Selection {redr3}")
                            elif payt3 == "2":
                                momo3 = input(
                                    "Dear Vaia Joseph, you are buying MTN 12.5GB monthly Plan data bundle for N3000 valid till 01/04/2026 for 2349164900946 \n"
                                    "Please enter your MoMo Pin to confirm:")
                                if momo3 == "00000000":
                                    pass
                                else:
                                    print("Invalid pin")
                            else:
                                print(f"Invalid Selection {payt3}")
                        elif fbook2 == "3":
                            tel = input("Enter recipient's number:")
                            if len(tel) == 11 and tel.isnumeric() and (
                                    tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                                0:3] == "090" or tel[
                                        0:3] == "091"):
                                tel2 = input("Confirm recipient's number:")
                                if len(tel2) == 11 and tel2.isnumeric() and (
                                        tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                    0:3] == "090" or tel2[
                                            0:3] == "091"):
                                    pass
                                else:
                                    print(f"{tel2} is not a valid number")
                        else:
                            print(f"Invalid Selection {fbook2}")
                    elif fbook == "3":
                        fbook3= input("You will pay N150 for 120MB Facebook Monthly Plan. To Proceed, Select: \n"
                                      "1. Auto-Renew \n"
                                      "2. One-Off Purchase \n"
                                      "3. Buy for a Friend \n"
                                      "Select:"
                        )
                        if fbook3 == "1":
                            print(
                                "Activation of 12.5GB monthly plan at N5,500 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                        elif fbook3 == "2":
                            payt3 = input("kindly Select payment type \n"
                                          "1. Airtime \n"
                                          "2. MoMo PSB Wallet \n"
                                          "Select:"
                                          )
                            if payt3 == "1":
                                redr3 = input(
                                    "Activation of 12.5GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                    "99. Next \n"
                                    "Select:")
                                if redr3 == "99":
                                    pass
                                else:
                                    print(f"Invalid Selection {redr3}")
                            elif payt3 == "2":
                                momo3 = input(
                                    "Dear Vaia Joseph, you are buying MTN 12.5GB monthly Plan data bundle for N3000 valid till 01/04/2026 for 2349164900946 \n"
                                    "Please enter your MoMo Pin to confirm:")
                                if momo3 == "00000000":
                                    pass
                                else:
                                    print("Invalid pin")
                            else:
                                print(f"Invalid Selection {payt3}")
                        elif fbook3 == "3":
                            tel = input("Enter recipient's number:")
                            if len(tel) == 11 and tel.isnumeric() and (
                                    tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                                0:3] == "090" or tel[
                                        0:3] == "091"):
                                tel2 = input("Confirm recipient's number:")
                                if len(tel2) == 11 and tel2.isnumeric() and (
                                        tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                    0:3] == "090" or tel2[
                                            0:3] == "091"):
                                    pass
                                else:
                                    print(f"{tel2} is not a valid number")
                        else:
                            print(f"Invalid Selection {fbook3}")
                    else:
                        print(f"Invalid Selection {fbook}")
                elif social == "3":
                    print("Service is temporarily unavailable.")
                elif social == "4":
                    ttok= input("TikTok \n"
                                "1. N50 for 150MB/1 day \n"
                                "2. N400 for 2GB/7 days \n"
                                "Select:"
                                )
                    if ttok == "1":
                        ttok1= input("You will pay N50 for 150MB TikTok Daily Plan. To Proceed, Select: \n"
                                      "1. Auto-Renew \n"
                                      "2. One-Off Purchase \n"
                                      "3. Buy for a Friend \n"
                                      "Select:"
                        )
                        if ttok1 == "1":
                            print(
                                "Activation of 12.5GB monthly plan at N5,500 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                        elif ttok1 == "2":
                            payt3 = input("kindly Select payment type \n"
                                          "1. Airtime \n"
                                          "2. MoMo PSB Wallet \n"
                                          "Select:"
                                          )
                            if payt3 == "1":
                                redr3 = input(
                                    "Activation of 12.5GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                    "99. Next \n"
                                    "Select:")
                                if redr3 == "99":
                                    pass
                                else:
                                    print(f"Invalid Selection {redr3}")
                            elif payt3 == "2":
                                momo3 = input(
                                    "Dear Vaia Joseph, you are buying MTN 12.5GB monthly Plan data bundle for N3000 valid till 01/04/2026 for 2349164900946 \n"
                                    "Please enter your MoMo Pin to confirm:")
                                if momo3 == "00000000":
                                    pass
                                else:
                                    print("Invalid pin")
                            else:
                                print(f"Invalid Selection {payt3}")
                        elif ttok1 == "3":
                            tel = input("Enter recipient's number:")
                            if len(tel) == 11 and tel.isnumeric() and (
                                    tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                                0:3] == "090" or tel[
                                        0:3] == "091"):
                                tel2 = input("Confirm recipient's number:")
                                if len(tel2) == 11 and tel2.isnumeric() and (
                                        tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                    0:3] == "090" or tel2[
                                            0:3] == "091"):
                                    pass
                                else:
                                    print(f"{tel2} is not a valid number")
                        else:
                            print(f"Invalid Selection {ttok1}")
                    elif ttok == "2":
                        ttok2= input("You will pay N400 for 2GB TikTok Weekly Plan. To Proceed, Select: \n"
                                      "1. Auto-Renew \n"
                                      "2. One-Off Purchase \n"
                                      "3. Buy for a Friend \n"
                                      "Select:"
                        )
                        if ttok2 == "1":
                            print(
                                "Activation of 12.5GB monthly plan at N5,500 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                        elif ttok2 == "2":
                            payt3 = input("kindly Select payment type \n"
                                          "1. Airtime \n"
                                          "2. MoMo PSB Wallet \n"
                                          "Select:"
                                          )
                            if payt3 == "1":
                                redr3 = input(
                                    "Activation of 12.5GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                    "99. Next \n"
                                    "Select:")
                                if redr3 == "99":
                                    pass
                                else:
                                    print(f"Invalid Selection {redr3}")
                            elif payt3 == "2":
                                momo3 = input(
                                    "Dear Vaia Joseph, you are buying MTN 12.5GB monthly Plan data bundle for N3000 valid till 01/04/2026 for 2349164900946 \n"
                                    "Please enter your MoMo Pin to confirm:")
                                if momo3 == "00000000":
                                    pass
                                else:
                                    print("Invalid pin")
                            else:
                                print(f"Invalid Selection {payt3}")
                        elif ttok2 == "3":
                            tel = input("Enter recipient's number:")
                            if len(tel) == 11 and tel.isnumeric() and (
                                    tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                                0:3] == "090" or tel[
                                        0:3] == "091"):
                                tel2 = input("Confirm recipient's number:")
                                if len(tel2) == 11 and tel2.isnumeric() and (
                                        tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                    0:3] == "090" or tel2[
                                            0:3] == "091"):
                                    pass
                                else:
                                    print(f"{tel2} is not a valid number")
                        else:
                            print(f"Invalid Selection {ttok2}")
                    else:
                        print(f"Invalid Selection {ttok}")
                elif social == "5":
                    ayb= input("1. N50 for 40MB/7 days \n"
                               "Select:")
                    if ayb == "1":
                        ayb1= input("You will pay N50 for 40MB Ayoba Weekly Plan. To Proceed, Select: \n"
                                      "1. Auto-Renew \n"
                                      "2. One-Off Purchase \n"
                                      "3. Buy for a Friend \n"
                                      "Select:"
                        )
                        if ayb1 == "1":
                            print(
                                "Activation of 12.5GB monthly plan at N5,500 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                        elif ayb1 == "2":
                            payt3 = input("kindly Select payment type \n"
                                          "1. Airtime \n"
                                          "2. MoMo PSB Wallet \n"
                                          "Select:"
                                          )
                            if payt3 == "1":
                                redr3 = input(
                                    "Activation of 12.5GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                    "99. Next \n"
                                    "Select:")
                                if redr3 == "99":
                                    pass
                                else:
                                    print(f"Invalid Selection {redr3}")
                            elif payt3 == "2":
                                momo3 = input(
                                    "Dear Vaia Joseph, you are buying MTN 12.5GB monthly Plan data bundle for N3000 valid till 01/04/2026 for 2349164900946 \n"
                                    "Please enter your MoMo Pin to confirm:")
                                if momo3 == "00000000":
                                    pass
                                else:
                                    print("Invalid pin")
                            else:
                                print(f"Invalid Selection {payt3}")
                        elif ayb1 == "3":
                            tel = input("Enter recipient's number:")
                            if len(tel) == 11 and tel.isnumeric() and (
                                    tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                                0:3] == "090" or tel[
                                        0:3] == "091"):
                                tel2 = input("Confirm recipient's number:")
                                if len(tel2) == 11 and tel2.isnumeric() and (
                                        tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                    0:3] == "090" or tel2[
                                            0:3] == "091"):
                                    pass
                                else:
                                    print(f"{tel2} is not a valid number")
                        else:
                            print(f"Invalid Selection {ayb1}")
                    else:
                        print(f"Invalid Selection {ayb}")
                elif social == "6":
                    alls= input("For use on all social apps \n"
                                "1. Daily @N100 for 200MB \n"
                                "2. Weekly @ N200 for 470MB \n"
                                "3. Monthly @ N450 for 1.2GB \n"
                                "Select:")
                    if alls == "1":
                        alls1= input("You will pay N100 for 200MB All Socials Daily Plan. To Proceed, Select: \n"
                                      "1. Auto-Renew \n"
                                      "2. One-Off Purchase \n"
                                      "3. Buy for a Friend \n"
                                      "Select:"
                        )
                        if alls1 == "1":
                            print(
                                "Activation of 12.5GB monthly plan at N5,500 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                        elif alls1 == "2":
                            payt3 = input("kindly Select payment type \n"
                                          "1. Airtime \n"
                                          "2. MoMo PSB Wallet \n"
                                          "Select:"
                                          )
                            if payt3 == "1":
                                redr3 = input(
                                    "Activation of 12.5GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                    "99. Next \n"
                                    "Select:")
                                if redr3 == "99":
                                    pass
                                else:
                                    print(f"Invalid Selection {redr3}")
                            elif payt3 == "2":
                                momo3 = input(
                                    "Dear Vaia Joseph, you are buying MTN 12.5GB monthly Plan data bundle for N3000 valid till 01/04/2026 for 2349164900946 \n"
                                    "Please enter your MoMo Pin to confirm:")
                                if momo3 == "00000000":
                                    pass
                                else:
                                    print("Invalid pin")
                            else:
                                print(f"Invalid Selection {payt3}")
                        elif alls1 == "3":
                            tel = input("Enter recipient's number:")
                            if len(tel) == 11 and tel.isnumeric() and (
                                    tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                                0:3] == "090" or tel[
                                        0:3] == "091"):
                                tel2 = input("Confirm recipient's number:")
                                if len(tel2) == 11 and tel2.isnumeric() and (
                                        tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                    0:3] == "090" or tel2[
                                            0:3] == "091"):
                                    pass
                                else:
                                    print(f"{tel2} is not a valid number")
                        else:
                            print(f"Invalid Selection {alls1}")
                    elif alls == "2":
                        alls2= input("You will pay N200 for 470MB All Socials Weekly Plan. To Proceed, Select: \n"
                                      "1. Auto-Renew \n"
                                      "2. One-Off Purchase \n"
                                      "3. Buy for a Friend \n"
                                      "Select:"
                        )
                        if alls2 == "1":
                            print(
                                "Activation of 12.5GB monthly plan at N5,500 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                        elif alls2 == "2":
                            payt3 = input("kindly Select payment type \n"
                                          "1. Airtime \n"
                                          "2. MoMo PSB Wallet \n"
                                          "Select:"
                                          )
                            if payt3 == "1":
                                redr3 = input(
                                    "Activation of 12.5GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                    "99. Next \n"
                                    "Select:")
                                if redr3 == "99":
                                    pass
                                else:
                                    print(f"Invalid Selection {redr3}")
                            elif payt3 == "2":
                                momo3 = input(
                                    "Dear Vaia Joseph, you are buying MTN 12.5GB monthly Plan data bundle for N3000 valid till 01/04/2026 for 2349164900946 \n"
                                    "Please enter your MoMo Pin to confirm:")
                                if momo3 == "00000000":
                                    pass
                                else:
                                    print("Invalid pin")
                            else:
                                print(f"Invalid Selection {payt3}")
                        elif alls2 == "3":
                            tel = input("Enter recipient's number:")
                            if len(tel) == 11 and tel.isnumeric() and (
                                    tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                                0:3] == "090" or tel[
                                        0:3] == "091"):
                                tel2 = input("Confirm recipient's number:")
                                if len(tel2) == 11 and tel2.isnumeric() and (
                                        tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                    0:3] == "090" or tel2[
                                            0:3] == "091"):
                                    pass
                                else:
                                    print(f"{tel2} is not a valid number")
                        else:
                            print(f"Invalid Selection {alls2}")
                    elif alls == "3":
                        alls3= input("You will pay N450 for 1.2GB All Socials Monthly Plan. To Proceed, Select: \n"
                                      "1. Auto-Renew \n"
                                      "2. One-Off Purchase \n"
                                      "3. Buy for a Friend \n"
                                      "Select:"
                        )
                        if alls3 == "1":
                            print(
                                "Activation of 12.5GB monthly plan at N5,500 was successful and renews on 01/04/2026. You will receive an SMS shortly with more details")
                        elif alls3 == "2":
                            payt3 = input("kindly Select payment type \n"
                                          "1. Airtime \n"
                                          "2. MoMo PSB Wallet \n"
                                          "Select:"
                                          )
                            if payt3 == "1":
                                redr3 = input(
                                    "Activation of 12.5GB failed due to insufficient balance. Click https://go.mtn.ng/app/RechargeMainScreen to recharge, dial *671# to buy \n"
                                    "99. Next \n"
                                    "Select:")
                                if redr3 == "99":
                                    pass
                                else:
                                    print(f"Invalid Selection {redr3}")
                            elif payt3 == "2":
                                momo3 = input(
                                    "Dear Vaia Joseph, you are buying MTN 12.5GB monthly Plan data bundle for N3000 valid till 01/04/2026 for 2349164900946 \n"
                                    "Please enter your MoMo Pin to confirm:")
                                if momo3 == "00000000":
                                    pass
                                else:
                                    print("Invalid pin")
                            else:
                                print(f"Invalid Selection {payt3}")
                        elif alls3 == "3":
                            tel = input("Enter recipient's number:")
                            if len(tel) == 11 and tel.isnumeric() and (
                                    tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                                0:3] == "090" or tel[
                                        0:3] == "091"):
                                tel2 = input("Confirm recipient's number:")
                                if len(tel2) == 11 and tel2.isnumeric() and (
                                        tel2[0:3] == "070" or tel2[0:3] == "080" or tel2[0:3] == "081" or tel2[
                                    0:3] == "090" or tel2[
                                            0:3] == "091"):
                                    pass
                                else:
                                    print(f"{tel2} is not a valid number")
                        else:
                            print(f"Invalid Selection {alls3}")
                    else:
                        print(f"Invalid Selection {alls}")
                else:
                    print(f"Invalid Selection {social}")
            elif plans == "7":
                brba= input("1. Link Device \n"
                            "2. Recharge Device \n"
                            "3. Check Device Balance \n"
                            "4. View & Unlink Device \n"
                            "5. Buy Data Bundle On Device \n"
                            "6. Link NIN to Device \n"
                            "Select:"
                            )
                if brba == "1":
                    link= input("1. Link Device \n"
                                "Select:"
                                )
                    if link == "1":
                        link1= input("Enter Device Number (e.g 080xxxxxxxxx \n"
                                     "Enter:"
                                     )
                    else:
                        print(f"Invalid Selection {link}")
                elif brba == "2":
                    print("No Mifi Consumer attached")
                elif brba == "3":
                    chkbl= input("1. Airtime Balance \n"
                                 "2. Data Balance \n"
                                 "3. Broadband Balance \n"
                                 "4. Broadband points Balance \n"
                                 "Select:"
                                 )
                    if chkbl == "1":
                        print("No Mifi Consumer attached")
                    elif chkbl == "2":
                        print("No Mifi Consumer attached")
                    elif chkbl == "3":
                        print("No Mifi Consumer attached")
                    elif chkbl == "4":
                        print("No Mifi Consumer attached")
                    else:
                        print(f"Invalid Selection {chkbl}")
                elif brba == "4":
                    vnul= input("1. Unlink Device \n"
                                "2. View Device \n"
                                "Select"
                                )
                    if vnul == "1":
                        print("No Mifi Consumer attached")
                    elif vnul == "2":
                        print("No Mifi Consumer attached")
                    else:
                        print(f"Invalid Selection {vnul}")
                elif brba == "5":
                    buyd= input("1. Daily Bundle \n"
                                "2. Weekly Bundle \n"
                                "3. Monthly Bundle \n"
                                "4. 2-3Month Plans \n"
                                "5. MIFI Bundles \n"
                                "6. Router(Broadband) Bundles \n"
                                "Select:"
                                )
                    if buyd == "1":
                        print("No Mifi Consumer attached")
                    elif buyd == "2":
                        print("No Mifi Consumer attached")
                    elif buyd == "3":
                        print("No Mifi Consumer attached")
                    elif buyd == "4":
                        print("No Mifi Consumer attached")
                    elif buyd == "5":
                        print("No Mifi Consumer attached")
                    elif buyd == "6":
                        print("No Mifi Consumer attached")
                    else:
                        print(f"Invalid Selection {buyd}")
                elif brba == "6":
                    nin= input("1. Proceed \n"
                               "Select:"
                               )
                    if nin == "1":
                        print("Link your NIN to your Broadband device SIM to avoid being barred. Click: \n"
                              "https://apps.mtn.ng/newsletter/c/link-your-nin or visit any MTN store today.")
                    else:
                        print(f"Invalid Selection {nin}")
                else:
                    print(f"Invalid Selection {brba}")
            elif plans == "8":
                binge= input("1. N500 for 1GB \n"
                              "2. N600 for 1.5GB \n"
                              "3. N900 for 2.5GB \n"
                              "4. N1,000 for 3.2GB \n"
                              "5. N2,500 for 6GB \n"
                              "6. N3,500 for 11GB \n"
                             "Select:"
                              )
                if binge == "1":
                    big1= input("Get 1.5GB+1.5mins Daily plan for N500. \n"
                                "To proceed, select: \n"
                                "1. Auto-Renew \n"
                                "2. One-Off \n"
                                "3. Buy for a Friend \n"
                                "4. Redeem Promo Code \n"
                                "Select:"
                    )
                    if big1 == "1":
                        bigpay= input("kindly select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                        )
                    elif big1 == "2":
                        bigpay2= input("kindly select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                        )
                    elif big1 == "3":
                        bigpay3= input("Enter recipient's number:"
                        )
                    elif big1 == "4":
                        coupon= input("Input your coupon code:")
                    else:
                        print(f"Invalid Selection {big1}")
                elif binge == "2":
                    big2= input("Get 1.5GB+100MB YT Music for N600. \n"
                                "To proceed, select: \n"
                                "1. Auto-Renew \n"
                                "2. One-Off \n"
                                "3. Buy for a Friend \n"
                                "4. Redeem Promo Code \n"
                                "Select:"
                                )
                    if big2 == "1":
                        big2pay= input("kindly select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                    elif big2 == "2":
                        big2pay2= input("kindly select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                    elif big2 == "3":
                        big2pay3= input("Enter recipient's number:"
                              )
                    elif big2 == "4":
                        big2pay4= input("Input your coupon code:")
                    else:
                        print(f"Invalid Selection {big2}")
                elif binge == "3":
                    big3= input("You will pay N900 for 2.5GB 2-Day Plan. \n"
                                "To proceed, select: \n"
                                "1. Auto-Renew \n"
                                "2. One-Off \n"
                                "3. Buy for a Friend \n"
                                "4. Redeem Promo Code \n"
                                "Select:"
                                )
                    if big3 == "1":
                        big3pay= input("kindly select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                    elif big3 == "2":
                        big3pay2= input("kindly select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                    elif big3 == "3":
                        big3pay3= input("Enter recipient's number:")
                    elif big3 == "4":
                        big3pay4= input("Input your coupon code:")
                    else:
                        print("UNKNOWN APPLICATION")
                elif binge == "4":
                    big4= input("You will pay N1000 for 3.2GB 2-Day Plan. \n"
                                "To proceed, select: \n"
                                "1. Auto-Renew \n"
                                "2. One-Off \n"
                                "3. Buy for a Friend \n"
                                "4. Redeem Promo Code \n"
                                "Select:"
                                )
                    if big4 == "1":
                        big4pay= input("kindly select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                    elif big4 == "2":
                        big4pay2= input("kindly select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                    elif big4 == "3":
                        big4pay3= input("Enter recipient's number:")
                    elif big4 == "4":
                        big4pay4= input("Input your coupon code:")
                    else:
                        print("UNKNOWN APPLICATION")
                elif binge == "5":
                    big5= input("Get 6GB Weekly Plan for N2,500. \n"
                                "To proceed, select: \n"
                                "1. Auto-Renew \n"
                                "2. One-Off \n"
                                "3. Buy for a Friend \n"
                                "4. Redeem Promo Code \n"
                                "Select:"
                                )
                    if big5 == "1":
                        big5pay= input("kindly select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                    elif big5 == "2":
                        big5pay2= input("kindly select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                    elif big5 == "3":
                        big5pay3= input("Enter recipient's number:")
                    elif big5 == "4":
                        big5pay4= input("Input your coupon code")
                    else:
                        print(f"Invalid Selection {big5}")
                elif binge == "6":
                    big6= input("Get 11GB Weekly Plan for N3,500. \n"
                                "To proceed, select: \n"
                                "1. Auto-Renew \n"
                                "2. One-Off \n"
                                "3. Buy for a Friend \n"
                                "4. Redeem Promo Code \n"
                                "Select:"
                                )
                    if big6 == "1":
                        big6pay= input("kindly select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                    elif big6 == "2":
                        big6pay2= input("kindly select payment type \n"
                                      "1. Airtime \n"
                                      "2. MoMo PSB Wallet \n"
                                      "Select:"
                                      )
                    elif big6 == "3":
                        big6pay3= input("Enter recipient's number:")
                    elif big6 == "4":
                        big6pay4= input("Input your coupon code:")
                    else:
                        print("UNKNOWN APPLICATION")
                else:
                    print(f"Invalid Selection {binge}")
            elif plans == "9":
                fmly= input("1. Add New Beneficiary/Sponsor \n"
                            "2. Manage Beneficiary/Sponsor \n"
                            "3. Balance Enquiry \n"
                            "4. Deactivate Sevice \n"
                            "5. Help \n"
                            "Select:"
                            )
                if fmly == "1":
                    add= input("1. Add new Beneficiary \n"
                               "2. Allocate Family Pack \n"
                               "3. Reset Family Pack \n"
                               "Select:"
                               )
                    if add == "1":
                        add1= input("To add beneficiary to your family pack service, \n"
                                    "Enter phone number:"
                                    )
                    elif add == "2":
                        print("No Consumer on the entered MSISDN")
                    elif add == "3":
                        reset= input("1. Reset all beneficiaries \n"
                                     "2. Reset beneficiary \n"
                                     "Select:"
                                     )
                    else:
                        print(f"Invalid Selection {add}")
                elif fmly == "2":
                    del1= input("1. View Beneficiary \n"
                                "2. View Sponsor \n"
                                "3. Delete all beneficiaries \n"
                                "4. Delete Beneficiary \n"
                                "5. Delete Sponsor \n"
                                "6. Ask for data \n"
                                "Select:"
                                )
                    if del1 == "1":
                        print("No Consumer on the entered MSISDN")
                    elif del1 == "2":
                        print("Sorry, you do not have a Family Pack sponsor. Thank You")
                    elif del1 == "3":
                        conf= input("Do you want to delete all your beneficiaries from yout family pack service \n"
                                    "1. Yes \n"
                                    "2. Cancel \n"
                                    "3. Select:"
                                    )
                    elif del1 == "4":
                        print("No Consumer on the entered MSISDN")
                    elif del1 == "5":
                        print("NO provider attached on the entered MSISDN")
                    elif del1 == "6":
                        req= input("To Request Data from a friend enter phone number (e.g 08xxxxxxxxx) \n"
                                   ":"
                                   )
                    else:
                        print(f"Invalid Selection {del1}")
                elif fmly == "3":
                    man= input("1. Sponsor Balance Enquiry \n"
                               "2. Beneficiary Balance Enquiry \n"
                               "Select:"
                               )
                    if man == "1":
                        sprbal= input("1. Sponsor Balance Enquiry \n"
                                      "Enter:"
                                      )
                    elif man == "2":
                        benbal= input("1. Beneficiary Balance Enquiry \n"
                                      "Enter:"
                                      )
                    else:
                        print(f"Invalid Selection {man}")
                elif fmly == "4":
                    deact= input("Are you sure you want to deactivate family pack (All beneficiary will be removed during this process)? \n"
                                 "1. Proceed \n"
                                 "Select:"
                                 )
                    if deact == "1":
                        deact1= input("Your Family pack has been deactivated successfully and all beneficiary has been removed. Your family pack is still available for \n"
                                      "99. Next \n"
                                      "Select:"
                                      )
                        if deact1 == "99":
                            deact2= input("your use. Dial *323# to check your balance. Thank you. \n"
                                          "88. Exit \n"
                                          "Select:"
                                          )
                            if deact2 == "88":
                                print("Exited Successfully!")
                            else:
                                print(f"Invalid Selection {deact2}")
                        else:
                            print(f"Invalid Selection {deact1}")
                    else:
                        print(f"Invalid Selection {deact}")
                elif fmly == "5":
                    print("Service is temporarily unavailable")
                else:
                    print(f"Invalid Selection {fmly}")
            elif plans == "10":
                hdeals= input("New Xtravalue Plans"
                              "1. N500 - 600MB+2mins+2 SMS. Valid 7days \n"
                              "2. N1,500 - 1.8GB+6mins+5 SMS. Valid 30days \n"
                              "3. N3000 - 5.5GB+8mins+7 SMS. Valid 30days \n"
                              "Select:"
                              )
                if hdeals == "1":
                    hd1= input("Buy XtraData 500 @N500 & get 600MB+2mins+2 SMS valid for 7 days. \n"
                               "You will be migrated to XtraValue. To proceed, select: \n"
                               "1. Auto-Renew \n"
                               "2. One-off \n"
                               "Select:"
                               )
                    if hd1 == "1":
                        print("Y'ellow! Activation of XtraData 500 failed due to insufficient balance. Dial *904# to recharge from your bank account")
                    elif hd1 == "2":
                        print(
                            "Y'ellow! Activation of XtraData 500 failed due to insufficient balance. Dial *904# to recharge from your bank account")
                    else:
                        print(f"Invalid Selection {hd1}")
                elif hdeals == "2":
                    hd2= input("Buy XtraData 1500 @N1500 & get 1.8GB+6mins+5 SMS valid for 30 days. \n"
                               "You will be migrated to XtraValue. To proceed, select: \n"
                               "1. Auto-Renew \n"
                               "2. One-off \n"
                               "Select:"
                               )
                    if hd2 == "1":
                        print(
                            "Y'ellow! Activation of XtraData 1500 failed due to insufficient balance. Dial *904# to recharge from your bank account")
                    elif hd2 == "2":
                        print(
                            "Y'ellow! Activation of XtraData 1500 failed due to insufficient balance. Dial *904# to recharge from your bank account")
                    else:
                        print(f"Invalid Selection {hd2}")
                elif hdeals == "3":
                    hd3= input("Buy XtraData 3000 @N3000 & get 5.5GB+8mins+7 SMS valid for 30 days. \n"
                               "You will be migrated to XtraValue. To proceed, select: \n"
                               "1. Auto-Renew \n"
                               "2. One-off \n"
                               "Select:"
                               )
                    if hd3 == "1":
                        print(
                            "Y'ellow! Activation of XtraData 3000 failed due to insufficient balance. Dial *904# to recharge from your bank account")
                    elif hd3 == "2":
                        print(
                            "Y'ellow! Activation of XtraData 3000 failed due to insufficient balance. Dial *904# to recharge from your bank account")
                    else:
                        print(f"Invalid Selection {hd3}")
                else:
                    print(f"Invalid Selection {hdeals}")
            elif plans == "99":
                rmd= input("11. Always ON \n"
                           "12. Manage data \n"
                           "13. YouTube \n"
                           "14. Apple Music Flexa"
                           )
                if rmd == "11":
                    ayon= input("Always On Bundle \n"
                                "1. N5,500 for 18GB/30 Days \n"
                                "2. N9,000 for 45GB/30 Days \n"
                                "Select:"
                                )
                    if ayon == "1":
                        alwson= input("Get 18.6GB Monthly Always On Plan for N5,500. To proceed, select: \n"
                                      "1. Auto-Renew \n"
                                      "2. One-Off \n "
                                      "3. Buy for a Friend \n"
                                      "Select:"
                                      )
                        if alwson == "1":
                            print("Activation of 18.6GB Monthly Always On Plan failed due to Insufficient Balance. \n"
                                  "Please recharge or dial *303# to borrow airtime and try again. Thank you.")
                        elif alwson == "2":
                            print("Activation of 18.6GB Monthly Always On Plan failed due to Insufficient Balance. \n"
                                  "Please recharge or dial *303# to borrow airtime and try again. Thank you.")
                        elif alwson == "3":
                            pass
                        else:
                            print(f"Invalid Selection {alwson}")
                    elif ayon == "2":
                        alson= input("Get 45GB Monthly Always On Plan for N9,000. To proceed, select: \n"
                                      "1. Auto-Renew \n"
                                      "2. One-Off \n "
                                      "3. Buy for a Friend \n"
                                      "Select:")
                        if alson == "1":
                            print("Activation of 45GB Monthly Always On Plan failed due to Insufficient Balance. \n"
                                  "Please recharge or dial *303# to borrow airtime and try again. Thank you.")
                        elif alson == "2":
                            print("Activation of 45GB Monthly Always On Plan failed due to Insufficient Balance. \n"
                                  "Please recharge or dial *303# to borrow airtime and try again. Thank you.")
                        elif alson == "3":
                            pass
                        else:
                            print(f"Invalid Selection {alson}")
                    else:
                        print(f"Invalid Selection {ayon}")
                elif rmd == "12":
                    mang= input("Manage your Data Bundle \n"
                                "1. View Active Data Bundle \n"
                                "2. Opt in for Auto-Renewal \n"
                                "3. Cancel Auto-Renewal \n"
                                "4. Deal Zone Offers \n"
                                "Select:"
                                )
                    if mang == "1":
                        print("Service is temporarily Unavailable")
                    elif mang == "2":
                        print("Service is temporarily unavailable")
                    elif mang == "3":
                        print("Service is temporarily unavailable")
                    elif mang == "4":
                        print("Service is temporarily unavailable")
                elif rmd == "13":
                    yout= input("Buy and get data to stream YouTube at Night (12am to 5am) \n"
                                "1. Weekly Plan \n"
                                "2. Monthly Plan \n"
                                "Select:"
                                )
                    if yout == "1":
                        youweek= input("Weekly Plan \n"
                                       "1. N800 for 1GB \n"
                                       "2. N1,000 for 1.5GB \n"
                                       "3. N500 for 500MB \n"
                                       "Select:"
                                       )
                    elif yout == "2":
                        youmth= input("Monthly Plan \n"
                                      "1. N1,500 for 2GB \n"
                                      "2. N2,500 for 3.5GB \n"
                                      "3. N3,500 for 7GB \n"
                                      "4. N4,500 for 10GB \n"
                                      "5. N5,500 for 12.5GB \n"
                                      "99. Next"
                                      "Select:"
                                      )
                    else:
                        print(f"Invalid Selection {yout}")
                elif rmd == "14":
                    print("Service not available. Please try again later")
                else:
                    print(f"Invalid Selection {rmd}")
            else:
                print(f"Invalid Selectin {plans}")
        elif data == "2":
            deal1= input("Special Offer for you! Get 4.5GB for N1000. Data is valid for 1day."
                         "1. Activate \n"
                         "Select:"
            )
            if deal1 == "1":
                resp= input("Activation of 4.5GB Smart Daily Bundle @N1000 failed due to insufficient balance. Click https.//go.mtn.ng/app/RechargeMainScreen to recharge, dial \n"
                            "00. Next \n"
                            "Select: "
                )
                if resp == "00":
                    print("*671# to buy airtime from MoMo wallet, *904# to recharge from your bank account or *303# to borrow airtime and pay later.")
                else:
                    print(f"Invalid selection {resp}")
            else:
                print(f"Invalid Selection {deal1}")
        elif data == "3":
            deal2= input("Special Offer for you! Get 20GB for N4500. Data is valid for 7days."
                         "1. Activate \n"
                         "Select:"
            )
            if deal2 == "1":
                resp2= input("Activation of 20GB Smart Daily Bundle @N4500 failed due to insufficient balance. Click https.//go.mtn.ng/app/RechargeMainScreen to recharge, dial \n"
                            "00. Next \n"
                            "Select:")
                if resp2 == "00":
                    print("*671# to buy airtime from MoMo wallet, *904# to recharge from your bank account or *303# to borrow airtime and pay later.")
                else:
                    print(f"Invalid Selection {resp2}")
            else:
                print(f"Invalid Selection {deal2}")
        elif data == "4":
            voff= input("1. GistPlus - 4X \n"
                        "2. Satchet Bundles - 15k/sec \n"
                        "Select:"
            )
            if voff == "1":
                voff1= input("GistPlus. Enjoy extra airtime @75k/s. \n"
                             "Select Amount: \n"
                             "1. N100 = N400 \n"
                             "2. N150 = N600\n"
                             "3. N200 = N800 \n"
                             "4. N400 = N1600 \n"
                             "99. Next \n"
                             "Select:"
                )
                if voff1 == "1":
                    get1= input("Get N400 for N100 from your airtime to call, text and browse in Nigeria, Select: \n"
                               "1. Proceed \n"
                               "2. Cancelled \n"
                               "Select:"
                    )
                    if get1 == "1":
                        print("GistPlus purchase of N100 failed due to insufficient Balance, kindly recharge and dial *889# to try again")
                    elif get1 == "2":
                        print("Transaction has been cancelled successfully!")
                    else:
                        print(f"Invalid Selection {get1}")
                elif voff1 == "2":
                    get2 = input("Get N600 for N150 from your airtime to call, text and browse in Nigeria, Select: \n"
                                 "1. Proceed \n"
                                 "2. Cancelled \n"
                                 "Select:"
                    )
                    if get2 == "1":
                        print(
                            "GistPlus purchase of N150 failed due to insufficient Balance, kindly recharge and dial *889# to try again")
                    elif get2 == "2":
                        print("Transaction has been cancelled successfully!")
                    else:
                        print(f"Invalid Selection {get2}")
                elif voff1 == "3":
                    get3 = input("Get N800 for N200 from your airtime to call, text and browse in Nigeria, Select: \n"
                                 "1. Proceed \n"
                                 "2. Cancelled \n"
                                 "Select:"
                                 )
                    if get3 == "1":
                        print(
                            "GistPlus purchase of N200 failed due to insufficient Balance, kindly recharge and dial *889# to try again")
                    elif get3 == "2":
                        print("Transaction has been cancelled successfully!")
                    else:
                        print(f"Invalid Selection {get3}")
                elif voff1 == "4":
                    get4 = input("Get N1600 for N400 from your airtime to call, text and browse in Nigeria, Select: \n"
                                 "1. Proceed \n"
                                 "2. Cancelled \n"
                                 "Select:"
                    )
                    if get4 == "1":
                        print(
                            "GistPlus purchase of N400 failed due to insufficient Balance, kindly recharge and dial *889# to try again")
                    elif get4 == "2":
                        print("Transaction has been cancelled successfully!")
                    else:
                        print(f"Invalid Selection {get4}")
                elif voff1 == "99":
                    enter= input("Enter Amount \n"
                                 "5. N500 = N2000 \n"
                                 "6. N1,000 = N4,000 \n"
                                 "7. N1,500 = N6,000 \n"
                                 "8. N5,000 = N20,000 \n"
                                 "Select:"
                    )
                    if enter == "5":
                        get5 = input(
                            "Get N2000 for N500 from your airtime to call, text and browse in Nigeria, Select: \n"
                            "1. Proceed \n"
                            "2. Cancelled \n"
                            "Select:"
                        )
                        if get5 == "1":
                            print(
                                "GistPlus purchase of N500 failed due to insufficient Balance, kindly recharge and dial *889# to try again")
                        elif get5 == "2":
                            print("Transaction has been cancelled successfully!")
                        else:
                            print(f"Invalid Selection {get5}")
                    elif enter == "6":
                        get6 = input(
                            "Get N4000 for N1000 from your airtime to call, text and browse in Nigeria, Select: \n"
                            "1. Proceed \n"
                            "2. Cancelled \n"
                            "Select:"
                        )
                        if get6 == "1":
                            print(
                                "GistPlus purchase of N1000 failed due to insufficient Balance, kindly recharge and dial *889# to try again")
                        elif get6 == "2":
                            print("Transaction has been cancelled successfully!")
                        else:
                            print(f"Invalid Selection {get6}")
                    elif enter == "7":
                        get7 = input(
                            "Get N1600 for N400 from your airtime to call, text and browse in Nigeria, Select: \n"
                            "1. Proceed \n"
                            "2. Cancelled \n"
                            "Select:"
                        )
                        if get7 == "1":
                            print(
                                "GistPlus purchase of N400 failed due to insufficient Balance, kindly recharge and dial *889# to try again")
                        elif get7 == "2":
                            print("Transaction has been cancelled successfully!")
                        else:
                            print(f"Invalid Selection {get7}")
                    elif enter == "8":
                        get8 = input(
                            "Get N20,000 for N5,000 from your airtime to call, text and browse in Nigeria, Select: \n"
                            "1. Proceed \n"
                            "2. Cancelled \n"
                            "Select:"
                        )
                        if get8 == "1":
                            print(
                                "GistPlus purchase of N5000 failed due to insufficient Balance, kindly recharge and dial *889# to try again")
                        elif get8 == "2":
                            print("Transaction has been cancelled successfully!")
                        else:
                            print(f"Invalid Selection {get8}")
                    else:
                        print(f"Invalid Selection {enter}")
                else:
                    print(f"Invalid Selection {voff1}")
            elif voff == "2":
                voff2= input("Satchet Bundles. Talk more for less! Enjoy amazing discounted rates! Get: \n"
                             "1. N100 @20k/s \n"
                             "2. N200 @16k/s \n"
                             "3. N500 @15k/s \n"
                             "Select:"
                )
                if voff2 == "1":
                    get9 = input("Get 8.50mins for N100 to call all networks in Nigeria, Select: \n"
                                 "1. Proceed \n"
                                 "2. Cancel \n"
                                 "Select:"
                                 )
                    if get9 == "1":
                        print(
                            "GistPlus purchase of N100 failed due to insufficient Balance, kindly recharge and dial *889# to try again")
                    elif get9 == "2":
                        print("Transaction has been cancelled successfully!")
                    else:
                        print(f"Invalid Selection {get9}")
                elif voff2 == "2":
                    get10 = input("Get 21mins for N200 to call all networks in Nigeria, Select: \n"
                                 "1. Proceed \n"
                                 "2. Cancel \n"
                                 "Select:"
                                 )
                    if get10 == "1":
                        print(
                            "GistPlus purchase of N200 failed due to insufficient Balance, kindly recharge and dial *889# to try again")
                    elif get10 == "2":
                        print("Transaction has been cancelled successfully!")
                    else:
                        print(f"Invalid Selection {get10}")
                elif voff2 == "3":
                    get11 = input("Get 55mins for N500 to call all networks in Nigeria, Select: \n"
                                 "1. Proceed \n"
                                 "2. Cancel \n"
                                 "Select:"
                                 )
                    if get11 == "1":
                        print(
                            "GistPlus purchase of N500 failed due to insufficient Balance, kindly recharge and dial *889# to try again")
                    elif get11 == "2":
                        print("Transaction has been cancelled successfully!")
                    else:
                        print(f"Invalid Selection {get11}")
                else:
                    print(f"Invalid Selection {voff2}")
            else:
                print(f"Invalid Selection {voff}")
        elif data == "5":
            xvle= input("Standard Local Calls @30k/s. Buy Xtravalue bundle for 18k/sec local calls & discounted Int'l rates \n"
                        "1. XtraData \n"
                        "2. XtraTalk \n"
                        "3. Value data \n"
                        "4. XtraData+ \n"
                        "99. Next \n"
                        "Select:"
            )
            if xvle == "1":
                xtrad= input("1. XtraData 500 \n"
                             "2. XtraData 1500 \n"
                             "3. XtraData 3000 \n"
                             "4. XtraData 5500 \n"
                             "5. XtraData 10000 \n"
                             "6. XtraData more 2500 \n"
                             "Select:"
                )
                if xtrad == "1":
                    buyx= input("Buy XtraData500 @ N500 & get 600MB+2mins+2 SMS, valid for 7 days. To proceed, Select:"
                                "1. Auto-Renew \n"
                                "2. One-Off")
                    if buyx == "1":
                        print("Yello! Activation of XtraData failed due to insuffecient balance. Dial *904 to recherge from your bamk account")
                    elif buyx == "2":
                        print(
                            "Yello! Activation of XtraData failed due to insuffecient balance. Dial *904 to recherge from your bamk account")
                    else:
                        print(f"Invalid Selection {buyx}")
                elif xtrad == "2":
                    buyx = input("Buy XtraData1500 @ N1500 & get 1.8GB+6mins+5 SMS, valid for 30 days. To proceed, Select:"
                                 "1. Auto-Renew \n"
                                 "2. One-Off")
                    if buyx == "1":
                        print("Yello! Activation of XtraData failed due to insuffecient balance. Dial *904 to recherge from your bamk account")
                    elif buyx == "2":
                        print(
                            "Yello! Activation of XtraData failed due to insuffecient balance. Dial *904 to recherge from your bamk account")
                    else:
                        print(f"Invalid Selection {buyx}")
                elif xtrad == "3":
                    buyx = input("Buy XtraData3000 @ N3000 & get 5.5GB+8mins+7 SMS, valid for 30 days. To proceed, Select:"
                                 "1. Auto-Renew \n"
                                 "2. One-Off")
                    if buyx == "1":
                        print("Yello! Activation of XtraData failed due to insuffecient balance. Dial *904 to recharge from your bank account")
                    elif buyx == "2":
                        print(
                            "Yello! Activation of XtraData failed due to insuffecient balance. Dial *904 to recherge from your bamk account")
                    else:
                        print(f"Invalid Selection {buyx}")
                elif xtrad == "4":
                    buyx = input("Buy XtraDataMore5500 @ N5500 & get 12.5GB+36mins+15 SMS, valid for 30 days. To proceed, Select:"
                                 "1. Auto-Renew \n"
                                 "2. One-Off")
                    if buyx == "1":
                        print("Yello! Activation of XtraData failed due to insuffecient balance. Dial *904 to recherge from your bamk account")
                    elif buyx == "2":
                        print(
                            "Yello! Activation of XtraData failed due to insuffecient balance. Dial *904 to recherge from your bamk account")
                    else:
                        print(f"Invalid Selection {buyx}")
                elif xtrad == "5":
                    buyx = input("Buy XtraData10000 @ N10000 & get 35GB+43.7mins, valid for 30 days. To proceed, Select:"
                                 "1. Auto-Renew \n"
                                 "2. One-Off")
                    if buyx == "1":
                        print("Yello! Activation of XtraData failed due to insuffecient balance. Dial *904 to recherge from your bamk account")
                    elif buyx == "2":
                        print(
                            "Yello! Activation of XtraData failed due to insuffecient balance. Dial *904 to recherge from your bamk account")
                    else:
                        print(f"Invalid Selection {buyx}")
                elif xtrad == "6":
                    buyx = input("Buy XtraDataMore2500 @ N2500 & get 6GB+17mins+5 SMS, valid for 7 days. To proceed, Select:"
                                 "1. Auto-Renew \n"
                                 "2. One-Off")
                    if buyx == "1":
                        print("Yello! Activation of XtraData failed due to insuffecient balance. Dial *904 to recherge from your bamk account")
                    elif buyx == "2":
                        print(
                            "Yello! Activation of XtraData failed due to insuffecient balance. Dial *904 to recherge from your bamk account")
                    else:
                        print(f"Invalid Selection {buyx}")
                else:
                    print(f"Invalid Selection {xtrad}")
            elif xvle == "2":
                xtrat= input("1. XtraTalk 500 \n"
                             "2. XtraTalk 1500 \n"
                             "3. XtraTalk 3000 \n"
                             "4. XtraTalk 5500 \n"
                             "Select:"
                )
                if xtrat == "1":
                    buyx= input("Buy XtraTalk500 @ N500 & get 37min+250MB+5 SMS, valid for 7 days. To proceed, Select:"
                                "1. Auto-Renew \n"
                                "2. One-Off")
                    if buyx == "1":
                        print("Yello! Activation of XtraTalk failed due to insuffecient balance. Dial *904 to recherge from your bamk account")
                    elif buyx == "2":
                        print(
                            "Yello! Activation of XtraTalk failed due to insuffecient balance. Dial *904 to recherge from your bamk account")
                    else:
                        print(f"Invalid Selection {buyx}")
                elif xtrat == "2":
                    buyx = input("Buy XtraTalk1500 @ N1500 & get 117min+580MB+10 SMS, valid for 30 days. To proceed, Select:"
                                 "1. Auto-Renew \n"
                                 "2. One-Off")
                    if buyx == "1":
                        print(
                            "Yello! Activation of XtraTalk failed due to insuffecient balance. Dial *904 to recherge from your bamk account")
                    elif buyx == "2":
                        print(
                            "Yello! Activation of XtraTalk failed due to insuffecient balance. Dial *904 to recherge from your bamk account")
                    else:
                        print(f"Invalid Selection {buyx}")
                elif xtrat == "3":
                    buyx = input("Buy XtraTalk500 @ N500 & get 250mins+750MB+12 SMS, valid for 30 days. To proceed, Select:"
                                 "1. Auto-Renew \n"
                                 "2. One-Off")
                    if buyx == "1":
                        print(
                            "Yello! Activation of XtraTalk failed due to insuffecient balance. Dial *904 to recherge from your bamk account")
                    elif buyx == "2":
                        print(
                            "Yello! Activation of XtraTalk failed due to insuffecient balance. Dial *904 to recherge from your bamk account")
                    else:
                        print(f"Invalid Selection {buyx}")
                elif xtrat == "4":
                    buyx = input("Buy XtraTalk5500 @ N5500 & get 438min+2GB+20 SMS, valid for 30 days. To proceed, Select:"
                                 "1. Auto-Renew \n"
                                 "2. One-Off")
                    if buyx == "1":
                        print(
                            "Yello! Activation of XtraTalk failed due to insuffecient balance. Dial *904 to recherge from your bamk account")
                    elif buyx == "2":
                        print(
                            "Yello! Activation of XtraTalk failed due to insuffecient balance. Dial *904 to recherge from your bamk account")
                    else:
                        print(f"Invalid Selection {buyx}")
            elif xvle == "3":
                value= input("1. 6.7GB at N3,000 \n"
                             "2. 14.5GB at N5,000 \n"
                             "3. 34GB at M10,000 \n"
                             "Select:"
                )
                if value == "1":
                    buyv= input("Buy ValueData3000 @ N3000 & get 6.75GB, valid for 30 days. To proceed, Select:"
                                 "1. Auto-Renew \n"
                                 "2. One-Off")
                    if buyv == "1":
                        print(
                            "Yello! Activation of ValueData failed due to insuffecient balance. Dial *904 to recherge from your bamk account")
                    elif buyv == "2":
                        print(
                            "Yello! Activation of ValueData failed due to insuffecient balance. Dial *904 to recherge from your bamk account")
                    else:
                        print(f"Invalid Selection {buyv}"
                )
                elif value == "2":
                    buyv = input("Buy ValueData5000 @ N5000 & get 14.5GB, valid for 30 days. To proceed, Select:"
                                 "1. Auto-Renew \n"
                                 "2. One-Off")
                    if buyv == "1":
                        print(
                            "Yello! Activation of ValueData failed due to insuffecient balance. Dial *904 to recherge from your bamk account")
                    elif buyv == "2":
                        print(
                            "Yello! Activation of ValueData failed due to insuffecient balance. Dial *904 to recherge from your bamk account")
                    else:
                        print(f"Invalid Selection {buyv}")
                elif value == "3":
                    buyv = input("Buy ValueData10000 @ N10000 & get 34GB, valid for 30 days. To proceed, Select:"
                                 "1. Auto-Renew \n"
                                 "2. One-Off")
                    if buyv == "1":
                        print(
                            "Yello! Activation of ValueData failed due to insuffecient balance. Dial *904 to recherge from your bamk account")
                    elif buyv == "2":
                        print(
                            "Yello! Activation of ValueData failed due to insuffecient balance. Dial *904 to recherge from your bamk account")
                    else:
                        print(f"Invalid Selection {buyv}")
                else:
                    print("Invalid Selection")
            elif xvle == "4":
                xtrap= input("XtraData+ bundles give you Airtime, Data, Video, Music, Games &Callerfeel \n"
                             "1. XtraData + 300 \n"
                             "2. XtraData + 500 \n"
                             "3. XtraData + 5000 \n"
                             "Select:"
                )
                if xtrap == "1":
                    getn= input("Get N250 Talk, 250MB data, Audiomack, Callefeel & Sony one & Gameworld \n"
                                "1. Auto-Renew \n"
                                "2. One-Off \n"
                                "Select:"
                    )
                    if getn == "1":
                        print(
                            "Yello! Activation of XtraData failed due to insuffecient balance. Dial *904 to recharge from your bank account")
                    elif getn == "2":
                        print(
                            "Yello! Activation of XtraData failed due to insuffecient balance. Dial *904 to recharge from your bank account")
                    else:
                        print("Invalid Selection")
                elif xtrap == "2":
                    getn = input("Get N425 Talk, 600MB data, Audiomack, Callefeel & Sony one & Gameworld \n"
                                 "1. Auto-Renew \n"
                                 "2. One-Off \n"
                                 "Select:"
                                 )
                    if getn == "1":
                        print(
                            "Yello! Activation of XtraData failed due to insuffecient balance. Dial *904 to recharge from your bank account")
                    elif getn == "2":
                        print(
                            "Yello! Activation of XtraData failed due to insuffecient balance. Dial *904 to recharge from your bank account")
                    else:
                        print("Invalid Selection")
                elif xtrap == "3":
                    getn = input("Get N4500 Talk, 13GB data, udux, Callefeel & Sony one & Gameworld \n"
                                 "1. Auto-Renew \n"
                                 "2. One-Off \n"
                                 "Select:"
                                 )
                    if getn == "1":
                        print(
                            "Yello! Activation of XtraData failed due to insuffecient balance. Dial *904 to recharge from your bank account")
                    elif getn == "2":
                        print(
                            "Yello! Activation of XtraData failed due to insuffecient balance. Dial *904 to recharge from your bank account")
                    else:
                        print("Invalid Selection")
            elif xvle == "99":
                eligible= input("5. Eligible Int'l Destinations \n"
                                "Select:"
                )
                if eligible == "5":
                    print("1. United States \n"
                          "2. Canada \n"
                          "3. China \n"
                          "4. India \n"
                          "5. Malaysia."
                    )
                else:
                    print(f"Invalid Selection {eligible}")
            else:
                print(f"Invalid Selection {xvle}")
        elif data == "6":
            rmil= input("1. TravelPass Plan \n"
                        "2. Data Hybrid \n"
                        "3. Free Incoming Roaming Call \n"
                        "4. Int'l Calling Bundle \n"
                        "5. Roaming Balance check \n"
                        "6. Premium Data Roaming \n"
                        "Select:"
            )
            if rmil == "1":
                flight= input("1. Daily \n"
                              "2. Weekly \n"
                              "3. Monthly \n"
                              "4. Inflight Roaming/Eligible Airlines \n"
                              "Select:")
            elif rmil == "2":
                use= input("Use your local data bundle while roaming at no additional cost \n"
                           "1. Eligible Bundles \n"
                           "2. Eligible Destinations \n"
                           "Select:"
                )
            elif rmil == "3":
                checking= input("1. Check Eligibility \n"
                                "2. Eligible Destinations \n"
                                "3. Check free Incoming minutes \n"
                                "Select:"
                )
            elif rmil == "4":
                subscribe= input("1. Subscribe to Int'l calling Bundle \n"
                                 "2. Eligible countries (Bundle applicable to selected networks in destinations listed \n"
                                 "Select:"
                )
            elif rmil == "5":
                print("Dear Customer, you don't have any active data bundle. Please dial *312*1# to buy another data bundle")
            elif rmil == "6":
                activate= input("This allows you to brose in high data cost destinations. To proceed, Select: \n"
                                "1. Activate \n"
                                "2. Deactivate \n"
                                "Select:"
                )
            else:
                print(f"Invalid Selection {rmil}")
        elif data == "7":
            gftd= input("1. Transfer From Data balance \n"
                        "2. Buy for a Friend \n"
                        "3. Request from a Friend \n"
                        "4. View Pending Requests \n"
                        "Select:"
            )
            if gftd == "1":
                fromm = input("1. From Access Data Balance \n"
                              "2. From XtraValue Bundle \n"
                              "Select"
                              )
                if fromm == "1":
                    tel = input("Enter recipient's number:")
                    if len(tel) == 11 and tel.isnumeric() and (
                            tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                        0:3] == "090" or tel[
                                0:3] == "091"):
                        damt = input("Select amount of Data you want to transfer \n"
                                     "Maximum Daily transfer is 5GB \n"
                                     "1. 100MB \n"
                                     "2. 200MB \n"
                                     "3. 500MB \n"
                                     "4. 1GB \n"
                                     "5. 2GB \n"
                                     "6. 3GB \n"
                                     "7. 5GB \n"
                                     "Select:"
                                     )
                        if damt == "1":
                            pls = input(
                                "Please confirm you want to transfer 100MB from your data bundle to 2349164900946\n"
                                "1. Proceed \n"
                                "2. Cancel \n"
                                "Select:"
                                )
                            if pls == "1":
                                print("Y'ello! Transfer of 100MB was successful.")
                            elif pls == "2":
                                print("Y'ello! Transfer of 100MB has been cancelled")
                            else:
                                print(f"Invalid Selection {pls}")
                        elif damt == "2":
                            pls = input(
                                "Please confirm you want to transfer 200MB from your data bundle to 2349164900946\n"
                                "1. Proceed \n"
                                "2. Cancel \n"
                                "Select:"
                            )
                            if pls == "1":
                                print("Y'ello! Transfer of 200MB was successful.")
                            elif pls == "2":
                                print("Y'ello! Transfer of 200MB has been cancelled")
                            else:
                                print(f"Invalid Selection {pls}")
                        elif damt == "3":
                            pls = input(
                                "Please confirm you want to transfer 500MB from your data bundle to 2349164900946\n"
                                "1. Proceed \n"
                                "2. Cancel \n"
                                "Select:"
                            )
                            if pls == "1":
                                print("Y'ello! Transfer of 500MB was successful.")
                            elif pls == "2":
                                print("Y'ello! Transfer of 500MB has been cancelled")
                            else:
                                print(f"Invalid Selection {pls}")
                        elif damt == "4":
                            pls = input(
                                "Please confirm you want to transfer 1GB from your data bundle to 2349164900946\n"
                                "1. Proceed \n"
                                "2. Cancel \n"
                                "Select:"
                            )
                            if pls == "1":
                                print("Y'ello! Transfer of 1GB was successful.")
                            elif pls == "2":
                                print("Y'ello! Transfer of 1GB has been cancelled")
                            else:
                                print(f"Invalid Selection {pls}")
                        elif damt == "5":
                            pls = input(
                                "Please confirm you want to transfer 2GB from your data bundle to 2349164900946\n"
                                "1. Proceed \n"
                                "2. Cancel \n"
                                "Select:"
                            )
                            if pls == "1":
                                print("Y'ello! Transfer of 2GB was successful.")
                            elif pls == "2":
                                print("Y'ello! Transfer of 2GB has been cancelled")
                            else:
                                print(f"Invalid Selection {pls}")
                        elif damt == "6":
                            pls = input(
                                "Please confirm you want to transfer 3GB from your data bundle to 2349164900946\n"
                                "1. Proceed \n"
                                "2. Cancel \n"
                                "Select:"
                            )
                            if pls == "1":
                                print("Y'ello! Transfer of 3GB was successful.")
                            elif pls == "2":
                                print("Y'ello! Transfer of 3GB has been cancelled")
                            else:
                                print(f"Invalid Selection {pls}")
                        elif damt == "7":
                            pls = input(
                                "Please confirm you want to transfer 5GB from your data bundle to 2349164900946\n"
                                "1. Proceed \n"
                                "2. Cancel \n"
                                "Select:"
                            )
                            if pls == "1":
                                print("Y'ello! Transfer of 5GB was successful.")
                            elif pls == "2":
                                print("Y'ello! Transfer of 5GB has been cancelled")
                            else:
                                print(f"Invalid Selection {pls}")
                    else:
                        print("Invalid Phone number")
            elif gftd == "2":
                welcome= input("Welcome to MTN Data Gifting. Select data plan to gift: \n"
                               "1. Data Plans \n"
                               "2. Social Bundle \n"
                               "Select:"
                )
                if welcome == "1":
                    gfplan= input("1. Daily Plans \n"
                                  "2. Weekly Plans \n"
                                  "3. Monthly Plans \n"
                                  "4. 2-Months Plan \n"
                                  "5. 3-Months Plan \n"
                                  "Select:"
                    )
                    if gfplan == "1":
                        day= input("1. N75 for 75MB \n"
                                   "2. N100 for 110MB \n"
                                   "3. N200 for 230MB \n"
                                   "4. N500 for 1GB \n"
                                   "5. N750 for 2GB (2 days)\n"
                                   "6. N1000 for 3.2GB \n"
                                   "7. N600 for 1.5GB \n"
                                   "99. Next \n"
                                   "Select:"
                        )
                        if day == "1":
                            you= input("You will be charged N75 for the gifting of 75MB Daily Data Bundle. \n"
                                       "1. Proceed \n"
                                       "Select:"
                            )
                            if you == "1":
                                print("Activation of 75MB daily Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        elif day == "2":
                            you = input("You will be charged N100 for the gifting of 110MB Daily Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 110MB daily Plan was successful")
                        elif day == "3":
                            you = input("You will be charged N200 for the gifting of 230MB Daily Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 230MB daily Plan was successful")
                        elif day == "4":
                            you = input("You will be charged N500 for the gifting of 1GB Daily Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 1GB daily Plan was successful")
                        elif day == "5":
                            you = input("You will be charged N750 for the gifting of 2GB Daily Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 2GB daily Plan was successful")
                        elif day == "6":
                            you = input("You will be charged N1000 for the gifting of 3.2GB Daily Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 3.2GB daily Plan was successful")
                        elif day == "7":
                            you = input("You will be charged N600 for the gifting of 1.5GB Daily Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 1.5GB daily Plan was successful")
                        elif day == "99":
                            remday= input("8. N350 for 500MB \n"
                                          "9. N1,800 for 7GB \n"
                                          "Select:"
                            )
                            if remday == "8":
                                you = input("You will be charged N350 for the gifting of 500MB Daily Data Bundle. \n"
                                            "1. Proceed \n"
                                            "Select:"
                                            )
                                if you == "1":
                                    print("Activation of 500MB daily Plan was successful")
                            elif remday == "9":
                                you = input("You will be charged N1,800 for the gifting of 7GB Daily Data Bundle. \n"
                                            "1. Proceed \n"
                                            "Select:"
                                            )
                                if you == "1":
                                    print("Activation of 7GB daily Plan was successful")
                            else:
                                print(f"Inalid Selection {remday}")
                        else:
                            print(f"Invalid Selection {day}")
                    elif gfplan == "2":
                        week = input("1. N500 for 500MB \n"
                                     "2. N2,500 for 6GB \n"
                                     "3. N1,000 for 1.5GB \n"
                                     "4. N800 for 1GB \n"
                                     "5. N3,500 for 11GB \n"
                                     "6. N1,500 for 3.5GB \n"
                                     "Select:"
                        )
                        if week == "1":
                            you= input("You will be charged N500 for the gifting of 500MB weekly Data Bundle. \n"
                                       "1. Proceed \n"
                                       "Select:"
                            )
                            if you == "1":
                                print("Activation of 500MB weekly Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        elif week == "2":
                            you = input("You will be charged N2,500 for the gifting of 6GB weekly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 6GB weekly Plan was successful")
                        elif week == "3":
                            you = input("You will be charged N1,000 for the gifting of 1.5GB weekly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 1.5GB weekly Plan was successful")
                        elif week == "4":
                            you = input("You will be charged N800 for the gifting of 1GB weekly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 1GB weekly Plan was successful")
                        elif week == "5":
                            you = input("You will be charged N3,500 for the gifting of 11GB weekly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 11GB weekly Plan was successful")
                        elif week == "6":
                            you = input("You will be charged N1,500 for the gifting of 3.5GB weekly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 3.5GB weekly Plan was successful")
                        else:
                            print(f"Invalid Selection {week}")
                    elif gfplan == "2":
                        months= input("1. N1,500 @ 2GB \n"
                                      "2. N2,000 @ 2.7GB \n"
                                      "3. N2,500 @ 3.5GB \n"
                                      "4. N3,500 @ 7GB \n"
                                      "5. N4,500 @ 10GB \n"
                                      "6. N9,000 @ 25GB \n"
                                      "7. N5,500 @ 12.5GB \n"
                                      "8. N6,500 @ 16.5GB \n"
                                      "99. Next \n"
                                      "Select:"
                        )
                        if months == "1":
                            you= input("You will be charged N1,500 for the gifting of 2GB monthly Data Bundle. \n"
                                       "1. Proceed \n"
                                       "Select:"
                            )
                            if you == "1":
                                print("Activation of 2GB monthly Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        elif months == "2":
                            you = input("You will be charged N2000 for the gifting of 2.7GB monthly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 2.7GB monthly Plan was successful")
                        elif months == "3":
                            you = input("You will be charged N2,500 for the gifting of 3.5GB monthly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 3.5GB monthly Plan was successful")
                        elif months == "4":
                            you = input("You will be charged N3,500 for the gifting of 7GB monthly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 7GB daily Plan was successful")
                        elif months == "5":
                            you = input("You will be charged N4,500 for the gifting of 10GB Monthly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 10GB monthly Plan was successful")
                        elif months == "6":
                            you = input("You will be charged N9000 for the gifting of 25GB monthly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 25GB monthly Plan was successful")
                        elif months == "7":
                            you = input("You will be charged N5,500 for the gifting of 12.5GB monthly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 12.5GB monthly Plan was successful")
                        elif months == "8":
                            you = input("You will be charged N6,500 for the gifting of 16.5GB monthly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 16.5GB monthly Plan was successful")
                        elif months == "99":
                            remday= input("9. N7,000 @ 25GB \n"
                                          "10. N7,500 @ 20GB \n"
                                          "11. N11,000 @ 36GB \n"
                                          "12. N18,000 @ 75GB \n"
                                          "13. N35,000 @ 165GB \n"
                                          "14. N55,000 @ 250GB \n"
                                          "15, N16,000 @ 65GB \n"
                                          "Select:"
                            )
                            if remday == "9":
                                you = input("You will be charged N7000 for the gifting of 25GB monthly Data Bundle. \n"
                                            "1. Proceed \n"
                                            "Select:"
                                            )
                                if you == "1":
                                    print("Activation of 25GB monthly Plan was successful")
                            elif remday == "10":
                                you = input("You will be charged N7,500 for the gifting of 20GB monthly Data Bundle. \n"
                                            "1. Proceed \n"
                                            "Select:"
                                            )
                                if you == "1":
                                    print("Activation of 20GB monthly Plan was successful")
                            elif remday == "11":
                                you = input("You will be charged N3,500 for the gifting of 7GB monthly Data Bundle. \n"
                                            "1. Proceed \n"
                                            "Select:"
                                            )
                                if you == "1":
                                    print("Activation of 20GB monthly Plan was successful")
                            elif remday == "12":
                                you = input("You will be charged N18,000 for the gifting of 75GB Monthly Data Bundle. \n"
                                            "1. Proceed \n"
                                            "Select:"
                                            )
                                if you == "1":
                                    print("Activation of 75GB monthly Plan was successful")
                            elif remday == "13":
                                you = input("You will be charged N35000 for the gifting of 165GB monthly Data Bundle. \n"
                                            "1. Proceed \n"
                                            "Select:"
                                            )
                                if you == "1":
                                    print("Activation of 165GB monthly Plan was successful")
                            elif remday == "14":
                                you = input(
                                    "You will be charged N55,000 for the gifting of 250GB monthly Data Bundle. \n"
                                    "1. Proceed \n"
                                    "Select:"
                                    )
                                if you == "1":
                                    print("Activation of 250GB monthly Plan was successful")
                            elif remday == "15":
                                you = input(
                                    "You will be charged N6,500 for the gifting of 16.5GB monthly Data Bundle. \n"
                                    "1. Proceed \n"
                                    "Select:"
                                    )
                                if you == "1":
                                    print("Activation of 16.5GB monthly Plan was successful")
                            else:
                                print(f"Inalid Selection {remday}")
                        else:
                            print(f"Invalid Selection {months}")
                    elif gfplan == "3":
                        tomonths= input("1. N25,000 @ 90GB \n"
                                        "2. N40,000 @ 150GB \n"
                                        "Select:"
                        )
                        if tomonths == "1":
                            you = input(
                                "You will be charged N25,000 for the gifting of 90GB 2-months Data Bundle. \n"
                                "1. Proceed \n"
                                "Select:"
                            )
                            if you == "1":
                                print("Activation of 90GB 2-months Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        elif tomonths == "2":
                            you = input(
                                "You will be charged N40,000 for the gifting of 150GB 2-months Data Bundle. \n"
                                "1. Proceed \n"
                                "Select:"
                            )
                            if you == "1":
                                print("Activation of 150GB 2-months Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                    elif gfplan == "4":
                        threemonth= input("1. N90,000 @480GB \n"
                                          "Select:"
                        )
                        if threemonth == "1":
                            you = input(
                                "You will be charged N90,000 for the gifting of 480GB 3-months Data Bundle. \n"
                                "1. Proceed \n"
                                "Select:"
                            )
                            if you == "1":
                                print("Activation of 480GB 3-months Plan was successful")
                            else:
                                print(f"Invalid Selectio {you}")
                    else:
                        print(f"Invalid Selection {gfplan}")
                elif welcome == "2":
                    socialb= input("1. WhatsApp \n"
                                   "2. Facebook \n"
                                   "3. TikTok \n"
                                   "4. Ayoba \n"
                                   "5. All Social Bundles \n"
                                   "Select:"
                    )
                    if socialb == "1":
                        app1= input("WhatsApp \n"
                                    "1. Daily @ N25 for 20MB \n"
                                    "2. Weekly @ N50 for 40MB \n"
                                    "3. Monthly @ N150 for 120MB \n"
                                    "Select:"

                        )
                        if app1 == "1":
                            you = input("You will be charged N25 for the gifting of 20MB WhatsApp Daily Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 20MB WhatsApp daily Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        elif app1 == "2":
                            you = input("You will be charged N50 for the gifting of 40MB WhatsApp weekly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 40MB WhatsApp weekly Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        elif app1 == "3":
                            you = input("You will be charged N150 for the gifting of 120MB WhatsApp monthly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 120MB WhatsApp monthly Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        else:
                            print(f"Invalid Selection {app1}")
                    elif socialb == "2":
                        app2= input("Facebook \n"
                                    "1. Daily @ N25 for 20MB \n"
                                    "2. Weekly @ N50 for 40MB \n"
                                    "3. Monthly @ N150 for 120MB \n"
                                    "Select:"

                        )
                        if app2 == "1":
                            you = input("You will be charged N25 for the gifting of 20MB Facebook Daily Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 20MB Facebook daily Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        elif app2 == "2":
                            you = input("You will be charged N50 for the gifting of 40MB Facebook weekly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 40MB Facebook weekly Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        elif app2 == "3":
                            you = input("You will be charged N150 for the gifting of 120MB Facebook monthly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 120MB Facebook monthly Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        else:
                            print(f"Invalid Selection {app2}")
                    elif socialb == "3":
                        app3= input("1. N50 for 150MB \n"
                                    "2. N400 for 2GB/7 days \n"
                                    "Select:"

                        )
                        if app3 == "1":
                            you = input(
                                "You will be charged N50 for the gifting of 150MB TikTok daily Data Bundle. \n"
                                "1. Proceed \n"
                                "Select:"
                                )
                            if you == "1":
                                print("Activation of 150MB TikTok daily Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        elif app3 =="2":
                            you = input(
                                "You will be charged N400 for the gifting of 2GB TikTok weekly Data Bundle. \n"
                                "1. Proceed \n"
                                "Select:"
                            )
                            if you == "1":
                                print("Activation of 2GB TikTok weekly Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        else:
                            print(f"Invalid Selection {app3}")
                    elif socialb == "4":
                        app4= input("Ayoba \n"
                                    "1. N50 for 40MB/7 days \n"
                                    "Select:"

                        )
                        if app4 == "1":
                            you = input(
                                "You will be charged N50 for the gifting of 40MB Ayoba weekly Data Bundle. \n"
                                "1. Proceed \n"
                                "Select:"
                            )
                            if you == "1":
                                print("Activation of 40MB Ayoba weekly Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        else:
                            print(f"Invalid Selection {app4}")
                    elif socialb == "5":
                        all1= input("1. Daily @N100 for 200MB \n"
                                    "2. Weekly @ N200 for 470MB \n"
                                    "3. Monthly @ N450 for 1.2GB \n"
                                    "Select:"
                        )
                        if all1 == "1":
                            you = input("You will be charged N100 for the gifting of 200MB All Socials Daily Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 200MB All Socials daily Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        elif all1 == "2":
                            you = input("You will be charged N200 for the gifting of 470MB All Socials weekly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 470MB All Socials weekly Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        elif all1 == "3":
                            you = input("You will be charged N450 for the gifting of 1.2GB All Socials monthly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 1.2GB All Socials monthly Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        else:
                            print(f"Invalid Selection {all1}")
                    else:
                        print(f"Invalid Selection {socialb}")
                else:
                    print(f"Invalid Selection {welcome}")
            elif gftd == "3":
                toreq= input("To Request Data from a friend enter Phone number (e.g 08xxxxxxxxx) \n"
                             ":"
                )
                if len(toreq) == 11 and toreq.isnumeric() and (
                        toreq[0:3] == "070" or toreq[0:3] == "080" or toreq[0:3] == "081" or toreq[
                    0:3] == "090" or toreq[
                            0:3] == "091"):
                    print("Y'ello! Your Request for data to Phone number 2347037464312 has been delivered.")
                else:
                    print("Invalid Phone Number Entered")
            elif gftd == "4":
                print("You have no pending requests. Thank you!")
            else:
                print(f"Invalid Selection {gftd}")
        elif data == "99":
            rmdr2= input("8. Video Packs \n"
                         "9. Chat with Zigi \n"
                         "10. VAS"
                         "Select:"
            )
            if rmdr2 == "8":
                video= input("Video Streaming Packs \n"
                             "1. Buffet Bundle \n"
                             "2. Shomax Mobile \n"
                             "Select:"
                )
                if video == "1":
                    bundle= input("Subscribe to this bundle to enjoy video streaming or download on YouTube. \n"
                                  "1. 12 Hours Plan \n"
                                  "2. 4 Hours Plan \n"
                                  "Select:"
                    )
                    if bundle == "1":
                        buffet= input("You will pay N600 for YouTube Buffet Plan to Stream YouTube up 12hrs. To proceed, Select: \n"
                                      "1. Auto-Renew \n"
                                      "2. One-Off \n"
                                      "3. Buy for  Friend \n"
                                      "Select:"
                        )
                    elif bundle == "2":
                        buffet2= input("You will pay N250 for YouTube Buffet Plan to Stream YouTube up 4hrs. To proceed, Select: \n"
                                      "1. Auto-Renew \n"
                                      "2. One-Off \n"
                                      "3. Buy for  Friend \n"
                                      "Select:"
                        )
                    else:
                        print("Invalid Selection")
                elif video == "2":
                    print("Service not available, Please try again later")
                else:
                    print("Invalid Selection")
            elif rmdr2 == "9":
                print("Y'ello! Need Help? Chat with Zigi on your preffered channels; WhatsApp, Facebook Messenger, Web and Telegram. Details via SMS.")
            elif rmdr2 == "10":
                caller= input("1. CallerFeel \n"
                              "2. CallerTunez \n"
                              "Select"
                )
                if caller == "1":
                    awoof= input("Welcome to MTN CallerFeel. Take an action \n"
                                 "1. Awoof! Subscribe and win \n"
                                 "2. Business Card \n"
                                 "3. Cancer Box \n"
                                 "4. Choose a message box \n"
                                 "5. Packages \n"
                                 "6. Help \n"
                                 "Select:"
                    )
                elif caller == "2":
                    music= input("Welcome to MTN CallerTunez \n"
                                 "1. I WANT IT THAT WAY BY TWA \n"
                                 "2. CHAMPION SOUND BY TWA \n"
                                 "3. WAYYO ALLAH NA \n"
                                 "4. CallerTunez Awoof \n"
                                 "5. Hot Tunez \n"
                                 "6. Search CallerTunez \n"
                                 "7. Setting \n"
                                 "98. More \n"
                                 "Select:"
                    )
                    if music == "1":
                        thank= input("Thanks, to download I WANT IT THAT WAY by TWA @50.0 7 days. \n"
                                     "Please Reply: \n"
                                     "1. Accept Auto-Renewal \n"
                                     "2. Accept One-Off \n"
                        )
                        if thank == "1":
                            print("Welcome to MTN CallerTunez. Dial *410# to enjoy Unlimited tunes")
                        elif thank == "2":
                            print("Welcome to MTN CallerTunez. Dial *410# to enjoy Unlimited tunes")
                        else:
                            print("Invalid Selection")
                    elif music == "2":
                        donls= input("Thanks, to download CHAMPION SOUND by TWA @50.0 7 days. \n"
                                     "Please Reply: \n"
                                     "1. Accept Auto-Renewal \n"
                                     "2. Accept One-Off \n"
                        )
                        if donls == "1":
                            print("Welcome to MTN CallerTunez. Dial *410# to enjoy Unlimited tunes")
                        elif donls == "2":
                            print("Welcome to MTN CallerTunez. Dial *410# to enjoy Unlimited tunes")
                        else:
                            print("Invalid Selection")
                    elif music == "3":
                        rep= input("Thanks, to download Wayyo Allah Na @50.0 7 days. \n"
                                     "Please Reply: \n"
                                     "1. Accept Auto-Renewal \n"
                                     "2. Accept One-Off \n")
                        if rep == "1":
                            print("Welcome to MTN CallerTunez. Dial *410# to enjoy Unlimited tunes")
                        elif rep == "2":
                            print("Welcome to MTN CallerTunez. Dial *410# to enjoy Unlimited tunes")
                        else:
                            print("Invalid Selection")
                    elif music == "4":
                        aloof= input("CallerTunez Awoof \n"
                                     "1. Bunaya-C-Awoof \n"
                                     "2. Oh Baby 1-C-Awoof \n"
                                     "3. Tunani mai zufi-C-Awoof \n"
                                     "4. Made now-C-Awoof \n"
                                     "98. More \n"
                                     "Select:"
                        )
                        if aloof == "1":
                            rep = input("Thanks, to download Bunaya @50.0 7 days. \n"
                                        "Please Reply: \n"
                                        "1. Accept Auto-Renewal \n"
                                        "2. Accept One-Off \n")
                            if rep == "1":
                                print("Welcome to MTN CallerTunez. Dial *410# to enjoy Unlimited tunes")
                            elif rep == "2":
                                print("Welcome to MTN CallerTunez. Dial *410# to enjoy Unlimited tunes")
                            else:
                                print("Invalid Selection")
                        elif aloof == "2":
                            rep1 = input("Thanks, to download Oh Baby @50.0 7 days. \n"
                                        "Please Reply: \n"
                                        "1. Accept Auto-Renewal \n"
                                        "2. Accept One-Off \n")
                            if rep1 == "1":
                                print("Welcome to MTN CallerTunez. Dial *410# to enjoy Unlimited tunes")
                            elif rep1 == "2":
                                print("Welcome to MTN CallerTunez. Dial *410# to enjoy Unlimited tunes")
                            else:
                                print("Invalid Selection")
                        elif aloof == "3":
                            rep2 = input("Thanks, to download Tunani @50.0 7 days. \n"
                                         "Please Reply: \n"
                                         "1. Accept Auto-Renewal \n"
                                         "2. Accept One-Off \n")
                            if rep2 == "1":
                                print("Welcome to MTN CallerTunez. Dial *410# to enjoy Unlimited tunes")
                            elif rep2 == "2":
                                print("Welcome to MTN CallerTunez. Dial *410# to enjoy Unlimited tunes")
                            else:
                                print("Invalid Selection")
                        elif aloof == "4":
                            rep1 = input("Thanks, to download made one @50.0 7 days. \n"
                                         "Please Reply: \n"
                                         "1. Accept Auto-Renewal \n"
                                         "2. Accept One-Off \n")
                            if rep1 == "1":
                                print("Welcome to MTN CallerTunez. Dial *410# to enjoy Unlimited tunes")
                            elif rep1 == "2":
                                print("Welcome to MTN CallerTunez. Dial *410# to enjoy Unlimited tunes")
                            else:
                                print("Invalid Selection")
                        else:
                            print(f"Invalid Selection {aloof}")
                    elif music == "5":
                        pass
                    else:
                        print(f"Invalid Selection {music}")
                else:
                    print("Invalid Selection")
            else:
                print(f"Invalid Selection {rmdr2}")
        else:
            print(f"Invalid Selection {data}")
    elif sel =="2":
        print("Y'ellow, kindly dial *311*recharge pin# to recharge your account. Thank You.")
    elif sel == "3":
        brm= input("MTN XtraTime:Get up to N3006. Fees incl. VAT \n"
                   "1. N3000 \n"
                   "2. N2000 \n"
                   "3. N1500 \n"
                   "4. Borrow Data \n"
                   "5. More XtraTime \n"
                   "6. Account \n"
                   "Select:"
                   )
    elif sel == "4":
        bal= input("1. Access Plan Balance \n"
                   "2. Business Plan Balance \n"
                   "3. Broadband balance \n"
                   "4. Balance check \n"
                   "Select:"
                   )
        if bal == "1":
            pass
        elif bal == "2":
            pass
        elif bal == "3":
            pass
        elif bal == "4":
            pass
        else:
            print(f"Invalid Selection {bal}")
    elif sel == "5":
        print("Y'ellow, kindly dial *310# to check your account balance. Thank you.")
    elif sel == "6":
        mtns= input("Welcome to Airtime and Data Transfer/Gift Service. Please Select the service to transfer/gift \n"
                    "1. Airtime Share \n"
                    "2. Gift Data \n"
                    "3. SME Data Share \n"
                    "Select:"
                    )
        if mtns == "1":
            share= input("1. Transfer Airtime \n"
                         "2. Request Airtime from a friend \n"
                         "3. Change Pin \n"
                         "4. Forgot Pin \n"
                         "5. Create Pin \n"
                         "6. Help \n"
                         "Select:"
                         )
            if share == "1":
                recieve1= input("Enter Reciever's Phone number or Fibre ID \n"
                                ":"
                )
            elif share == "2":
                friend= input("1. Request Airtime from a friend \n"
                              "2. Block Requester \n"
                              "3. Unblock Requester \n"
                              "Select:"

                )
            elif share == "3":
                pass
            elif share == "4":
                pass
            elif share == "5":
                pass
            elif share == "6":
                helpp= input("1. Transfer Fees \n"
                             "2. Transfer Limit \n"
                             "3. Contact Us \n"
                             "Select:"

                )
            else:
                print(f"Invalid Selection {share}")
        elif mtns == "2":
            gift= input("1. Transfer from Data Balance \n"
                        "2. Buy for a Friend \n"
                        "3. Request from a Friend \n"
                        "4. View Pending Request \n"
                        "Select:"
                        )
            if gift == "1":
                fromm = input("1. From Access Data Balance \n"
                              "2. From XtraValue Bundle \n"
                              "Select"
                              )
                if fromm == "1":
                    tel = input("Enter recipient's number:")
                    if len(tel) == 11 and tel.isnumeric() and (
                            tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                        0:3] == "090" or tel[
                                0:3] == "091"):
                        damt = input("Select amount of Data you want to transfer \n"
                                     "Maximum Daily transfer is 5GB \n"
                                     "1. 100MB \n"
                                     "2. 200MB \n"
                                     "3. 500MB \n"
                                     "4. 1GB \n"
                                     "5. 2GB \n"
                                     "6. 3GB \n"
                                     "7. 5GB \n"
                                     "Select:"
                                     )
                        if damt == "1":
                            pls = input(
                                "Please confirm you want to transfer 100MB from your data bundle to 2349164900946\n"
                                "1. Proceed \n"
                                "2. Cancel \n"
                                "Select:"
                                )
                            if pls == "1":
                                print("Y'ello! Transfer of 100MB was successful.")
                            elif pls == "2":
                                print("Y'ello! Transfer of 100MB has been cancelled")
                            else:
                                print(f"Invalid Selection {pls}")
                        elif damt == "2":
                            pls = input(
                                "Please confirm you want to transfer 200MB from your data bundle to 2349164900946\n"
                                "1. Proceed \n"
                                "2. Cancel \n"
                                "Select:"
                            )
                            if pls == "1":
                                print("Y'ello! Transfer of 200MB was successful.")
                            elif pls == "2":
                                print("Y'ello! Transfer of 200MB has been cancelled")
                            else:
                                print(f"Invalid Selection {pls}")
                        elif damt == "3":
                            pls = input(
                                "Please confirm you want to transfer 500MB from your data bundle to 2349164900946\n"
                                "1. Proceed \n"
                                "2. Cancel \n"
                                "Select:"
                            )
                            if pls == "1":
                                print("Y'ello! Transfer of 500MB was successful.")
                            elif pls == "2":
                                print("Y'ello! Transfer of 500MB has been cancelled")
                            else:
                                print(f"Invalid Selection {pls}")
                        elif damt == "4":
                            pls = input(
                                "Please confirm you want to transfer 1GB from your data bundle to 2349164900946\n"
                                "1. Proceed \n"
                                "2. Cancel \n"
                                "Select:"
                            )
                            if pls == "1":
                                print("Y'ello! Transfer of 1GB was successful.")
                            elif pls == "2":
                                print("Y'ello! Transfer of 1GB has been cancelled")
                            else:
                                print(f"Invalid Selection {pls}")
                        elif damt == "5":
                            pls = input(
                                "Please confirm you want to transfer 2GB from your data bundle to 2349164900946\n"
                                "1. Proceed \n"
                                "2. Cancel \n"
                                "Select:"
                            )
                            if pls == "1":
                                print("Y'ello! Transfer of 2GB was successful.")
                            elif pls == "2":
                                print("Y'ello! Transfer of 2GB has been cancelled")
                            else:
                                print(f"Invalid Selection {pls}")
                        elif damt == "6":
                            pls = input(
                                "Please confirm you want to transfer 3GB from your data bundle to 2349164900946\n"
                                "1. Proceed \n"
                                "2. Cancel \n"
                                "Select:"
                            )
                            if pls == "1":
                                print("Y'ello! Transfer of 3GB was successful.")
                            elif pls == "2":
                                print("Y'ello! Transfer of 3GB has been cancelled")
                            else:
                                print(f"Invalid Selection {pls}")
                        elif damt == "7":
                            pls = input(
                                "Please confirm you want to transfer 5GB from your data bundle to 2349164900946\n"
                                "1. Proceed \n"
                                "2. Cancel \n"
                                "Select:"
                            )
                            if pls == "1":
                                print("Y'ello! Transfer of 5GB was successful.")
                            elif pls == "2":
                                print("Y'ello! Transfer of 5GB has been cancelled")
                            else:
                                print(f"Invalid Selection {pls}")
                    else:
                        print("Invalid Phone number")
            elif gift == "2":
                welcome= input("Welcome to MTN Data Gifting. Select data plan to gift: \n"
                               "1. Data Plans \n"
                               "2. Social Bundle \n"
                               "Select:"
                )
                if welcome == "1":
                    gfplan= input("1. Daily Plans \n"
                                  "2. Weekly Plans \n"
                                  "3. Monthly Plans \n"
                                  "4. 2-Months Plan \n"
                                  "5. 3-Months Plan \n"
                                  "Select:"
                    )
                    if gfplan == "1":
                        day= input("1. N75 for 75MB \n"
                                   "2. N100 for 110MB \n"
                                   "3. N200 for 230MB \n"
                                   "4. N500 for 1GB \n"
                                   "5. N750 for 2GB (2 days)\n"
                                   "6. N1000 for 3.2GB \n"
                                   "7. N600 for 1.5GB \n"
                                   "99. Next \n"
                                   "Select:"
                        )
                        if day == "1":
                            you= input("You will be charged N75 for the gifting of 75MB Daily Data Bundle. \n"
                                       "1. Proceed \n"
                                       "Select:"
                            )
                            if you == "1":
                                print("Activation of 75MB daily Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        elif day == "2":
                            you = input("You will be charged N100 for the gifting of 110MB Daily Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 110MB daily Plan was successful")
                        elif day == "3":
                            you = input("You will be charged N200 for the gifting of 230MB Daily Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 230MB daily Plan was successful")
                        elif day == "4":
                            you = input("You will be charged N500 for the gifting of 1GB Daily Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 1GB daily Plan was successful")
                        elif day == "5":
                            you = input("You will be charged N750 for the gifting of 2GB Daily Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 2GB daily Plan was successful")
                        elif day == "6":
                            you = input("You will be charged N1000 for the gifting of 3.2GB Daily Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 3.2GB daily Plan was successful")
                        elif day == "7":
                            you = input("You will be charged N600 for the gifting of 1.5GB Daily Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 1.5GB daily Plan was successful")
                        elif day == "99":
                            remday= input("8. N350 for 500MB \n"
                                          "9. N1,800 for 7GB \n"
                                          "Select:"
                            )
                            if remday == "8":
                                you = input("You will be charged N350 for the gifting of 500MB Daily Data Bundle. \n"
                                            "1. Proceed \n"
                                            "Select:"
                                            )
                                if you == "1":
                                    print("Activation of 500MB daily Plan was successful")
                            elif remday == "9":
                                you = input("You will be charged N1,800 for the gifting of 7GB Daily Data Bundle. \n"
                                            "1. Proceed \n"
                                            "Select:"
                                            )
                                if you == "1":
                                    print("Activation of 7GB daily Plan was successful")
                            else:
                                print(f"Inalid Selection {remday}")
                        else:
                            print(f"Invalid Selection {day}")
                    elif gfplan == "2":
                        week = input("1. N500 for 500MB \n"
                                     "2. N2,500 for 6GB \n"
                                     "3. N1,000 for 1.5GB \n"
                                     "4. N800 for 1GB \n"
                                     "5. N3,500 for 11GB \n"
                                     "6. N1,500 for 3.5GB \n"
                                     "Select:"
                        )
                        if week == "1":
                            you= input("You will be charged N500 for the gifting of 500MB weekly Data Bundle. \n"
                                       "1. Proceed \n"
                                       "Select:"
                            )
                            if you == "1":
                                print("Activation of 500MB weekly Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        elif week == "2":
                            you = input("You will be charged N2,500 for the gifting of 6GB weekly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 6GB weekly Plan was successful")
                        elif week == "3":
                            you = input("You will be charged N1,000 for the gifting of 1.5GB weekly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 1.5GB weekly Plan was successful")
                        elif week == "4":
                            you = input("You will be charged N800 for the gifting of 1GB weekly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 1GB weekly Plan was successful")
                        elif week == "5":
                            you = input("You will be charged N3,500 for the gifting of 11GB weekly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 11GB weekly Plan was successful")
                        elif week == "6":
                            you = input("You will be charged N1,500 for the gifting of 3.5GB weekly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 3.5GB weekly Plan was successful")
                        else:
                            print(f"Invalid Selection {week}")
                    elif gfplan == "2":
                        months= input("1. N1,500 @ 2GB \n"
                                      "2. N2,000 @ 2.7GB \n"
                                      "3. N2,500 @ 3.5GB \n"
                                      "4. N3,500 @ 7GB \n"
                                      "5. N4,500 @ 10GB \n"
                                      "6. N9,000 @ 25GB \n"
                                      "7. N5,500 @ 12.5GB \n"
                                      "8. N6,500 @ 16.5GB \n"
                                      "99. Next \n"
                                      "Select:"
                        )
                        if months == "1":
                            you= input("You will be charged N1,500 for the gifting of 2GB monthly Data Bundle. \n"
                                       "1. Proceed \n"
                                       "Select:"
                            )
                            if you == "1":
                                print("Activation of 2GB monthly Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        elif months == "2":
                            you = input("You will be charged N2000 for the gifting of 2.7GB monthly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 2.7GB monthly Plan was successful")
                        elif months == "3":
                            you = input("You will be charged N2,500 for the gifting of 3.5GB monthly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 3.5GB monthly Plan was successful")
                        elif months == "4":
                            you = input("You will be charged N3,500 for the gifting of 7GB monthly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 7GB daily Plan was successful")
                        elif months == "5":
                            you = input("You will be charged N4,500 for the gifting of 10GB Monthly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 10GB monthly Plan was successful")
                        elif months == "6":
                            you = input("You will be charged N9000 for the gifting of 25GB monthly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 25GB monthly Plan was successful")
                        elif months == "7":
                            you = input("You will be charged N5,500 for the gifting of 12.5GB monthly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 12.5GB monthly Plan was successful")
                        elif months == "8":
                            you = input("You will be charged N6,500 for the gifting of 16.5GB monthly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 16.5GB monthly Plan was successful")
                        elif months == "99":
                            remday= input("9. N7,000 @ 25GB \n"
                                          "10. N7,500 @ 20GB \n"
                                          "11. N11,000 @ 36GB \n"
                                          "12. N18,000 @ 75GB \n"
                                          "13. N35,000 @ 165GB \n"
                                          "14. N55,000 @ 250GB \n"
                                          "15, N16,000 @ 65GB \n"
                                          "Select:"
                            )
                            if remday == "9":
                                you = input("You will be charged N7000 for the gifting of 25GB monthly Data Bundle. \n"
                                            "1. Proceed \n"
                                            "Select:"
                                            )
                                if you == "1":
                                    print("Activation of 25GB monthly Plan was successful")
                            elif remday == "10":
                                you = input("You will be charged N7,500 for the gifting of 20GB monthly Data Bundle. \n"
                                            "1. Proceed \n"
                                            "Select:"
                                            )
                                if you == "1":
                                    print("Activation of 20GB monthly Plan was successful")
                            elif remday == "11":
                                you = input("You will be charged N3,500 for the gifting of 7GB monthly Data Bundle. \n"
                                            "1. Proceed \n"
                                            "Select:"
                                            )
                                if you == "1":
                                    print("Activation of 20GB monthly Plan was successful")
                            elif remday == "12":
                                you = input("You will be charged N18,000 for the gifting of 75GB Monthly Data Bundle. \n"
                                            "1. Proceed \n"
                                            "Select:"
                                            )
                                if you == "1":
                                    print("Activation of 75GB monthly Plan was successful")
                            elif remday == "13":
                                you = input("You will be charged N35000 for the gifting of 165GB monthly Data Bundle. \n"
                                            "1. Proceed \n"
                                            "Select:"
                                            )
                                if you == "1":
                                    print("Activation of 165GB monthly Plan was successful")
                            elif remday == "14":
                                you = input(
                                    "You will be charged N55,000 for the gifting of 250GB monthly Data Bundle. \n"
                                    "1. Proceed \n"
                                    "Select:"
                                    )
                                if you == "1":
                                    print("Activation of 250GB monthly Plan was successful")
                            elif remday == "15":
                                you = input(
                                    "You will be charged N6,500 for the gifting of 16.5GB monthly Data Bundle. \n"
                                    "1. Proceed \n"
                                    "Select:"
                                    )
                                if you == "1":
                                    print("Activation of 16.5GB monthly Plan was successful")
                            else:
                                print(f"Inalid Selection {remday}")
                        else:
                            print(f"Invalid Selection {months}")
                    elif gfplan == "3":
                        tomonths= input("1. N25,000 @ 90GB \n"
                                        "2. N40,000 @ 150GB \n"
                                        "Select:"
                        )
                        if tomonths == "1":
                            you = input(
                                "You will be charged N25,000 for the gifting of 90GB 2-months Data Bundle. \n"
                                "1. Proceed \n"
                                "Select:"
                            )
                            if you == "1":
                                print("Activation of 90GB 2-months Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        elif tomonths == "2":
                            you = input(
                                "You will be charged N40,000 for the gifting of 150GB 2-months Data Bundle. \n"
                                "1. Proceed \n"
                                "Select:"
                            )
                            if you == "1":
                                print("Activation of 150GB 2-months Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                    elif gfplan == "4":
                        threemonth= input("1. N90,000 @480GB \n"
                                          "Select:"
                        )
                        if threemonth == "1":
                            you = input(
                                "You will be charged N90,000 for the gifting of 480GB 3-months Data Bundle. \n"
                                "1. Proceed \n"
                                "Select:"
                            )
                            if you == "1":
                                print("Activation of 480GB 3-months Plan was successful")
                            else:
                                print(f"Invalid Selectio {you}")
                    else:
                        print(f"Invalid Selection {gfplan}")
                elif welcome == "2":
                    socialb= input("1. WhatsApp \n"
                                   "2. Facebook \n"
                                   "3. TikTok \n"
                                   "4. Ayoba \n"
                                   "5. All Social Bundles \n"
                                   "Select:"
                    )
                    if socialb == "1":
                        app1= input("WhatsApp \n"
                                    "1. Daily @ N25 for 20MB \n"
                                    "2. Weekly @ N50 for 40MB \n"
                                    "3. Monthly @ N150 for 120MB \n"
                                    "Select:"

                        )
                        if app1 == "1":
                            you = input("You will be charged N25 for the gifting of 20MB WhatsApp Daily Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 20MB WhatsApp daily Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        elif app1 == "2":
                            you = input("You will be charged N50 for the gifting of 40MB WhatsApp weekly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 40MB WhatsApp weekly Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        elif app1 == "3":
                            you = input("You will be charged N150 for the gifting of 120MB WhatsApp monthly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 120MB WhatsApp monthly Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        else:
                            print(f"Invalid Selection {app1}")
                    elif socialb == "2":
                        app2= input("Facebook \n"
                                    "1. Daily @ N25 for 20MB \n"
                                    "2. Weekly @ N50 for 40MB \n"
                                    "3. Monthly @ N150 for 120MB \n"
                                    "Select:"

                        )
                        if app2 == "1":
                            you = input("You will be charged N25 for the gifting of 20MB Facebook Daily Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 20MB Facebook daily Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        elif app2 == "2":
                            you = input("You will be charged N50 for the gifting of 40MB Facebook weekly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 40MB Facebook weekly Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        elif app2 == "3":
                            you = input("You will be charged N150 for the gifting of 120MB Facebook monthly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 120MB Facebook monthly Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        else:
                            print(f"Invalid Selection {app2}")
                    elif socialb == "3":
                        app3= input("1. N50 for 150MB \n"
                                    "2. N400 for 2GB/7 days \n"
                                    "Select:"

                        )
                        if app3 == "1":
                            you = input(
                                "You will be charged N50 for the gifting of 150MB TikTok daily Data Bundle. \n"
                                "1. Proceed \n"
                                "Select:"
                                )
                            if you == "1":
                                print("Activation of 150MB TikTok daily Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        elif app3 =="2":
                            you = input(
                                "You will be charged N400 for the gifting of 2GB TikTok weekly Data Bundle. \n"
                                "1. Proceed \n"
                                "Select:"
                            )
                            if you == "1":
                                print("Activation of 2GB TikTok weekly Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        else:
                            print(f"Invalid Selection {app3}")
                    elif socialb == "4":
                        app4= input("Ayoba \n"
                                    "1. N50 for 40MB/7 days \n"
                                    "Select:"

                        )
                        if app4 == "1":
                            you = input(
                                "You will be charged N50 for the gifting of 40MB Ayoba weekly Data Bundle. \n"
                                "1. Proceed \n"
                                "Select:"
                            )
                            if you == "1":
                                print("Activation of 40MB Ayoba weekly Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        else:
                            print(f"Invalid Selection {app4}")
                    elif socialb == "5":
                        all1= input("1. Daily @N100 for 200MB \n"
                                    "2. Weekly @ N200 for 470MB \n"
                                    "3. Monthly @ N450 for 1.2GB \n"
                                    "Select:"
                        )
                        if all1 == "1":
                            you = input("You will be charged N100 for the gifting of 200MB All Socials Daily Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 200MB All Socials daily Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        elif all1 == "2":
                            you = input("You will be charged N200 for the gifting of 470MB All Socials weekly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 470MB All Socials weekly Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        elif all1 == "3":
                            you = input("You will be charged N450 for the gifting of 1.2GB All Socials monthly Data Bundle. \n"
                                        "1. Proceed \n"
                                        "Select:"
                                        )
                            if you == "1":
                                print("Activation of 1.2GB All Socials monthly Plan was successful")
                            else:
                                print(f"Invalid Selection {you}")
                        else:
                            print(f"Invalid Selection {all1}")
                    else:
                        print(f"Invalid Selection {socialb}")
                else:
                    print(f"Invalid Selection {welcome}")
            elif gift == "3":
                toreq= input("To Request Data from a friend enter Phone number (e.g 08xxxxxxxxx) \n"
                             ":"

                )
                if len(toreq) == 11 and toreq.isnumeric() and (
                        toreq[0:3] == "070" or toreq[0:3] == "080" or toreq[0:3] == "081" or toreq[
                    0:3] == "090" or toreq[
                            0:3] == "091"):
                    print("Y'ello! Your Request for data to Phone number 2347037464312 has been delivered.")
                else:
                    print("Invalid Phone Number Entered")
            elif gift == "4":
                print("You have no pending requests. Thank you!")
            else:
                print(f"Invalid Selection {gift}")
        elif mtns == "3":
            dashr= input("1. Pin Retrieval & Reset \n"
                         "2. Check Balance \n"
                         "3. Share Data to Others \n"
                         "Select:"
                         )
            if dashr == "1":
                maid= input("Enter your mother's maiden name:")
                if maid == "Bolanle":
                    dob= input("Enter your date of birth e.g: dd/mm/yyy:")
                    if dob == "07/07/007":
                        sorg= input("Enter state of origin:")
                        if sorg == "Kwara state":
                            print("Oops, Pin retrieval was not successful")
            elif dashr == "2":
                print("Dear Customer, you don't have any active data bundle. Please dial *312*1# to buy another data bundle")
            elif dashr == "3":
                share= input("1. Share 500MB \n"
                             "2. Share 1GB \n"
                             "3. Share 2GB \n"
                             "4. Share 3GB \n"
                             "5. Share 10GB \n"
                             "Select:"
                )
                if share == "1":
                    tel = input("Enter recipient's number:")
                    if len(tel) == 11 and tel.isnumeric() and (
                            tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                        0:3] == "090" or tel[
                                0:3] == "091"):
                        pin= input("Enter 4-digit pin:")
                        if pin == "0000":
                            print("You have entered default PIN. Please change your PIN and try again.")
                    else:
                        print("Invalid Phone number")
                elif share == "2":
                    tel = input("Enter recipient's number:")
                    if len(tel) == 11 and tel.isnumeric() and (
                            tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                        0:3] == "090" or tel[
                                0:3] == "091"):
                        pin = input("Enter 4-digit pin:")
                        if pin == "0000":
                            print("You have entered default PIN. Please change your PIN and try again.")
                    else:
                        print("Invalid Phone number")
                elif share == "3":
                    tel = input("Enter recipient's number:")
                    if len(tel) == 11 and tel.isnumeric() and (
                            tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                        0:3] == "090" or tel[
                                0:3] == "091"):
                        pin = input("Enter 4-digit pin:")
                        if pin == "0000":
                            print("You have entered default PIN. Please change your PIN and try again.")
                    else:
                        print("Invalid Phone number")
                elif share == "4":
                    tel = input("Enter recipient's number:")
                    if len(tel) == 11 and tel.isnumeric() and (
                            tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                        0:3] == "090" or tel[
                                0:3] == "091"):
                        pin = input("Enter 4-digit pin:")
                        if pin == "0000":
                            print("You have entered default PIN. Please change your PIN and try again.")
                    else:
                        print("Invalid Phone number")
                elif share == "5":
                    tel = input("Enter recipient's number:")
                    if len(tel) == 11 and tel.isnumeric() and (
                            tel[0:3] == "070" or tel[0:3] == "080" or tel[0:3] == "081" or tel[
                        0:3] == "090" or tel[
                                0:3] == "091"):
                        pin = input("Enter 4-digit pin:")
                        if pin == "0000":
                            print("You have entered default PIN. Please change your PIN and try again.")
                    else:
                        print("Invalid Phone number")
                else:
                    print(f"Invalid Selection {share}")
            else:
                print(f"Invalid Selection {dashr}")
        else:
            print(f"Invalid Selection {mtns}")
    elif sel == "7":
        print("No active service found. thank you")
    elif sel == "8":
        print("Dear Customer, kindly dial *996# to link your NIN. Thank you.")
    else:
        print("Input Error, please input again")
else:
    print("Invalid MMI Code")
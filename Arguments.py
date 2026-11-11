def total_cal(bill_amount,tip_per):
    total=bill_amount + bill_amount *0.01*tip_per
    total = round(total,2)
    print("please pay $", total)
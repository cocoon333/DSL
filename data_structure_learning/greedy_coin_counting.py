def money_counter(bill_total):
    assert(type(bill_total) is int)
    num_10_bills = 0
    num_5_bills = 0
    num_2_bills = 0
    num_1_bills = 0

    num_10_bills = bill_total/10
    bill_total -= num_10_bills*10
    num_5_bills = bill_total/5
    bill_total -= num_5_bills*5
    num_2_bills = bill_total/2
    bill_total -= num_2_bills*2
    num_1_bills = bill_total
    total_bills = num_10_bills+num_5_bills+num_2_bills+num_1_bills

    return "$10 bills: %d\n$5 bills: %d\n$2 bills: %d\n$1 bills: %d\nTotal number of bills:%d" % (num_10_bills, num_5_bills, num_2_bills, num_1_bills, total_bills)

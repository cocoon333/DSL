class CreditPlan(object):
    def __init__(self):
        self.month = 1
        self.total_balance_owed = input('Enter the amount of payment: ')
        self.monthly_payment = 0.05*(self.total_balance_owed-0.1*self.total_balance_owed)
        self.monthly_interest = self.monthly_payment*0.01
        self.monthly_principal_amount = self.monthly_payment-self.monthly_interest
        self.balanced_after_pay = self.total_balance_owed-self.monthly_payment

    def table(self):
        print 'Month   Total Balance Owed   Interest   Principal Amount   Payment   Balance Remaining'
        while self.balanced_after_pay > 0:
            print self.month, '      ', self.total_balance_owed, '        ', self.monthly_interest, '     ', self.monthly_principal_amount, '         ', self.monthly_payment, '            ', self.balanced_after_pay
            self.month += 1
            self.total_balance_owed = self.balanced_after_pay
            self.balanced_after_pay -= self.monthly_payment

if __name__ == '__main__':
    cp = CreditPlan()
    cp.table()

#DONE

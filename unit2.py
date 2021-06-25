def get_monthly_payment(balance, interest_rate, months=12):
    """
    Args:
        balance: the outstanding balance on the credit card
        interest_rate: annual interest rate as a decimal
        months: the period for which calculation is done
    Returns:
        the lowest monthly payment that will pay off all debt in under 1 year,:
    """
    month_payment, remaining_balance, count = 10, 0, 0
    while True:
        remaining_balance = balance
        count += 1
        for i in range(months):
            anpaid_balance = (remaining_balance - count * month_payment)
            remaining_balance = anpaid_balance + anpaid_balance * interest_rate / 12.0

        if remaining_balance < 0:
            break
    return count * month_payment


def get_credit_card_balance(balance, interest_rate, payment_rate, months=12):
    """
    Args:
        balance: the outstanding balance on the credit card
        interest_rate: annual interest rate as a decimal
        payment_rate: minimum monthly payment rate as a decimal
        months: the months after that credit card balance is calculated

    Returns:
        Remaining balance at the end of the months:
    """

    for n in range(months):
        anpaid_balance = (balance - balance * payment_rate)
        balance = anpaid_balance + anpaid_balance * interest_rate / 12.0
    return round(balance, 2)




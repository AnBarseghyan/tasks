def get_monthly_payment(balance: int, interest_rate: float, months=12) -> int:
    """
    Args:
        balance: the outstanding balance on the credit card
        interest_rate: annual interest rate as a decimal
        months: the period for which calculation is done
    Returns:
        the lowest monthly payment that will pay off all debt in under 1 year,:
    """
    month_payment,  remaining_balance, count = 10, 0, 0
    while True:
        remaining_balance = balance
        count += 1
        for i in range(months):
            anpaid_balance = (remaining_balance - count * month_payment)
            remaining_balance = anpaid_balance + anpaid_balance * interest_rate / 12.0

        if remaining_balance <  0:
            break
    return count * month_payment


print(get_monthly_payment(3926, 0.2))
def get_monthly_payment(balance: int, interest_rate: float, months=12):
    """
    Args:
        balance: the outstanding balance on the credit card
        interest_rate: annual interest rate as a decimal
        months: the period for which calculation is done
    Returns:
        the lowest monthly payment that will pay off all debt in under 1 year,:
    """
    lower_bound = balance / 12
    upper_bound = (balance * (1 + interest_rate / 12)**12) / 12
    epsilon = 0.01
    while (upper_bound - lower_bound) > epsilon:
        month_payment = (lower_bound + upper_bound) / 2
        remaining_balance = balance
        for i in range(months):
            anpaid_balance = remaining_balance - month_payment
            remaining_balance = anpaid_balance + anpaid_balance * interest_rate / 12.0
        if remaining_balance == 0:
            break
        elif remaining_balance > 0:
            lower_bound = month_payment
        else:
            upper_bound = month_payment
    return round(month_payment, 2)

import time
start = time.time()
print(get_monthly_payment(320000, 0.2))
print(time.time() - start)

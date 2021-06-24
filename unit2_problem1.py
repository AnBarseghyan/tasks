import time

def get_credit_card_balance(balance: int, interest_rate: float, payment_rate: float, months=12) -> float:
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



start = time.time()
print(get_credit_card_balance(42, 0.2, 0.04))
print(time.time() - start)



# def get_credit_card_balance(balance: int, interest_rate: float, payment_rate: float,
#                              months: int) -> float:
#     """
#
#     Args:
#         balance: the outstanding balance on the credit card
#         interest_rate: annual interest rate as a decimal
#         payment_rate: minimum monthly payment rate as a decimal
#         months: the months after that credit card balance is calculated
#
#     Returns:
#         Remaining balance at the end of the year:
#     """
#     if months == 1:
#         anpaid_balance = (balance - balance * payment_rate)
#         balance = anpaid_balance + anpaid_balance * interest_rate / 12.0
#     else:
#         balance = get_credit_card_balance(get_credit_card_balance(balance, interest_rate,  payment_rate, 1),
#                                           interest_rate, payment_rate, months-1)
#
#     return round(balance, 2)

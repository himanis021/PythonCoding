'''
if its hot
    its a hot day
    drink plenty of water
otherwise if its cold
    its cold day
    wear warm clothes
otherwise
    its a lovely day
'''

is_hot = False
is_cold = False
if is_hot:
    print("its a hot day")
    print("drink plenty of water")
elif is_cold:
    print("its cold day")
    print("wear warm clothes")
else:
    print("enjoy your day")

"""
Price of house is $1M
if buyer has good credit
    they need to put down 10%
otherwise
    they need to put down 20%
print the down payment
"""

price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = price * .1
else:
    down_payment = price * .2
print(f"Down payment: ${down_payment}")


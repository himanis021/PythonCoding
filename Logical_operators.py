"""
if applicant has high income AND good credits
   Eligible for Loan
"""

has_high_income = False
has_good_credit = True
if has_good_credit and has_high_income:     # both should be true when AND is used.
    print("Eligible for loan")
if has_high_income or has_good_credit:   # any 1 condition should be true
    print("eligible fo loan 2")


# if applicant has good credit and doesn't hve a criminal record then eligibe for loan
has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:   # not changes true to false and vice-versa
    print("eligible")


return_day, return_month, return_year = map(int, input().split())
due_day, due_month, due_year = map(int, input().split())

fine = -1

if return_year < due_year:
    # Not late
    fine = 0
elif return_year == due_year:
    if return_month <= due_month:
        if return_day <= due_day:
            # Not late
            fine = 0
        else:
            # Days late
            fine = 15 * (return_day - due_day)
    else:
        # More than a calendar month late
        fine = 500 * (return_month - due_month)
else:
    # More than a calendar year late
    fine = 10000

print(fine)

#!/bin/python3

import sys

gmailAccounts = []

N = int(input().strip())
for a0 in range(N):
    firstName, emailID = input().strip().split(' ')
    firstName, emailID = [str(firstName),str(emailID)]
    if '@gmail.com' in emailID:
        gmailAccounts.append(firstName)

for g in sorted(gmailAccounts):
    print(g)

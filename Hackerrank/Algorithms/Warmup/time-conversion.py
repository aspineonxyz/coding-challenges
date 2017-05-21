time = input().strip()
hr = int(time[0:2])
newHr = time[0:2]
if 'PM' in time:
    if hr != 12:
        newHr = str(hr + 12)
elif hr == 12 :
        newHr = "00"
print(newHr + time[2:8])

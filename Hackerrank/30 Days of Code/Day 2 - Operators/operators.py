mealCost = float(input())
tip, tax = mealCost * (int(input())/100), mealCost * (int(input())/100)
totalCost = str(int(round(mealCost + tip + tax)))
print("The total meal cost is " + totalCost + " dollars.")

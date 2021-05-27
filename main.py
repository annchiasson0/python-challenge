
import pandas as pd
import os

budget_csv = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

budget_data = pd.read_csv(budget_csv)
#budget_data
#budget_data.info()

#budget_data['Date'] =  pd.to_datetime(budget_data['Date'], infer_datetime_format=True)
#budget_data.info()

total_months = len(budget_data)
#total_months

net_profit = budget_data['Profit/Losses'].sum()
#net_profit

sum = 0
max = 0
min = 0
for i in range(total_months-1):
    change = budget_data['Profit/Losses'][i+1]-budget_data['Profit/Losses'][i]
    sum = sum + change
    if change > max:
        max = change 
        imax = i 
    if change < min:
        min = change 
        imin = i 
average_change = sum/(total_months-1)
#average_change

#print(max, budget_data['Date'][imax+1])
#print(min, budget_data['Date'][imin+1])



print('Financial Analysis')
print('----------------------------')
print ("Total Months: %2d" % total_months) #d=int
print ("Total: $%d" % net_profit)
print ("Average Change: $%.2f" % average_change) #f = floating point, 2=2 decimal places
print ("Greatest Increase in Profits: %s ($%d)" % (budget_data['Date'][imax+1],max))
print ("Greatest Decrease in Profits: %s ($%d)" % (budget_data['Date'][imin+1],min)) #%s = string







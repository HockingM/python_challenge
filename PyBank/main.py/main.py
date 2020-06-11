# import modules for csv reader and operating system interaction

import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

total_months = 0
total_profit = 0
prior_month = 0
monthly_profit = 0

month_year = []
average_change = []

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # ignore the 1st row
    header = next(csvreader)
 
    for row in csvreader:
        total_months +=1 #count the rows
        total_profit = total_profit + int(row[1]) # sum the profit and loss
  
        # calculate average change by month
        if total_months >1:
            prior_month = monthly_profit
       
        # create list of months
        month = str(row[0])
        month_year.append(month)

         # calculate monthly change in profit and save to list
        monthly_profit = int(row[1])
        monthly_change = monthly_profit - prior_month    
           
        if total_months >=2:
            average_change.append(monthly_change)

# find maximum and minimum profits and months
max_profit = max(average_change)
min_profit = min(average_change)
max_index = average_change.index(max_profit) + 1
min_index = average_change.index(min_profit) + 1

# calculate average monthly change for all years
sum_average_change = sum(average_change)
total_average = round(sum_average_change/(total_months - 1),2)

    
# print report
print("\n\nFinancial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total: " + str(total_profit))
print("Average Change: $" + str(total_average))
print("Greatest Increase in Profits: " + str(month_year[max_index]) + "  ($"+ str(max_profit) + ")")
print("Greatest Decrease in Profits: " + str(month_year[min_index]) + "  ($" + str(min_profit) +")\n")

# write report
report_path = os.path.join('..', 'Analysis',"Analysis.txt")

my_file = open(report_path, 'w')

my_file.write("Financial Analysis")
my_file.write("\n----------------------------")
my_file.write("\nTotal Months: " + str(total_months))
my_file.write("\nTotal: " + str(total_profit))
my_file.write("\nAverage Change: $" + str(total_average))
my_file.write("\nGreatest Increase in Profits: " + str(month_year[max_index]) + "  ($"+ str(max_profit) + ")")
my_file.write("\nGreatest Decrease in Profits: " + str(month_year[min_index]) + "  ($" + str(min_profit) +")")

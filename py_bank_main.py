#Import the os module
import os
#Module for reading CSV files
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')
#Reading using CSV module
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #Skip the header row
    row = next(csvreader)
    #Create lists to store data
    monthly_chg = []
    date = []
    #Store Variables
    total_months = 0    
    total_PL = 0
    int_profit = 867884
    total_chg_profit = 0
#Read the header row
    #csv_header = next(csvreader)
    #print(f"csv header: {csv_header}")
#Read each row in row[0] of data after the header
    for row in csvreader:
        #Count the number of cells with values
        total_months += 1
        #Store Date list
        date.append(row[0])
        #Calculate the net total amount of "Profit/Loses" over the entire period
        total_PL += int(row[1])
        #Caluculate Monthly Change, first determine the monthly change    
        profit = int(row[1])
        #print(f"{profit} profit")
        monthly_chg_profit = profit - int_profit
        #print(f"{monthly_chg_profit} monthly chg profit")
        #Store in Montly Chg List
        monthly_chg.append(monthly_chg_profit)
        #Assign the next row profit as the new int_profit
        int_profit = profit
        #Calculate the total change in profit in order to help calculate the average change in profits
        total_chg_profit= total_chg_profit + monthly_chg_profit
        #print(f"{total_chg_profit} tot chg profit")
        #Caluculate average change in profits
        average_chg_profit = round(total_chg_profit/total_months, 2)
        #Calculate the greatest increase in profit and date
        greatest_inc_profits=max(monthly_chg)
        #Idenify the date in the same index as the greatest increase profit figure
        inc_date = date[monthly_chg.index(greatest_inc_profits)]
        #Calculate the greatest decrease in profit
        greatest_dec_profits=min(monthly_chg)
        #Identify the date in the same index as the greatest decrease profit figure
        dec_date = date[monthly_chg.index(greatest_dec_profits)]
        
#Print the Total Number of Months
print("Financial Analysis")
print("--------------------------")
print(f"Total Months:  {total_months}")
print(f"Total: ${total_PL}")   
print(f"Total: $ {average_chg_profit}")
print(f"Greatest Increase in Profits: {inc_date} ${greatest_inc_profits}")
print(f"Greatest Decrease in Profits: {dec_date} ${greatest_dec_profits}")

#Output a txt file
with open('financial_analysis.txt', "w") as text:
    text.write("Financial Analysis")
    text.write("--------------------------")
    text.write(f"Total Months:  {total_months}")
    text.write(f"Total: ${total_PL}")   
    text.write(f"Total: $ {average_chg_profit}")
    text.write(f"Greatest Increase in Profits: {inc_date} ${greatest_inc_profits}")
    text.write(f"Greatest Decrease in Profits: {dec_date} ${greatest_dec_profits}")
        
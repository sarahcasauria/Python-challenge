# In this challenge, you are tasked with creating a Python script to analyze the financial records of your company. 
#You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses". 
#(Thankfully, your company has rather lax standards for accounting, so the records are simple.)
# Your task is to create a Python script that analyzes the records to calculate each of the following:


# The total number of months included in the dataset


# The net total amount of "Profit/Losses" over the entire period


# The changes in "Profit/Losses" over the entire period, and then the average of those changes


# The greatest increase in profits (date and amount) over the entire period


# The greatest decrease in profits (date and amount) over the entire period

#First import the relevant modules to read the csv data
import os
import csv

#Create a path to read the data from the budget_data.csv file
pybank_csv = os.path.join('Resources', 'budget_data.csv')

#With open function to open and read the csv
with open(pybank_csv, encoding = 'utf') as csvfile:
    pybank_csv_reader = csv.reader(csvfile, delimiter = ',')
    print('--------------------------------------------------')
    print(pybank_csv_reader)
    #Skip reading the header
    next(pybank_csv_reader,None)
    
    #------------------------------
    #----TOTAL NUMBER OF MONTHS----
    #------------------------------
   
    #Create new variable for months
    total_months = []
    
    #Append total months list with value in current row in column 1
    for row in pybank_csv_reader:
        total_months.append(row[0])
        
    #Create new variable to store calculation of total number of months
    total_months_num = int(len(total_months))

    #This code resets the pybank_csv_reader loop to use again as it was already exhausted in the previous loop above.
    csvfile.seek(0)
    next(pybank_csv_reader)
    
    #-----------------------------
    #----NET TOTAL PROFIT/LOSS----
    #-----------------------------
    
    #Create variable for total net profit/loss
    net_profit_loss = 0
    
    #Iterate new loop to cumulatively add together the profit/loss value in each row
    #Remember to cast as integer for this calculation to work
    for row in pybank_csv_reader:
        net_profit_loss+=int(row[1])
    
    
    #Reset the row loop again for the next task
    csvfile.seek(0)
    next(pybank_csv_reader)
    
    #-------------------------------------
    #----MONTH TO MONTH AVERAGE CHANGE----
    #-------------------------------------

    #Saving first data row in csv into a variable (since we already excluded the header)
    first_row = next(pybank_csv_reader)
    # print('--------------------------------------------------')
    # print(first_row)
    
    #Using the value of the first data row, second column to define our initial profit/loss
    prev_profit_loss = int(first_row[1])
    # print('--------------------------------------------------')
    # print(prev_profit_loss)
    # print('--------------------------------------------------')
    
    #Create a list to store the monthly changes in to average later
    monthly_change_list = []
    great_inc_date = str()
    great_inc_profit = 0
    
    great_dec_date = str()
    great_dec_profit = 0
    
    #Find the differences between profit/loss for current row and previous row
    for profit_loss in pybank_csv_reader:
        monthly_change = int(profit_loss[1]) - prev_profit_loss
        
        #Redefine previous profit/loss value as the current one to use when restarting the loop
        prev_profit_loss = int(profit_loss[1])
        
        #Add newly calculated monthly change to list
        monthly_change_list.append(monthly_change)
        
    #----------------------------------------------
    #----GREAT INCREASE AND DECREASE IN PROFITS----
    #----------------------------------------------
        if monthly_change > great_inc_profit:
            great_inc_profit = monthly_change
            great_inc_date = profit_loss[0]
            
        elif monthly_change < great_dec_profit:
            great_dec_profit = monthly_change
            great_dec_date = profit_loss[0]
    
    # print('--------------------------------------------------')
    # print(monthly_change_list)
    
    #Calculate the average monthly change by summing all 
    #monthly changes in the list and dividing by length of list
    average_monthly_change = int(sum(monthly_change_list))/int(len(monthly_change_list))
    #Make sure it is set to two decimal places
    average_monthly_change = "{:.2f}".format(average_monthly_change)
    

    #----------------------------
    #----FINAL ANALYSIS TABLE----
    #----------------------------
    print("Financial Analysis")
    #----Total number of months for the financial analysis section----
    print('--------------------------------------------------')
    print(f"Total Number of Months: {total_months_num}")
    #----Total profit/loss for the financial analysis section----
    print (f"Total net profit/loss: ${net_profit_loss}")
    #----Average monthly profit/loss change----
    print(f"Average Change: {average_monthly_change}")
    #----Greatest Increase and Decrease in Profits----
    print(f"Greatest Increase in Profits: {great_inc_date} (${great_inc_profit})")
    print(f"Greatest Decrease in Profits: {great_dec_date} (${great_dec_profit})")
    
#-----------------------------
#----EXPORTING TO TXT FILE----
#-----------------------------

with open('analysis/pybank_output_file.txt', 'w', encoding = 'utf-8') as f:
    f.write("Financial Analysis\n" + "--------------------\n" + 
                "Total Number of Months: " + str(total_months_num) + "\n" +
                "Total Net Profit/Loss: $" + str(net_profit_loss) + "\n" +
                "Average Monthly Change: " + str(average_monthly_change) + "\n" +
                "Greatest Increase in Profits: " + str(great_inc_date) + " $" + str(great_inc_profit) + "\n" +
                "Greatest Decrease in Profits: " + str(great_dec_date) + " $" + str(great_dec_profit) + "\n")
    f.close()
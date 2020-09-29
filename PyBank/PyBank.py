import os

import csv

dirname = os.path.dirname(__file__)

csvpath = os.path.join(dirname,'Resources', 'budget_data.csv')

print (csvpath)

# def sum_of_budget_data(date):
#     total = 0 
#     for val in date:
#         total = total + val
#     return total

#     budget_data = [Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec]
#     print "The total is", sum_of_budget_data(budget_data)

    total_net = 0

    total_months = 0
# Set Path for Text File
    file_path = os.path.join("analysis","PyBank.txt")

# Open Text File
    f = open(file_path,'w', encoding="utf8")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:

# Track total
        total_months += 1
        total_net = total_net + int(row[1])

# Track net change
        list_a= [total_net,total_months]
        list_b= [net_change,]
        
    for row in csvreader:
        ...
        list_a.append(total_net)
        list_b.append(row[0])
        
        net_change = int(row[1]) - previous_net
        avg = sum(net_changes)/len(net_changes)

# Calculate the greatest increase
# Calculate the greatest decrease
# Calculate the average net change

    print(total_months)
    print(total_net)
    print(net_change)
   





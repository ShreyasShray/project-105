# import all modules
import csv
import math

# opening the file and getting the list of data
with open("standard_deviation_for_project.csv", newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data = file_data[0]

# getting the mean of data
total = 0
for x in file_data:
    total += float(x)
n = len(file_data)
mean = total/n

# getting the total sum for standard deviation
total_sum = 0
for x in file_data:
    a = int(x) - mean
    a = a**2
    total_sum += a

# getting the data for root
data_for_sqrt = total_sum/(len(file_data)-1) 

# getting the standard deviation
standard_deviation = math.sqrt(data_for_sqrt)

print("Standard Deviation is ", standard_deviation)
import csv
import numpy 
import math
import matplotlib.pyplot as plt


f = open("ccrb_datatransparencyinitiative_20170207.csv", 'rU')
#f = open("test_data2.csv", 'rU')
csv_f = csv.reader(f, delimiter = ",")
data = []
for row in csv_f:
    data.append(row)

#print(len(data))

#data = numpy.array(data)
# find rows that has NA data

COLUMN_INDEX1 = 4 # index
COLUMN_INDEX2 = 10
COLUMN_INDEX3 = 12
COLUMN_INDEX4 = 13
REMOVE_WORDS = ['Other/NA', 'NA']


# Build a new list 
data_without_NA1 = []
data_without_NA2 = []
data_without_NA3 = []
data_without_NA4 = []

for row in data:
	column = row[COLUMN_INDEX1] # check index 4
	if not any(remove_word in column for remove_word in REMOVE_WORDS):
		data_without_NA1.append(row)
		
for row in data_without_NA1:
	column = row[COLUMN_INDEX2] # check index 10
	if not any(remove_word in column for remove_word in REMOVE_WORDS):
		data_without_NA2.append(row)
	

for row in data_without_NA2:
	column = row[COLUMN_INDEX3] # check index 12
	if not any(remove_word in column for remove_word in REMOVE_WORDS):
		data_without_NA3.append(row)


for row in data_without_NA3:
	column = row[COLUMN_INDEX4] # check index 13
	if not any(remove_word in column for remove_word in REMOVE_WORDS):
		data_without_NA4.append(row)		
print('number of rows', len(data_without_NA4))		


complete_data = numpy.array(data_without_NA4)


data_col1_14 = complete_data[1:,0:14]
#print(ID)
data_uniq_ID = numpy.unique(data_col1_14, axis=0)
#print(data_uniq_ID)
uniq_complain_num = len(data_uniq_ID)
#print('uniq compaint number', uniq_complain_num)


uniq_borough = numpy.unique(data_uniq_ID[0:,4],return_counts = True)
uniq_borough = numpy.array(uniq_borough)
uniq_borough = uniq_borough.transpose()

#print('unique borough name and number', uniq_borough)

# most_complain_num = numpy.argmax(uniq_borough[:, 1])  
# print('most compaint number:', most_complain_num)

#print(float(most_complain_num)/float(uniq_complain_num))

population = numpy.array([
	['Bronx', '1455720'],
	['Brooklyn', '2629150'], 
	['Manhattan', '1643734'], 
	['Outside NYC', '0'], 
	['Queens', '2333054'], 
	['Staten Island', '476015']
	])
# print(population)

com_per_cap_list = []
for i in range(6):
	if i != 3:
		com_per_cap = float(list(uniq_borough[:,1])[i])/float(list(population[:,1])[i])
		com_per_cap_list.append(com_per_cap)

print(max(com_per_cap_list))

print(float(15536)/(float(1455720)/100000))


year_data = data_uniq_ID[0:,2:4]
#print(year_data)
closed_year = year_data[:,0] 
received_year = year_data[:,1]

int_closed_year = [int(i) for i in closed_year]
int_received_year = [int(i) for i in received_year]

# print(int_closed_year)
# print(int_received_year)

time_list = []
for t in range(0, len(year_data)):
 	time = int_closed_year[t] - int_received_year[t]
 	time_list.append(time)

print(numpy.average(time_list))


# <Q> stop and frisk
stop_and_frisk = data_uniq_ID[:,3:10]
#print(stop_and_frisk)

stop_and_frisk_yes = numpy.array([row for row in stop_and_frisk if row[6] == "TRUE"])
#print(stop_and_frisk_yes)

num_of_stop_frisk = numpy.unique(stop_and_frisk_yes[:,0], return_counts = True)
num_of_stop_frisk = numpy.array(num_of_stop_frisk).transpose()

x = num_of_stop_frisk[:,0]
y = num_of_stop_frisk[:,1]
x_int = numpy.array([int(i) for i in x])
y_int = numpy.array([int(i) for i in y])


# plt.figure()
# axis = plt.axis([1999,2020,0,3000])
m,b = numpy.polyfit(x_int,y_int,1)
# plt.plot(x_int,y_int,'r*')

# print(m,b)
prediction = 2018 * m + b
print(prediction)





data_col14 = complete_data[1:,14]
data_uniq_ale = numpy.unique(data_col14, axis=0, return_counts='True')
print(data_uniq_ale)


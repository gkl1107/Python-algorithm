#/user/bin/python

#given a list of US states, and a list of raw data includes US states and cities, categories states and cities into a dictionary
 
states = ['Washington', 'Wisconsin', 'West Virginia', 'Florida', 'Wyoming', 'New Hampshire', 'New Jersey', 'New Mexico', 'National', 'North Carolina', 'North Dakota', 'Nebraska', 'New York', 'Rhode Island', 'Nevada', 'Guam', 'Colorado', 'California', 'Georgia', 'Connecticut', 'Oklahoma', 'Ohio', 'Kansas', 'South Carolina', 'Kentucky', 'Oregon', 'South Dakota', 'Delaware', 'District of Columbia', 'Hawaii', 'Puerto Rico', 'Texas', 'Louisiana', 'Tennessee', 'Pennsylvania', 'Virginia', 'Virgin Islands', 'Alaska', 'Alabama', 'American Samoa', 'Arkansas', 'Vermont', 'Illinois', 'Indiana', 'Iowa', 'Arizona', 'Idaho', 'Maine', 'Maryland', 'Massachusetts', 'Utah', 'Missouri', 'Minnesota', 'Michigan', 'Montana', 'Northern Mariana Islands', 'Mississippi']


raw_data = ['Alabama', 'Auburn ', 'Florence ', 'Jacksonville ', 'Livingston ', 'Montevallo ', 'Troy ', 'Tuscaloosa ', 'Tuskegee ', 
		'Alaska', 'Fairbanks ', 
		'Arizona', 'Flagstaff ', 'Tempe ', 'Tucson ']

category = {}

while len(raw_data) > 0:

    for i in range(len(raw_data)-1, -1, -1):
        if raw_data[i] in states:

        	category[raw_data[i]] = raw_data[i+1:]
        	break
    raw_data = raw_data[0:i]
    
        
print(category)  



    
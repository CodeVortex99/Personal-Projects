PlantInfo = {'Rose':{'Moisture(%)':45, 'Sunlight(hours/day)':8, 'Expected Status': 'Healthy'}, 
             'Fern':{'Moisture(%)':20, 'Sunlight(hours/day)':5, 'Expected Status': 'Needs Water'},
             'Cactus': {'Moisture(%)':90, 'Sunlight(hours/day)':9, 'Expected Status': 'Too Much Water'},
             'Lily': {'Moisture(%)':70, 'Sunlight(hours/day)':3, 'Expected Status': 'Needs More Sun'},
             'Tulip': {'Moisture(%)':60, 'Sunlight(hours/day)':6, 'Expected Status': 'Healthy'}}

def Main():
    print('1. View Plant Info')
    print('2. Edit Plant details via name')
    print('3. Exit')
    Choice = input('Enter your choice: ')
    return Choice

Choice = Main()
if Choice == 1:
    Display_PlantInfo()
elif Choice == 2:
    Update_PlantInfo()
elif Choice == 3:
    exit()

#Needs to be completed
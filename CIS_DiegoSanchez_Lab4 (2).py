#Module 4 Lab-4
#Diego Sanchez
#2/25/24
#this program takes the monthly sales for a store and % increase
#and displays to the user the earned store bonus and individual employee bonus



#declare local variables
monthlySales=0 #monthly sales amount
storeAmount=0 #store bonus amount
empAmount=0 #employee bonus amount
salesIncrease=0 #percent of sales increase
prompt= 'Please enter the monthly sales amount:'
prompt2 = 'Please enter the percent of sales in decimal format:' 

#this code gets monthly sales

monthlySales = float(input(prompt))

#This code determines the storeAmount bonus

if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount = 0

#this code gets the percent increase in sales

salesIncrease = float(input(prompt2))
salesIncrease = salesIncrease / 100

#this code determines the empAmount bonus

if salesIncrease >= .05:
    empAmount = 75
elif salesIncrease >= .04:
    empAmount = 50
elif salesIncrease >= .03:
    empAmount = 40
else:
    empAmount = 0

#this code prints the store bonus information
print('The store bonus amount is $', storeAmount)
print('The employee bonus amount is $', empAmount)

if (storeAmount == 6000) and (empAmount == 75):
    print('Congrats! You have reached the highest bonus amounts possible!')
    

import math
#print the inputs that the users see when they first run the program
#Get their input on whether they want to calcuate investment or bond
  
print("Investment - to calculate the amount of interest you'll earn on investment")
print("Bond - to calculate the amount you'll have to pay on a home loan")
#make sure to add the .lower function to take in any any change in capitals
selection=input("Enter either 'Investment' or 'Bond' to proceed: ").lower()
#if they choose investment we will ask them for the following inputs

if selection=="investment": 
  amount=int(input("What is the amount you want to invest?"))
  interest_rate=int(input("What is the interest rate?"))
  interest_rate=interest_rate/100
  years=int(input("For how many years would you like to invest?"))
  interest=input("Kind of interest: simple or compound:")
#if choosen simple interest, we calculate based on the given formula
#then print the final amount

  if interest=="simple":
    final_amount1=amount*(1+interest_rate*years)
    print(f"Your final amount is £{final_amount1}")
#if choosen compound interest, we calculate based on the given formula
#then print the final amount
    
  elif interest=="compound":
  #round off the final amount to 2 decimal places
    final_amount2=round(amount*math.pow(1+(interest_rate),years),2)
    print(f"Your final amount is £{final_amount2}")
#if they choose bonds instead of investments, we will ask them for the following inputs
if selection=="bond":
  value=int(input("What is the present value of the house?"))
  interest_rate=int(input("What is the annumal interest rate?"))/100/12
  months=int(input("For how many months would you like to pay the bond?"))
#now calculate monthly payment based on the given formula and round it to 2 decimal places
  amount_payable=round((interest_rate*value)/(1-(1+interest_rate)**(-months)),2)
 #print the final amount 
  print(f"The amount you will need to pay per month is £{amount_payable}")

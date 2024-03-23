# holiday.py
city_flight = input("What city will you fly to? ")
num_nights = int(input("How many nights will you stay? ")) 
rental_days = int(input("How many days will you rent a car? "))

#lets define the hotel cost which is basically the number of nights times the hotel price per night
def hotel_cost(num_nights):
 cost_per_night = 100 
 return num_nights * cost_per_night

#now lets define plane cost, which the price from the city they are flying from. 

def plane_cost(city_flight):
  if city_flight == "New York":
      return 500
  elif city_flight == "London":
      return 600 
  elif city_flight == "Tokyo":
      return 800
  else:
      return 400

#now lets define rental car cost, which is the number of days they will rent a car times the rent

def car_rental(rental_days):
 daily_rental_cost = 50
 return rental_days * daily_rental_cost

#Lets difine holiday cost using all the costs above
def holiday_cost(city_flight, num_nights, rental_days):
 
 total_cost= hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
 return total_cost
  # Calculate and print out all the details about the holiday

total_holiday_cost = holiday_cost(city_flight, num_nights, rental_days)

print("Holiday details:")
print(f"City: {city_flight}")  
print(f"Number of nights: {num_nights}")
print(f"Rental days: {rental_days}")
print(f"Hotel cost: ${hotel_cost(num_nights)}")
print(f"Plane cost: ${plane_cost(city_flight)}")
print(f"Car rental cost: ${car_rental(rental_days)}")
print(f"Total cost: ${total_holiday_cost}")

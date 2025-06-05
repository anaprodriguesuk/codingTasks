print("To calculate the total cost of your holiday: ") 
print() 

# Getting the user to input information about the holiday, numbers are converted to integers to be calculated.

city_flight=input("Please enter the city you are flying to: ")
num_nights=int(input("Please enter the number of nights you will stay at a hotel: "))
rental_days=int(input("Please enter the number of days you will rent a car: "))


'''defining a function to calculate de hotel total cost, the function returns the numbers of night multiplied for the chosen price 59.90.
In calculating and printing out the total price, the 'round' function has been used to reduce the decimal numbers.'''
def hotel_cost(num_nights):               
    return float(num_nights * 59.90)      
total_hotel = round(hotel_cost(num_nights),2) 
print(f"The total cost of the hotel is: £ {total_hotel} ")   


'''Defining a function to calculate the plane cost using if/else statement
to choose the prices of the city flight the user will input'''
def plane_cost(city_flight):
    if city_flight == "London":
        price = float(89.90)
    elif city_flight == "Edinburg":
        price= float(99.90)
    else:
        price= float(120.90)
    return price            
total_flight=plane_cost(city_flight)
print(f"The total cost of the flight is: £ {total_flight} ")



''' Defining a function to calculate the rental total cost
that returns the days of rental multiplied by the chosen price 29.90'''
def car_rental(rental_days):
    return float(rental_days * 29.90)
total_car=round(car_rental(rental_days),2)
print(f"The total cost of the car rental is: £ {total_car} ")


# Defining a function to calculate the total holiday cost that returns in the sum of all functions created.
def holiday_cost(hotel_cost,plane_cost,car_rental):
    return hotel_cost(num_nights) + plane_cost(city_flight)+ car_rental(rental_days)
    
    
# Calling the function that calculates the total holiday price to print it out.  
totalholiday_cost= round(holiday_cost(hotel_cost,plane_cost,car_rental,),2)
print(f"The total cost of your holiday is: £ {totalholiday_cost}")
    







    








    




    
    
    
    


    



   

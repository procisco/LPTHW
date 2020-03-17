# assign the value of 100 to the variable cars
cars = 100
# assign the value of 4.0 to the variable space_in_a_car
space_in_a_car = 4.0
# assign the value of 30 to the variable drivers
drivers = 30
# assign the value of 90 to the variable passengers
passengers = 90
# assign the result of cars minus drivers to variable cars_not_driven
cars_not_driven = cars - drivers
# assign the value of drivers to the variable cars_driven
cars_driven = drivers
# assign the result of cars_driven multiplied by space_in_a_car to the variable carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
# assign the result of passengers divided by cars_driven to average_passengers_per_car
average_passengers_per_car = passengers / cars_driven


# display the number of cars available on the screen
print("There are", cars, "cars available.")
# display the nubmer of drivers available on the screen
print("There are only", drivers, "drivers available.")
# display the number of cars not driven on the screen
print("There will be", cars_not_driven, "enpty cars today.")
# disply the number of people that can be transported on the screen
print("We can transport", carpool_capacity, "people today.")
#  display the number of passengers we have today on the screen
print("We have", passengers, "passengers to carpool today.")
# display the number of passengers per car on the screen
print("We need to put about", average_passengers_per_car, "passengers in each car.")

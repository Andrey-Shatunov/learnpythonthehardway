# quantity cars
cars = 100
# variables space car
space_in_a_car = 4
#variables drivers
drivers = 30
#variables passengers
passengers = 90
#variables cars without drivers
cars_not_driven = cars - drivers
# variables cars with drivers
cars_driven = drivers
# capacity of car
carpool_capacity = cars_driven * space_in_a_car
# 
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

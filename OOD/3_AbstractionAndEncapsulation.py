# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 10:46:56 2018

The Four Pillars of OOP in Python 3 for Beginners
Created by Febin George
EXERCISE - ABSTRACTION AND ENCAPSULATION
Similar to a library management system, write a program to provide layers of 
abstraction for a car rental system.
Your program should perform the following:
1. Hatchback, Sedan, SUV should be type of cars that are being provided for rent
2. Cost per day:
Hatchback - $30
Sedan - $50
SUV - $100
3. Give a prompt to the customer asking him the type of car and the number of 
days he would like to borrow and provide the fare details to the user.

@author: Nirav Modi
"""

class CarRental:
    
    def __init__(self):
        self.carFare = {'Hatch': 30, 'Sedan': 50, 'SUV': 100}
    
    def displayFareDetails(self):
        print("Cost Per Day: ")
        print("Hatch: $", self.carFare['Hatch'])
        print("Sedan: $", self.carFare['Sedan'])
        print("SUV: $", self.carFare['SUV'])
    
    def provideFareDetails(self, carType, days):
        return self.carFare[carType]*days

class Customer:
    
    def requestCar(self):
        carType = self.requestCarType()
        days = self.requestDays()
        return carType, days
        
    def requestCarType(self):
        print("Please enter the type of car you want to rent? Hatch, Sedan, or SUV")    
        userCarChoice = input()
        return userCarChoice
        
    def requestDays(self):
        print("Please enter how many days you want to rent?")
        userDaysChoice = int(input())
        return userDaysChoice
       
    
customer = Customer()
carRental = CarRental()

while(1):
    print("Enter 1 to display fare details")
    print("Enter 2 to rent a car")
    print("Enter 3 to exit")
    userChoice = int(input())
    
    if userChoice == 1:
        carRental.displayFareDetails()
    elif userChoice == 2:
        carType, days = customer.requestCar()
        totalFare = carRental.provideFareDetails(carType, days)
        print("The total Fare is", totalFare)
    elif userChoice == 3:
        quit()


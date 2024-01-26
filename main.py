# Author: Minh Nguyen
# This program is to help the user analyze and visualize your monthly expenses.
# Assuming the user has their best behavior.

import matplotlib.pyplot as plt
import numpy as np

expenses={}

load=input("Do you want to load your data from the file 'expenses.csv'? (y/n) ").strip().lower()

count=0
done=0
while(not done):
    if (count==3):
        print("The user has given invalid inputs for 3 times. Skip this step automatically.\n")
        done=1
    
    if (load=='y' or load == 'yes'):
        file=open("expenses.csv")
        unneeded_header=file.readline()
        for line in file:    
            linelist=line.strip().split(",") 
            expenses[linelist[0]]=float(linelist[1])
        done=1
    elif (load=='n' or load == 'no'):
        done=1
        
    else:
        count+=1
        print("Invalid input, please try again.\n")
        load=input("Do you want to load your data from the file 'expenses.csv'? (y/n)").strip().lower()

def menu():
    print("\n1. Add a new expense \n\
2. Remove an expense \n\
3. Print all expense\n\
4. Give a basic report of expenses \n\
0. Quit\n")

def addExpense():
    category=input("What is the category of the expense? ").strip()
    amount=float(input("What is the amount of that category? "))
    expenses[category]=amount


def removeExpense():
    if (len(expenses)>0):
        num=int(input("\nWhat is the number of the expense that you want to remove? ")) - 1
        
        while (num<0 or num>len(expenses)):
            print("\nInvalid input.\n")
            num=(int(input("\nWhat is the number of the expense that you want to remove? "))) - 1
        
        expenseTobeRemoved=list(expenses.keys())[num]
        expenses.pop(expenseTobeRemoved)
        if (expenseTobeRemoved not in expenses.keys()):
            print("\nThe expense of {} was removed.\n".format(list(expenses.keys())[num]))
        else:
            print("\nFail to remove the expense.\n")
    else:
        print("\nThere is no expense to be removed.")    


def printExpenses():
    if (len(expenses)==0):
        print("\nThere is no expense to print.\n")
        return
    
    print("\nHere is the list of your expenses:")
    counter=1
    for key, value in expenses.items():
        print("{}. {}: ${:.2f} ".format(counter,key,value))
        counter+=1

def report():
    if (len(expenses)==0):
        print("\nThere is no expense to report.\n")
        return
    
    printExpenses()
    
    total=0.0
    labels=list(expenses.keys())
    values=list(expenses.values())
    sizes=[]

    for value in values:
        total += value

    for value in values:
        size=value/total * 100
        sizes.append(size)

    max_index=0
    min_index=0
    
    for i in range(len(values)):
        if (values[i]>values[max_index]):
            max_index=i
        if (values[i]<values[min_index]):
            min_index=i
    
    ratio=values[max_index]/values[min_index]
    print("\n\nHere is some comments about the expenses:")
    print("\nThe biggest expense is on {}, which is worth ${:.2f}.".format(labels[max_index],values[max_index]))
    print("\nThe smallest expense is on {}, which is worth ${:.2f}.".format(labels[min_index],values[min_index]))
    print("\nThe biggest expense is {:.2f} times greatest than the smallest expense.".format(ratio))
    
    print("\nThe pie chart of all expenses is displayed or saved. :)\n")
    

    fig=plt.figure(num=1, clear=True)
    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()

        
    plt.pie(sizes, labels=labels, autopct='%1.2f%%', startangle=90)
    plt.axis('equal')
        
    fig.canvas.draw()
    plt.pause(5)
    fig.savefig('fig.png')
    
menu()
option =int(input("Select an option (from 0 to 4): "))

while (option in range(5)):

    if (option==1):
        addExpense()
        menu()
        option =int(input("Select an option (from 0 to 4): "))
    
    elif (option==2):
        removeExpense()
        menu()
        option =int(input("Select an option (from 0 to 4): "))

    elif (option==3):
        printExpenses()
        menu()
        option =int(input("Select an option (from 0 to 4): "))

    elif(option==4):
        report()
        menu()
        option =int(input("Select an option (from 0 to 4): "))
        
    elif (option==0):
        print("Bye bye XD !!!")
        break

    else:
        print("Your input {} is invalid.".format(option))
        option =int(input("Select an option (from 0 to 4): "))

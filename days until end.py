"""
Created on Thu Feb 18 16:01:34 2021

@author: matte
"""
import sys
print("what month is it(integer form)?")#input what month
month=input()
print("what day is it(integer form)?")#input what day
day=input()

#make the strings ints
month=int(month)
day=int(day)

#calendar booleans to get the week
if month==1 and 24<=day<=30:
    week=1
elif (month==1 and day==31) or (month==2 and day<=6):
    week=2
elif month==2 and 7<=day<=13:
    week=3
elif month==2 and 14<=day<=20:
    week=4
elif month==2 and 21<=day<=27:
    week=5
elif (month==2 and day==28) or (month==3 and day<=6):
    week=6
elif month==3 and 7<=day<=13:
    week=7
elif month==3 and 14<=day<=20:
    week=8
elif month==3 and 21<=day<=27:
    week=9
elif month==3 and 28<=day<=31 or month==4 and day<=3:
    week=10
elif month==4 and 4<=day<=10:
    week=11
elif month==4 and 11<=day<=17:
    week=12
elif month==4 and 18<=day<=24:
    week=13
elif month==4 and 25<=day<=30 or month==5 and day==1:
    week=14
elif month==5 and 2<=day<=8:
    week=15
elif month==5 and 9<=day<=15:
    week=16
else: 
    print("That date is invalid for the spring 2021 semester")
    sys.exit()#program aborts
print()
print("It is week",week)#reads out the week
print()
y=int(week)#just to make sure y is asigned to an integer and not a string
def day_of_the_week(month,day): #assigns a day of the week to a certain date sunday==1...saturday==7
    if month==1:
        q=((day+5)%7)
        if q==0:
            return 7
        else:
            return q
    if month==2:
        q=((day+1)%7)
        if q==0:
            return 7
        else:
            return q
    if month==3:
        q=((day+1)%7)
        if q==0:
            return 7
        else:
            return q
    if month==4:
        q=((day+4)%7)
        if q==0:
            return 7
        else:
            return q
    if month==5 and 1<day<=14:
        q=((day+6))%7
        if q==0:
            return 7
        else:
            return q
    else:
        print("that date is invalid, how did you get this far?")
        sys.exit()
q=int(day_of_the_week(month,day))#i just wanted to thank q with a namesake
def day_alpha(q):
    if q==1:
        x="Sunday"
    elif q==2:
        x="Monday"
    elif q==3:
        x="Tuesday"
    elif q==4:
        x="Wednesday"
    elif q==5:
        x="Thursday"
    elif q==6:
        x="Friday"
    elif q==7:
        x="Saturday"
    else:
        x="seriously, how did you get this far?"
    return x
print("The day of the week today is",day_alpha(day_of_the_week(month,day)))
def how_many_days_left(q,y):
        z=111-((y-1)*7)-(q)#111 days including the first sunday
        return z
print("There are",how_many_days_left(q,y), "days left in the semester.")
#encouraging messages
if how_many_days_left(q,y)>30:
    print("stay strong!")
elif how_many_days_left(q,y)<30 and not week==16:
    print("You're close! stay strong")
elif week==16 and not how_many_days_left(q,y)==0:
    print("Finals week! Stay strong!")
elif how_many_days_left(q,y)==0:
    print("Congrats! This program is now useless!")
else:
    print("go do something else now")
    sys.exit()
    
        

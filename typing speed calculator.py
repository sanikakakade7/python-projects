import random as rand
from time import *
#here we are going to make use of time function from time module and this function gives no of seconds since 1971

#1 create list with the sentences to be typed by user
#2 now select random string from that list using choice function from random module
#3 record the start time
#4 tell the user to type taht string
#5 record end time
#6 pass all this data to error and speed functions to get no of errors and typing speed in words/second

def errors(chosen_string,user_string):
    error=0
    for i in range(len(chosen_string)):  #iterate from 0th too last character of main string
        try:
            #suppose user entered 5 charcaters and main string has 7 then at i=6 there will be an error that is recorded by except
            # again at i==7 there is error that is recorded by except and at 8 the itearation ends in this way less no of characters
            # from user string is taken as an error
            #also if main string has 3 characters and user entered 4 then that will not be counted as iteration ends at len of main string
            if chosen_string[i]!=user_string[i]:
              error=error+1

        except:
            error=error+1

    return error

def speed(start_time,end_time,user_string):
    time_delay=round(end_time-start_time,2)  #round function rounds off the value
    speed=round(len(user_string)/time_delay)
    return speed


list_of_strings=['My name is Sanika and I am in BCA 3rd year','I am going to get out of here as early as possible,probably after graduation',
'I am going to ruin these toxic peoples lives soon']

chosen_string=rand.choice(list_of_strings)

print(chosen_string)

start_time=time()
user_string=input("type the above string:\n")
end_time=time()

print('Errors:\n',errors(chosen_string,user_string))
print('Speed\n',speed(start_time,end_time,user_string),'words per second')
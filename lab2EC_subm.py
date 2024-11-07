"""
Extra Credit
CIS 40 Lab 2.2 Problem 3 - Converting Minutes to Seconds

The times given are in minutes: 8:15 per mile means 8 minutes and 15 seconds per mile
7:12 per mile means 7 minutes and 12 seconds per mile
It's simplest to add up all the seconds, then add up all the minutes
(this part should be done by the program, NOT pre-calculate it manually and then put it in a constant in the program),
then add to the starting time.
Then adjust for any minutes or seconds above 60.
However, there is a more elegant way by using two types of division operators - floor // and modulus % divisions.
Your script should not use any Python syntax beyond what we've covered so far.
"""

runTimes = (3*(7*60+12) + 2*(8*60+15)) / 60 #Converting 3 tempo miles into seconds and 2 easy miles into seconds

#Entering time of run start xx:xx
startingHour = int(input("Enter Starting Hour: "))
startingMinutes = int(input("Enter Starting Minute: "))

#Calculating finish time
endMinute = (runTimes + startingMinutes) % 60
endHour = startingHour + (runTimes + startingMinutes) // 60

print("\nYou will finish at %d:%d" %(endHour, endMinute))

#test
#print(runTimes, endMinute, endHour)

"""
C:\PycharmProjects\.venv\Scripts\python.exe C:\PycharmProjects\pythonProject\lab2EC_subm.py 
Enter Starting Hour: 7
Enter Starting Minute: 52

You will finish at 8:30

Process finished with exit code 0
"""
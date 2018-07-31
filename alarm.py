#!/usr/bin/python

import sys

current_time_str = raw_input("What is the current time (in hours 0-23)? ")
wait_time_str = input("How many hours do you want to wait? ")

print(type(current_time_str))

try:
	current_time_int = int(current_time_str)
	print(current_time_int)
	wait_time_int = int(wait_time_str)


	final_time_int = current_time_int + wait_time_int
	print(final_time_int)

	final_answer = final_time_int % 24

	print("The time after waiting is: " + str(final_answer))

except ValueError, NameError:
	print("please enter a valid number.")



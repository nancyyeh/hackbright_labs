"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

def calculator_run():
	while True: 
		input_string = input('Enter your forumula here: ')
		tokens = input_string.split(' ')

		if tokens[0] == "q":
			print ('Ending session.')
			break
		if len(tokens) == 1:
			print ("Please insert a valid equation.")
		elif len(tokens) > 3:
			print ("You have inserted too many variables.")

		elif len(tokens) == 3:
			formula = tokens[0]
			num1 = float(tokens[1])
			num2 = float(tokens[2])
			if formula == "+":
				print (add(num1, num2))
			elif formula == "-":
				print (subtract(num1, num2))
			elif formula == "*":
				print (multiply(num1, num2))
			elif formula == "/":
				print (divide(num1, num2))
			elif formula == "mod":
				print (mod(num1, num2))
		elif len(tokens) == 2:
			formula = tokens[0]
			num1 = float(tokens[1])
			if formula == "square":
				print (square(num1))
			elif formula == "cube":
				print (cube(num1))
			elif formula == "pow":
				print (power(num1, num2))

calculator_run()
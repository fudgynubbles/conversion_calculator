#USEFUL CALCULATOR BITCHES!!!
import currency
import miles_km
#prompt calculator type
def whatyouwant():
	calclist = ['1: Currency Converter', '2: Miles and Kilometers', '3: Centimeters and Inches', '4: Pounds and Kilograms', 'Exit']
	for i in calclist:
		print i
	calctype = raw_input("What kind of calculator would you like? \n> ").lower()
	if calctype == "done" or calctype == "exit":
		print "Goodbye"
	elif calctype == "1":
		currency.currency()
	elif calctype == "2":
		miles_km.miles_km()
	elif calctype == "3":
		cm_in()
	elif calctype == "4":
		lbs_km()


		
def cm_in():
	print "Enter '1' for cm to in, or '2' for in to cm"
	input = raw_input("> ").lower()
	if input == "1":
		print "Type a number to convert \n'back' goes to previous menu \n'done' goes to root menu"
		print "-" * 10
		cm_to_in()
	elif input == "2":
		print "Type a number to convert \n'back' goes to previous menu \n'done' goes to root menu"
		print "-" * 10
		in_to_cm()
	elif input == "done" or input == "exit": 
		whatyouwant()
	else:
		print "Try again, dummy"
		cm_in()
		

whatyouwant()
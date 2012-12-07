


# Select calculator options for converting miles and kilometers		
def miles_km():
	print "Enter '1' for mi to km, or '2' for km to mi"
	input = raw_input("> ").lower()
	if input == "1":
		print "Type a number to convert \n'back' goes to previous menu \n'done' goes to root menu"
		print "-" * 10
		miles_to_km()
	elif input == "2":
		print "Type a number to convert \n'back' goes to previous menu \n'done' goes to root menu"
		print "-" * 10
		km_to_miles()
	elif input == "done" or input == "exit":
		import project2
		project2.whatyouwant()
	else:
		print "\nSay '1', '2', or 'done'\n"
		miles_km()

# Selection 1: convert miles to kilometers		
def miles_to_km():
	number = raw_input("Enter Miles \n> ")
	if number == "exit" or number == "done":
		import project2
		project2.whatyouwant()
	elif number == "back":
		miles_km()
	else:
		result = float(number) * 1.61
		print "\n%s miles is equal to %s kilometers.\n" % (str(number), str(result))
		miles_to_km()

# Selection 2: convert kilometers to miles			
def km_to_miles():
	number = raw_input("Enter Kilometers \n> ")
	if number == "exit" or number == "done":
		import project2
		project2.whatyouwant()
	elif number == "back":
		miles_km()
	else:
		result = float(number) * 0.62
		print "\n%s kilometers is equal to %s miles.\n" % (str(number), str(result))
		km_to_miles()
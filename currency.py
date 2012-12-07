# Currency converter


def currency():
	print "Enter '1' for USD to TWD, or '2' for TWD to USD"
	input = raw_input("> ").lower()
	if input == "1":
		print "Type a number to convert \n'back' goes to previous menu \n'done' goes to root menu"
		print "-" * 10
		usd_to_twd()
	elif input == "2":
		print "Type a number to convert \n'back' goes to previous menu \n'done' goes to root menu"
		print "-" * 10
		twd_to_usd()
	elif input == "done" or input == "exit":
		import project2
		project2.whatyouwant()
	else:
		print "\nSay '1', '2', or 'done'\n"
		currency()


def usd_to_twd():
	print "Enter USD amount"
	number = raw_input("> ")
	if number == "done" or number == "exit":
		import project2
		project2.whatyouwant()
	elif number == "back":
		currency()
	else:
		try:
			x = float(number)
			if True:
				result = float(number) * 29.0
				print "\nUS$%s is equal to NT$%s\n" % (str(number), str(result))
				usd_to_twd()
		except:
			print "Not a number, dummy!"
			usd_to_twd()

		
def twd_to_usd():
	print "Enter TWD amount"
	number = raw_input("> ")
	if number == "done" or number == "exit":
		import project2
		project2.whatyouwant()
	elif number == "back":
		currency()
	else:
		try:
			x = float(number)
			if True:
				result = float(number) * 0.030
				print "\nNT$%s is equal to US$%s\n" % (str(number), str(result))
				twd_to_usd()
		except:
			print "Not a number, dummy!"
			twd_to_usd()

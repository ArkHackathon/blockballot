from park.park import Park
park= Park('13.91.88.132',
	4100,
	'fcd6189151cfa5190f1c238f0928cd178341554a1b0d82de2ac8ddda957362c2',
	'1.1.1'
	)

with open('addresses.txt', 'r') as ins:
	array=[]
	for line in ins:
		array.append(line)
for i in array:
	transaction = park.transactions().create('i', '1', 'ML875z91DK4v97CP5BrE6TBejKwaNFAUVV', 'secret', 'second secret')
	#The secret will be entered upon running the program
#check transactions
transaction(self, ML875z91DK4v97CP5BrE6TBejKwaNFAUVV)

def fukboi():
	a = int(input("Enter the amount you make before taxes: "))

	b = [.02,.04,.06,.08,.1,.12,.14,.16,.18,.20]

	#Scenario One
	a1 = a - (a*.25)
	Case1 = []
	for i in b:
		a2 = a1 - (a*i) 
		Case1.append(a2)

	#Scenario Two
	Case2 = []
	for i in b:
		f = a - (a*i)
		Case2.append(f)
	for i in Case2:
		i -= (.25*i)

	print(Case1)
	
	print(case2)


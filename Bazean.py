def main():

	file_1 = open("EagleFord_Production.txt","r",encoding = "latin-1")
	file_2 = open("EagleFord_Well Meta.txt","r",encoding = "latin-1")

	Content_1 = []
	for line in file_1:
		a = file_1.readline()
		a = a.strip()
		Content_1.append(a)

	Content_2 = []
	for line in file_2:
		a = file_2.readline()
		a = a.strip()
		Content_2.append(a)

	print(Content_1)

main()
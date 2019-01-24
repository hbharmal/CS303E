def main():

	file_1 = open("EagleFord_Production.txt","r")
	file_2 = open("EagleFord_Well Meta.txt","r")

	Content_1 = []
	for line in file_1:
		Content_1.append(file_1.readline())

	Content_2 = []
	for line in file_2:
		Content_2.append(file_2.readline())

	print(len(Content_1))
	print(len(Content_2))

main()
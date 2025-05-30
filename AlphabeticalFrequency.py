inputstring = "aaabbbccccdddddddddd"
numbers = []
letters = []
covered = []	
	
def solution(inputstring):
	letters = sorted(inputstring)
	for i in range(len(letters)):
		if letters[i] not in covered:
			covered.append(letters[i])
			frequency = letters.count(letters[i])
			numbers.append(frequency)	
		if letters[i] in covered:
			continue
	print("This is letters", letters)
	print("This is numbers", numbers)
	result = True
	for i in range (len(numbers) -1):
		if numbers[i] < numbers[i+1]: 
			result = False
			break
	print (result)	
	return result

solution(inputstring)

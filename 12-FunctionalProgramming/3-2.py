sentence = "I completely agree with you"

splited_sentence = sentence.split()

result = list(map(lambda word: len(word), splited_sentence))

print(f'No of letters in words: {result}')
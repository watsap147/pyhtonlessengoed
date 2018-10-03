sentence = input("What is your sentence? ")
sentence_list = sentence.split()
sentence_listlen = len(sentence_list)
sentence_25 = round(sentence_listlen * 0.25)
sentence_75 = round(sentence_listlen * 0.75)
sentence_percentage = sentence_list[sentence_25 : sentence_75]
print(" ".join(sentence_percentage))

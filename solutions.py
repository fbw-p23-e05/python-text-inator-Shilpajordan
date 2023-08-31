## Task
text = input('Enter the word: ')
#print(text[-1:])

if text[-1:]=='a' or text[-1:]=='e' or text[-1:]=='i' or text[-1:]=='o' or text[-1:]=='u':
    print(text + '-inator',str(len(text)) + '000')

else:
    print(text + 'inator',str(len(text)) + '000')   
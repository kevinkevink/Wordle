import matplotlib.pyplot as plt

guessesFile = open('/Users/kevinhutchins/Other/fun/WinterBreak2021/wordle/allowed-guesses.txt', 'r')
answersFile = open('/Users/kevinhutchins/Other/fun/WinterBreak2021/wordle/possible-answers.txt', 'r')
guesses = guessesFile.read().split()
answers = answersFile.read().split()

results = {}
counter = 0
for i in guesses:
    counter = counter + 1
    temp = " guesses out of "
    print(counter, temp, len(guesses))
    count = 0
    letters = list(dict.fromkeys(list(i)))
    for word in answers:
        wordLetters = list(dict.fromkeys(list(word)))
        for l in letters:
            for w in wordLetters:
                if(l == w):
                    count = count + 1
    results[i] = count / len(answers)
final =dict(reversed(sorted(results.items(),key= lambda x:x[1])))
print("Top Five:")
print(list(final.items())[0])
print(list(final.items())[1])
print(list(final.items())[2])
print(list(final.items())[3])
print(list(final.items())[4])

#with open('/Users/kevinhutchins/Desktop/wordle/output.txt', 'w') as f:
#    for key,value in final.items():
#       f.write('%s %s\n' % (key, value))


plt.bar(final.keys(), final.values(), color='g')
plt.show()

import random
lst_of_words = ['python', 'java', 'kotlin', 'javascript', 'hangman', 
                'programming', 'developer', 'function', 'variable', 
                'condition', 'loop', 'array', 'string',
                'integer', 'boolean', 'dictionary', 'tuple', 
                'set', 'exception', 'module', 'package',
                'algorithm', 'data', 'structure', 'object',
                'class', 'method', 'inheritance', 'polymorphism',
                'encapsulation', 'abstraction', 'interface', 'implementation',
                'compilation', 'interpretation', 'syntax', 'semantics',
                'debugging', 'testing', 'deployment', 'version',
                'repository', 'branch', 'commit', 'merge', 'conflict',
                'pull', 'request', 'issue', 'feature', 'bug',
                'performance', 'optimization', 'scalability', 'security']
word = random.choice(lst_of_words)
word_completion = '_' * len(word)
guessed = False
guessed_letters = []
tries = len(word)
print("Welcome to Hangman!")
print("Try to guess the word before you run out of tries.")
print(word_completion)
print(f'It is {len(word)} letters')
while not guessed and tries > 0:
    choice = input('Word or letter?').lower()
    if choice == 'letter':
        letter = input("Please enter a letter: ").lower()
        if letter not in 'abcdefghijklmnopqrstuvwxyz' or len(letter) != 1:
            print("Invalid input. Please enter a single letter.")
            continue
        if letter in guessed_letters:
            tries -= 1
            print('Idiot')
            print(f"You have {tries} tries left.")
            continue
        guessed_letters.append(letter)
        if letter in word:
            for i in range(0,len(word)):
                if word[i] == letter:
                    word_completion = list(word_completion)
                    word_completion[i] = letter
                    word_completion = ''.join(word_completion)
                    print(word_completion)
                    if '_' in list(word_completion):
                        guessed = False
                    else:
                        guessed = True
        else:
            print(f'{letter} is not in the word')
            tries -= 1
    elif choice == 'word':
        wordle = input('Enter the word ').lower()
        if wordle == word:
            guessed = True
        else:
            print('Wrong word!')
            tries -= 1
    else:
        print('Invalid Input')
if guessed:
    print('You win!')
else:
    print('You lose!')
print(word)
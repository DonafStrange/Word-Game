import random
import inflect
import os
import string
global lives
global tree
def whole():
    global user_letter
    global tree
    def get_valid_word():
        with open('//home//donaf//Downloads//Game//chemo.txt') as f:
            lines = f.readlines()
            f.close()
            line=random.choice(lines)
            spil = line.split()
            length=len(spil)
            lent=True
            while (line == "\n" or length<0 or lent<3):
                line=random.choice(lines)
                spil = line.split()
                length=len(spil)
                if (line == "\n" or length<3):
                    continue
                else:
                    word=spil[0]
                    lent=len(word)
                    if (lent<3):
                        continue
                    else:
                        word=spil[0]
                        lent=len(word)
                while '-' in word or "'" in word:
                    line=random.choice(lines)
                    spil = line.split()
                    length=len(spil)
                    if (line == "\n" or length<0 or lent<3):
                        continue
                    else:
                        word=spil[0]
                        lent=len(word)
        return word.upper(),line,lent;

    def hangman():
        global user_letter
        word,line,lent = get_valid_word()
        spil = word.split()
        word_letters = set(word)
        alphabet = set(string.ascii_uppercase)
        used_letters = set()

        lives = 9

        while len(word_letters) > 0 and lives > 0:
            global tree
            print( lives, 'lives remaining and you have used these ..: ', ' '.join(used_letters))
            print("HINT: __", end = '')
            for dela in spil:
                print(dela[0],"And",dela[lent-1])
            word_list = [letter if letter in used_letters else '-' for letter in word]
            print('Current word: ', ' '.join(word_list))
            print('Is it okay..? To change this word press  "/" ')
            user_letter = input('Guess a letter: ').upper()
            if(user_letter=='/'):
                break

            else:
                pass

            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                    print('Great!')

                else:
                    lives = lives - 1
                    print('\n Man..,', user_letter, 'This letter is not in the word.')

            elif user_letter in used_letters:
                print('\n Be careful..')

            else:
                lives = lives - 1
                print('Be Careful..')

        if lives == 0:
            print('Ohh Man ', word,'You should work more...?')
            print(line)

        elif user_letter=='/':
            print(word,' You had to guess this ')
            print(line)

        else:
            print('Great...!')
            print('"',word,'" You guessed correctly..')
            print(line)

    if __name__ == '__main__':
        hangman()

while True:
    whole()
    if(user_letter=='/'):
        continue
    else:
        print("_________________________________________________________________")
        print("                                                                 ")
        pass
    print('Wanna play again..? If Yes then Type "YES"')
    jett=input().upper()
    if (jett=='YES'):
        continue   
    else:
        print("...See you again...\n ...Have a nice day... ")
        break

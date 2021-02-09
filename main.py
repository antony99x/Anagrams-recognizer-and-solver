from itertools import permutations
import time


def anagrammiita(word):
    pp = permutations(word)
    perm_set = set()
    for i in pp:
        perm_set.add(i)
    ll = [list(i) for i in perm_set]
    ll.sort()
    if len(ll) == 1:
        print('''C'è 1 anagramma:''')
    else:
        print('Ci sono', len(ll), 'anagrammi:')
    listofliststostring(ll)


def anagrammieng(word):
    pp = permutations(word)
    perm_set = set()
    for i in pp:
        perm_set.add(i)
    ll = [list(i) for i in perm_set]
    ll.sort()
    if len(ll) == 1:
        print('There is 1 anagram:')

    else:
        print('There are ', len(ll), 'anagrams:')
    listofliststostring(ll)


def listofliststostring(lists):
    for lis in lists:
        st = "".join(lis)
        print(st)


def menuita():
    print('Benvenuto:')
    while True:
        print('0: Esci dal programma')
        print('1: Trova gli anagrammi di una parola')
        print('''2: Verifica se due parole sono anagrammi l' uno dell' altro''')
        ans = input()
        if ans == '1':
            print("Inserisci la parola di cui vuoi conoscere gli anagrammi: ")
            parola = input()
            anagrammiita(parola)
        if ans == '2':
            print("Inserisci la prima parola: ")
            word1 = input()
            print("Inserisci la seconda parola: ")
            word2 = input()
            checkanagramsita(word1, word2)
        if ans == '0':
            break
        if ans != '0':
            if ans != '1':
                if ans != '2':
                    print("Inserire 1 o 2")
                    menuita()
    print("Grazie per aver usato il programma")
    time.sleep(4)


def menueng():
    print('Welcome:')
    while True:
        print('0: Exit the program')
        print('1: Find the anagrams of a word')
        print('2: Check if two words are anagrams of each other')
        ans = input()
        if ans == '1':
            print("Enter the word whose anagrams you want to know: ")
            parola = input()
            anagrammieng(parola)
        if ans == '2':
            print("Enter the first word: ")
            word1 = input()
            print("Enter the second word: ")
            word2 = input()
            checkanagramseng(word1, word2)
        if ans == '0':
            break
        if ans != '0':
            if ans != '1':
                if ans != '2':
                    print("Enter 1 or 2")
                    menueng()
    print("Thanks for using the program")
    time.sleep(4)


def menu():
    print("Please choose your language:")
    print('1: English')
    print('2: Italian')
    ans = input()
    if ans == '1':
        menueng()
    if ans == '2':
        menuita()
    if ans != '1':
        if ans != '2':
            print("Enter 1 or 2")
            menu()


def checkanagramsita(word1, word2):
    res = True
    if len(word1) != len(word2):
        res = False
    else:
        i = 0
        while i < len(word1):
            if contaoccorrenze(word1, word1[i]) != contaoccorrenze(word2, word1[i]):
                res = False
                break
            i += 1
    if res:
        print("Le due parole sono anagrammi")
    else:
        print("Le due parole non sono anagrammi")


def checkanagramseng(word1, word2):
    res = True
    if len(word1) != len(word2):
        res = False
    else:
        i = 0
        while i < len(word1):
            if contaoccorrenze(word1, word1[i]) != contaoccorrenze(word2, word1[i]):
                res = False
                break
            i += 1
    if res:
        print("The two words are anagrams")
    else:
        print("The two words are not anagrams")


def contaoccorrenze(parola, lettera):
    cont = 0
    for i in parola:
        if i == lettera:
            cont += 1
    return cont


menu()

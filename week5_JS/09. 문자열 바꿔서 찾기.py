def solution(myString, pat):
    mystring2 = ''.join(['B' if letter == 'A' else 'A' for letter in myString])
    return 1 if pat in mystring2 else 0

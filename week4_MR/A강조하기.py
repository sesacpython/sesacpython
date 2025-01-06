def solution(myString):
    return ''.join([s.upper() if s=='A' or s=='a' else s.lower() for s in myString])
a = input()

for i in a: 
    if i in ('a', 'b', 'c', 'd', 'e', 'f', 'g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z'):
        i = i.upper()
        print(i, end='')
    else: 
        i = i.lower()
        print(i, end='')
password = ''
answer = 'swordfish'
while password != 'swordfish':
    for i in range(2):
        print('Password: ')
        password = input()
        if password == answer:
            break
    if password == answer:
        break
    print('Would you like a hint? (Y/N)')
    hintBool = input()
    print('It is a fish')
print('Access Granted')

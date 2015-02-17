def checkBobs(s):
    '''
    prints the number of times bob occurs
    takes an input string 's'
    '''
    number = 0
    for i in range(1, len(s)-1):
        if s[i-1:i+2] == 'bob':
            number += 1
    print('Number of times bob occurs is: '+ str(number))

z = checkBobs('azcbobobegghakl')
print z
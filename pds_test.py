import random, string, sys
from pdsapi import *

answer = input('This is test clear database! [y] [n] ')

if answer == 'y':
    ip = input('Input your ip ')
    port = int(input('Input your port '))
else:
    print('Breaked')
    exit()

status = 0


main = pds(ip,port)

try:
    code = main.ping()
except ConnectionRefusedError:
    print('Not connected!')
    sys.exit(1)

if main.ping() == 'PONG!':
   print('Connected!')
else:
   print('error!')
   sys.exit(1)

main.clear()
print('DB cleared')

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))


one = randomword(555)
two = randomword(555)
main.set(one,two)

if main.get(one) == two:
   print('test set_get ok!')
   status += 1
else:
   print('test set_get no!')
   sys.exit(1)

one_ren = randomword(555)
main.rename(one,one_ren)

if main.get(one_ren) == two:
   print('test rename ok!')
   status += 1
   main.clear()
else:
   print('test rename no!')
   sys.exit(1)

one = randomword(555)
two = randomword(555)
two1 = randomword(555)
two_plus = two + two1
main.set(one,two)
main.plus(one,two1)

if main.get(one) == two_plus:
     status += 1
     print('plus test ok!')
     main.clear()
else:
     sys.exit(1)

one = randomword(555)
two = randomword(555)
main.set(one,two)

if main.get(one) == two:
    main.rm(one)
    if main.get(one) == 'Key Error':
        status += 1
        print('rm test ok!')
    else:
        print('rm test no!')

if status == 4:
    print('All metods OK!')
    sys.exit(0)
else:
    print('Unit ERROR!')
    sys.exit(1)

import glob
import random
import string
import sys


def test(main):
    status = 0

    def randomword(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    one = randomword(555)
    two = randomword(555)
    main.set(one, two)

    if main.get(one) == two:
        print('test set_get ok!')
        status += 1
    else:
        print('test set_get no!')
        sys.exit(1)

    one_ren = randomword(555)
    main.rename(one, one_ren)

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
    main.set(one, two)
    main.plus(one, two1)

    if main.get(one) == two_plus:
        status += 1
        print('plus test ok!')
        main.clear()
    else:
        sys.exit(1)

    one = randomword(555)
    two = randomword(555)
    main.set(one, two)

    if main.get(one) == two:
        main.rm(one)
        if main.get(one) == 'Key Error':
            status += 1
            print('rm test ok!')
        else:
            print('rm test no!')

    main.clear()
    main.set(randomword(255), randomword(255))
    key = randomword(255)
    main.set(key, randomword(255))
    result = main.find_key(key)

    if result == 'Found':
        status += 1
        print('find_key ok!')
    else:
        print('Find_key test Error!')
        sys.exit(1)

    main.clear()
    value = randomword(255)
    main.set(randomword(255), value)
    result = main.find_value(value)
    if result == 'Found':
        status += 1
        print('find_value ok!')
    else:
        print('find_value no!')
        sys.exit(1)
    if status == 6:
        print('All metods OK!')
        sys.exit(0)
    else:
        print('Unit ERROR!')
        sys.exit(1)

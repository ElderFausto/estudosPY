# exercise 1

def ola(saudacao, nome):
    print(saudacao, nome)


ola('oi', 'elder')


# exercise 2

def soma(s1, s2, s3):
    print(s1 + s2 + s3)


soma(2, 3, 8)


# exercise 3


def div(d1, d2):
    calculo = ((d1 * d2 / 100) + d1)
    return print(calculo)


div(100, 10)


# exercise 4

def division(calc):
    if calc % 3 == 0 and calc % 5 == 0:
        return 'FizzBuzz'
    if calc % 3 == 0:
        return 'Fizz'
    if calc % 5 == 0:
        return 'Buzz'
    return calc


division(14)

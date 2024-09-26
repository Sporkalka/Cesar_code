from random import choice

en_alphabet = [chr(i) for i in range(97, 123)]
ru_alphabet = [chr(i) for i in range(1072, 1078)] + ['ё'] + [chr(i) for i in range(1078, 1104)]
incor_direction = ['Похоже ты ввёл неверную цифру, прочитай условие ещё раз.', 'Ой, не то. Попробуй снова',
                   'Введённые тобой данные не соответствуют тз. Следуй условию.']
def en_coding(txt, k):
    res = ''
    for i in range(len(txt)):
        if txt[i].isupper():
            coded_char_index = (en_alphabet.index(txt[i].lower()) + k) % 26
            res += en_alphabet[coded_char_index].upper()
        elif txt[i].islower():
            coded_char_index = (en_alphabet.index(txt[i]) + k) % 26
            res += en_alphabet[coded_char_index]
        else:
            res += txt[i]
    return res

def en_decoding(txt, k):
    res = ''
    for i in range(len(txt)):
        if txt[i].isupper():
            coded_char_index = (en_alphabet.index(txt[i].lower()) - k) % 26
            res += en_alphabet[coded_char_index].upper()
        elif txt[i].islower():
            coded_char_index = (en_alphabet.index(txt[i]) - k) % 26
            res += en_alphabet[coded_char_index]
        else:
            res += txt[i]
    return res

def ru_coding(txt, k):
    res = ''
    for i in range(len(txt)):
        if txt[i].isupper():
            coded_char_index = (ru_alphabet.index(txt[i].lower()) + k) % 33
            res += ru_alphabet[coded_char_index].upper()
        elif txt[i].islower():
            coded_char_index = (ru_alphabet.index(txt[i]) + k) % 33
            res += ru_alphabet[coded_char_index]
        else:
            res += txt[i]
    return res

def ru_decoding(txt, k):
    res = ''
    for i in range(len(txt)):
        if txt[i].isupper():
            coded_char_index = (ru_alphabet.index(txt[i].lower()) - k) % 33
            res += ru_alphabet[coded_char_index].upper()
        elif txt[i].islower():
            coded_char_index = (ru_alphabet.index(txt[i]) - k) % 33
            res += ru_alphabet[coded_char_index]
        else:
            res += txt[i]
    return res

def valid_direction(direction):
    return direction in [1, 0]
def cesar():
    print('-' * 30, 'Добро пожаловать в шифр Цезаря', '-' * 30, sep = '\n')

    direction = int(input('Введи 1 если хочешь зашифровать текст, или 0, если хочешь его расшифровать\n'))
    if not valid_direction(direction):
        error = choice(incor_direction)
        return error
    k = int(input('Введи шаг шифра\n'))

    txt = input('Введи текст\n')

    if txt[0].lower() in en_alphabet and direction == 1:
        res = en_coding(txt, k)
    elif txt[0].lower() in en_alphabet and direction == 0:
        res = en_decoding(txt, k)
    elif txt[0].lower() in ru_alphabet and direction == 1:
        res = ru_coding(txt, k)
    else:
        res = ru_decoding(txt, k)
    return res

while True:
    print(cesar())
    answer = input('Если хочешь повторить цикл напиши Да, иначе - Нет\n')
    if answer == 'Да':
        print(cesar())
    else:
        break
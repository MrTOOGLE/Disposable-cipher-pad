import secrets, sys

LETTERS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


# Создаём случайный ключ по длине равный сообщению без учёта пробелов
def getKey(message):
    key = ''
    for symbol in range(len(message)):
        key += secrets.choice(LETTERS)
    return key


# Шифруем сообщение по аналогии с шифром Виженера
def translateMessage(key, message, mode):
    translate = []
    keyIndex = 0

    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:  # Если символ найден в LETTERS ->
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex])

            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex])

            num %= len(LETTERS)  # Обработка завёртывания

            # Добаляем букву в тот регистр, который был у неё в изначальном сообщении
            if symbol.isupper():
                translate.append(LETTERS[num])
            elif symbol.islower():
                translate.append(LETTERS[num].lower())

            keyIndex += 1  # Переходим к следующему символу ключа
            if keyIndex == len(key):
                keyIndex = 0
        else:
            # Если символ не найден в LETTERS -> оставляем его без изменений
            translate.append(symbol)
    return ''.join(translate)


def main():
    # myMessage = input('Введите сообщение: ')
    myMessage = "Секретное сообщение, которое невозможно будет взломать."
    # myMessage = "Юцъамчеис ммбицрцфл, жхйесцп жгзюяшгфжш авмъл бырхлэнк."

    myMode = input("Введите:\nencrypt - для шифровки сообщения\ndecrypt - для расшифровки сообщения:\n")

    if myMode == 'encrypt':
        myKey = getKey(myMessage.replace(' ', ''))
        translated = translateMessage(myKey, myMessage, 'encrypt')
    elif myMode == 'decrypt':
        myKey = input('Введите ключ: ')
        translated = translateMessage(myKey, myMessage, 'decrypt')
    else:
        print('Неверно введено encrypt или decrypt')
        sys.exit()

    if myMode == 'encrypt':
        print(f'\nКлюч:\n{myKey}\nСообщение:\n{translated}')
    elif myMode == 'decrypt':
        print(f'\nСообщение:\n{translated}')


if __name__ == '__main__':
    main()

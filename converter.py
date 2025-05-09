ones = {
    '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
    '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'
}

ones_thousands = {
    '1': 'одна', '2': 'две'
}

teens = {
    '10': 'десять', '11': 'одиннадцать', '12': 'двенадцать', '13': 'тринадцать',
    '14': 'четырнадцать', '15': 'пятнадцать', '16': 'шестнадцать',
    '17': 'семнадцать', '18': 'восемнадцать', '19': 'девятнадцать'
}

tens = {
    '2': 'двадцать', '3': 'тридцать', '4': 'сорок', '5': 'пятьдесят',
    '6': 'шестьдесят', '7': 'семьдесят', '8': 'восемьдесят', '9': 'девяносто'
}

hundreds = {
    '1': 'сто', '2': 'двести', '3': 'триста', '4': 'четыреста',
    '5': 'пятьсот', '6': 'шестьсот', '7': 'семьсот', '8': 'восемьсот', '9': 'девятьсот'
}

orders = [
    '', 'тысяча', 'миллион', 'миллиард', 'триллион'
]

def get_plural(n, forms):
    n = abs(n) % 100
    if 11 <= n <= 19:
        return forms[2]
    n = n % 10
    if n == 1:
        return forms[0]
    elif 2 <= n <= 4:
        return forms[1]
    return forms[2]

def convert_triplet(triplet, order_index):
    result = []
    h, t, o = triplet


    if h != '0':
        result.append(hundreds[h])


    if t == '1':
        result.append(teens[t + o])
    else:
        if t != '0':
            result.append(tens[t])
        if o != '0':
            if order_index == 1:  
                result.append(ones_thousands.get(o, ones[o]))
            else:
                result.append(ones[o])

    if order_index > 0:
        number = int(triplet)
        if order_index == 1:
            form = get_plural(number, ['тысяча', 'тысячи', 'тысяч'])
        else:
            form = get_plural(number, ['миллион', 'миллиона', 'миллионов'])  
        if number != 0:
            result.append(form)

    return result

def convert_number(n):
    if n.startswith('-'):
        negative = True
        n = n[1:]
    else:
        negative = False

    n = n.lstrip('0') or '0'
    n = n.zfill(((len(n) + 2) // 3) * 3)
    triplets = [n[i:i + 3] for i in range(0, len(n), 3)]

    words = []
    for i, triplet in enumerate(triplets):
        order = len(triplets) - i - 1
        words += convert_triplet(triplet, order)

    if negative:
        words.insert(0, "минус")

    return ' '.join(words)

if __name__ == "__main__":
    while True:
        try:
            n = input("Введите число для перевода в слова или 'выход' для выхода: ")
            if n == "выход":
                break
            int(n) 
            print(n, "-->", convert_number(n))
        except ValueError:
            print("Ошибка: Неверное число!")

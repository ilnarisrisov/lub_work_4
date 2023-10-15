while True:
    try:
        the_amount = int(input('Введите сумму, которую хотите получить в банкомате(от 1 до 100000): '))
        break
    except ValueError:
        print('\nВведено, вероятно, не число. Попробуйте ввести что-нибудь другое')

print('')

def from_numbers_in_words(the_amount):
    ones = ['', 'один ', "два ", "три ", "четыре ", "пять ", "шесть ", "семь ", "восемь ", "девять "]
    teens = ["десять ", "одиннадцать ", "двенадцать ", "тринадцать ", "четырнадцать ",
             "пятнадцать ", "шестнадцать ", "семнадцать ", "восемнадцать ", "девятнадцать "]
    tens = ["", '', "двадцать ", "тридцать ", "сорок ", "пятьдесят ", "шестьдесят ", "семьдесят ",
            "восемьдесят ", "девяносто "]
    hundreds = ["", "сто ", "двести ", "триста ", "четыреста ", "пятьсот ", "шестьсот ", "семьсот ",
                "восемьсот ", "девятьсот "]

    if the_amount < 1 or the_amount > 99999:
        print('Введено неправильное число, попробуйте ввести другое')

    def work_with_thousands(the_amount):
        ones = ['', 'одна ', "две ", "три ", "четыре ", "пять ", "шесть ", "семь ", "восемь ", "девять "]
        tens = ['', "", "двадцать ", "тридцать ", "сорок ", "пятьдесят ", "шестьдесят ", "семьдесят ", "восемьдесят ",
                "девяносто "]
        hundreds = ['', 'сто ', 'двести ', 'триста ', 'четыреста ', 'пятьсот ', 'шестьсот ', 'семьсот ',
                    'восемьсот ', 'девятьсот ']


        the_final_cut = ''


        if the_amount >= 100:
            the_final_cut = the_final_cut + hundreds[the_amount // 100] + ''
            the_amount %= 100

        if the_amount > 19:
            the_final_cut = the_final_cut + tens[the_amount // 10] + ''
            the_amount = the_amount % 10

        elif the_amount >= 10 and the_amount < 20:
            the_final_cut = the_final_cut + teens[the_amount - 10] + ''
            the_amount = 0


        if the_amount == 1:
            the_final_cut = the_final_cut + 'одна тысяча '
        elif the_amount in [2, 3, 4]:
            the_final_cut = the_final_cut + ones[the_amount] + 'тысячи '
        else:
            the_final_cut = the_final_cut + ones[the_amount] + 'тысяч '

        return the_final_cut

    thousands = the_amount // 1000
    hundreds_and_ones = the_amount % 1000
    the_final_cut = ''

    if thousands > 0:
        the_final_cut += work_with_thousands(thousands)


    the_final_cut += work_with_other_numbers(hundreds_and_ones)


    if the_amount % 10 == 1 and the_amount % 100 != 11:
        the_final_cut += "рубль"
    elif 2 <= the_amount % 10 <= 4 and (the_amount % 100 < 10 or the_amount % 100 >= 20):
        the_final_cut += "рубля"
    else:
        the_final_cut += "рублей"

    return the_final_cut

def work_with_other_numbers(the_amount):
    ones = ['', 'один ', 'два ', 'три ', 'четыре ', 'пять ', 'шесть ', 'семь ', 'восемь ', 'девять ']
    teens = ['десять ', 'одиннадцать ', 'двенадцать ', 'тринадцать ', 'четырнадцать ', 'пятнадцать ', 'шестнадцать ',
             'семнадцать ', 'восемнадцать ', 'девятнадцать ']
    tens = ['', '', 'двадцать ', 'тридцать ', 'сорок ', 'пятьдесят ', 'шестьдесят ', 'семьдесят ', 'восемьдесят ',
            'девяносто ']
    hundreds = ['', 'сто ', 'двести ', 'триста ', 'четыреста ', 'пятьсот ', 'шестьсот ', 'семьсот ',
                'восемьсот ', 'девятьсот ']

    the_final_cut = ''


    if the_amount >= 100:
        the_final_cut += hundreds[the_amount // 100] + ''
        the_amount = the_amount % 100

    if the_amount > 19:
        the_final_cut = the_final_cut + tens[the_amount // 10] + ''
        the_amount = the_amount % 10

    elif the_amount <= 19 and the_amount >= 10:
        the_final_cut += teens[the_amount - 10] + ''
        the_amount = 0

    if the_amount > 0:
        the_final_cut = the_final_cut + ones[the_amount] + ''

    return the_final_cut
 
print(from_numbers_in_words(the_amount))
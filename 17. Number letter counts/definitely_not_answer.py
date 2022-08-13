words = {0: '', 1: "one", 2: "two", 3: "three", 4: "four", 5: 'five', 6: 'six',
         7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
         13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
         17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
         30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
         80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'onethousand'}


total_str = ''


def units(number):
    return words[number]


def tens(number):
    if number > 20:
        unit = number % 10
        tens = number - unit
        count = words[tens] + units(unit)
        return count
    else:
        return words[number]


def hundreds(number):
    ten = number % 100
    hundreds = number // 100
    and_word = "and"
    count = words[hundreds] + words[100] + tens(ten)

    if ten != 0:
        count += and_word
   
    return count


for i in range(1, 1001):
    if i < 10:
        total_str += units(i)
    elif i < 100:
        total_str += tens(i)
    elif i < 1000:
        total_str += hundreds(i)
    elif i == 1000:
        total_str += words[i]

print(len(total_str))

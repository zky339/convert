def base_2to10(num):
    numLength = len(num)
    result = 0
    for i in num:
        numLength = numLength - 1
        result = result + int(i) * 2 ** numLength
    return str(result)


def base_10to2(num):
    consult = int(num)
    result = ''
    while(consult != 0):
        result = str(consult % 2) + result
        consult = int(consult / 2)
    return result


def base_10to16(num):
    consult = int(num)
    result = ''
    while(consult != 0):
        if(consult % 16 < 9):
            result = str(consult % 16) + result
        elif(consult % 16 == 10):
            result = 'A' + result
        elif(consult % 16 == 11):
            result = 'B' + result
        elif(consult % 16 == 12):
            result = 'C' + result
        elif(consult % 16 == 13):
            result = 'D' + result
        elif(consult % 16 == 14):
            result = 'E' + result
        else:
            result = 'F' + result
        consult = int(consult / 16)
    return result


def base_16to10(num):
    numLength = len(num)
    result = 0
    for i in num:
        numLength = numLength - 1
        if(i == 'A'):
            result = result + 10 * 16 ** numLength
        elif(i == 'B'):
            result = result + 11 * 16 ** numLength
        elif(i == 'C'):
            result = result + 12 * 16 ** numLength
        elif(i == 'D'):
            result = result + 13 * 16 ** numLength
        elif(i == 'E'):
            result = result + 14 * 16 ** numLength
        elif(i == 'F'):
            result = result + 15 * 16 ** numLength
        else:
            result = result + int(i) * 16 ** numLength
    return str(result)


def base_2to16(num):
    return base_10to16(base_2to10(num))


def base_16to2(num):
    return base_10to2(base_16to10(num))


print("请从以下选择要转换的模式编号：")
print("1. 2进制转化为10进制")
print("2. 10进制转化为2进制")
print("3. 2进制转化为16进制")
print("4. 16进制转化为2进制")
print("5. 10进制转化为16进制")
print("6. 16进制转化为10进制")
base = input()

print("请输入需要转换的数字：")
num = input()

if(base == '1'):
    print(base_2to10(num))
elif(base == '2'):
    print(base_10to2(num))
elif(base == '3'):
    print(base_2to16(num))
elif(base == '4'):
    print(base_16to2(num))
elif(base == '5'):
    print(base_10to16(num))
else:
    print(base_16to10(num))

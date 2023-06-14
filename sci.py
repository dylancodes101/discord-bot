def format_e(n):
    a = '%E' % n
    return convert_number(a.split('E')[0].rstrip('0').rstrip('.') + 'E' + a.split('E')[1])

def convert_number(number):
    number = float(number)
    if abs(number) >= 1e9:
        return f"{number / 1e9}b"
    elif abs(number) >= 1e6:
        return f"{number / 1e6}m"
    elif abs(number) >= 1e3:
        return f"{number / 1e3}k"
    else:
        return str(number)



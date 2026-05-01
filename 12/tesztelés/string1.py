def donuts(count: int) -> str:
    if count < 10:
        return f"Fánkok száma: {count}"
    else:
        return 'Fánkok száma: sok'

def both_ends(s: str) -> str:
    if len(s) < 2:
        return ''
    else:
        return s[:2] + s[-2:]

def fix_start(s: str) -> str:
    first_char = s[0]
    rest_of_string = s[1:]
    modified_rest = rest_of_string.replace(first_char, '*')
    return first_char + modified_rest

def mix_up(a: str, b: str) -> str:
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    return new_a + " " + new_b
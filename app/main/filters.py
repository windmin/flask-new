def peixian_danyuan(s):
    if isinstance(s, int):
        s = str(s)
    PEIXIAN_DANYUAN = {
        '1': 'A',
        '2': 'B',
        '3': 'C',
        '4': 'D',
        '5': 'E',
        '6': 'F',
        '7': 'G',
        '8': 'H',
        '9': 'I',
        '10': 'J',
        '11': 'K',
        '12': 'L'
    }
    return PEIXIAN_DANYUAN[s]
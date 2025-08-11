def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_sym(text):
    symbols = {}
    ltext = text.lower()
    for symbol in ltext:
        if symbol in symbols:
            symbols[symbol] += 1
        else:
            symbols[symbol] = 1
    return symbols

def sort_on(items):
    return items["num"]

def sorted_sym(symbols):
    sorted_symbols = []
    for sym in symbols:
        sorted_symbols.append({"sym": sym, "num": symbols[sym]})
    sorted_symbols.sort(reverse=True, key=sort_on)
    return sorted_symbols

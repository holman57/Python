def solution(prices, notes, x):
    m = 0
    for price, note in zip(prices, notes):
        token = note.split(" ")[1]
        if token == "as":
            continue
        p = float(note.split("%")[0]) * 0.01
        if token == "higher":
            m += price - (price / (1 + p))
        elif token == "lower":
            m += price - (price / (1 - p))

    return True if round(m, 7) <= round(x, 7) else False

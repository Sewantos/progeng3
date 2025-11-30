def is_correct_bracket_seq(s: str) -> bool:
    """Проверяет правильность последовательности скобок."""
    open_br = "([{"
    close_br = ")]}"
    stack = []

    for symbol in s:
        idx = open_br.find(symbol)
        if idx != -1:
            stack.append(idx)
            continue

        idx = close_br.find(symbol)
        if idx != -1:
            if not stack or stack.pop() != idx:
                return False
            continue

        raise ValueError(f"That is not a bracket: {symbol}")

    return not stack

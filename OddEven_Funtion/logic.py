def check_odd_even(number):
    try:
        val = int(number)
        return "Even" if val % 2 == 0 else "Odd"
    except (ValueError, TypeError):
        return None

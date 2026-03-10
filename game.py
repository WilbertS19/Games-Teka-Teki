def check_guess(secret, guess):
    if guess < secret:
        return "Terlalu kecil"
    elif guess > secret:
        return "Terlalu besar"
    else:
        return "Benar!"
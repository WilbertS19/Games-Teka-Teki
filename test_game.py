from game import check_guess

def test_guess_too_small():
    assert check_guess(10, 5) == "Terlalu kecil"

def test_guess_too_big():
    assert check_guess(10, 15) == "Terlalu besar"

def test_guess_correct():
    
    assert check_guess(10, 10) == "Benar!"
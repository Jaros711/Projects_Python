from plates import is_valid


def main():
    # Call test functions
    test_min_and_max()
    test_start_two_letters()
    test_middle()
    test_first()
    test_special()

# Plates may contain a max of 6 char and min2 char


def test_min_and_max():
    assert is_valid('AA') == True
    assert is_valid('ABCDEF') == True
    assert is_valid('A') == False
    assert is_valid('ABCDEFGH') == False

# Plates starts min 2 letters


def test_start_two_letters():
    assert is_valid('AA') == True
    assert is_valid('A2') == False
    assert is_valid('2A') == False
    assert is_valid('22') == False

# Numbers cannot be used in the middle of a plate


def test_middle():
    assert is_valid('AAA222') == True
    assert is_valid('AAA22A') == False

# First number cannot be 0


def test_first():
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False

# No periods, spaces, punctuaction


def test_special():
    assert is_valid('PI3.14') == False
    assert is_valid('PI!@#') == False
    assert is_valid('PI ! @#') == False


if __name__ == "__main__":
    main()

from main_r import entero_a_romano, romano_a_entero

def test_336():
    assert entero_a_romano(336) == 'CCCXXXVI'


def test_2022():
    assert entero_a_romano(2022) == 'MMXXII'


def test_1():
    assert romano_a_entero('I') == 1
    
def test_1713():
    assert romano_a_entero('MDCCXIII') == 1713

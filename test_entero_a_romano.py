import pytest
from main_r import entero_a_romano, romano_a_entero, RomanNumberError

def test_336():
    assert entero_a_romano(336) == 'CCCXXXVI'


def test_2022():
    assert entero_a_romano(2022) == 'MMXXII'


def test_1():
    assert romano_a_entero('I') == 1
    
def test_1713():
    assert romano_a_entero('MDCCXIII') == 1713

def test_romano_a_entero_restar_a_izquierda():
    assert romano_a_entero('IV') == 4
    
def test_romano_a_entero_no_repetir_mas_de_tres():
    with pytest.raises(RomanNumberError) as exceptionInfo:
        romano_a_entero('LIIII')
        assert str(excetionInfo.value) == 'No se puede repetir el valor mas de tres veces'   

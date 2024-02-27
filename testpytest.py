import pytest

def test_calcul_addition():
    # FOnction test du resultat de 2+4
    output= 2+4
    assert output==6

def test_calcule_substraction():
    # fonction teste du resultat 2-4
    output= 2-4
    assert output==-2

def test_calcul_multiplication():
    # fonction teste resultat de 3*3
    output= 3*3
    assert output==9

def test_coucou():
    # fonction test si le resultat  renvoie est helo
    output= "hello"
    assert output =="hello"

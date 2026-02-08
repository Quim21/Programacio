from QuimPerez_Escacs import tauler, peo_blanc, peo_negre, cavall_blanc, cavall_negre, generacio_tauler
def test1():
    generacio_tauler()
    assert peo_blanc(6, 0, 5, 0) is True
def test2():
    generacio_tauler()
    assert peo_blanc(6, 0, 4, 0) == True
def test3():
    generacio_tauler()
    tauler[5][0] = "[♟]"
    assert peo_blanc(6, 0, 5, 0) == False
def test4():
    generacio_tauler()
    tauler[5][1] = "[♟]"
    assert peo_blanc(6, 0, 5, 1) == True
def test5():
    generacio_tauler()
    assert peo_blanc(6, 0, 5, 1) == False
def test6():
    generacio_tauler()
    assert peo_blanc(6, 0, 7, 0) == False
def test_c1():
    generacio_tauler()
    assert cavall_blanc(0, 1, 2, 2) == True

def test_c2():
    generacio_tauler()
    tauler[2][2] = "[♟]"
    assert cavall_blanc(0, 1, 2, 2) == True

def test_c3():
    generacio_tauler()
    assert cavall_blanc(0, 1, 1, 2) == False

def test_c4():
    generacio_tauler()
    assert cavall_blanc(0, 1, 3, 8) == False

def test_c5():
    generacio_tauler()
    tauler[2][2] = "[♙]"
    assert cavall_blanc(0, 1, 2, 2) == False

def test_c6():
    generacio_tauler()
    tauler[1][1] = "[♟]"
    tauler[1][2] = "[♟]"
    assert cavall_blanc(0, 1, 2, 2) == True

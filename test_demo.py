from demo import test1, est_premier, couple_premier

def test_test1():
    assert test1() == None
def test_est_premier():
    assert est_premier(1) == False
    assert est_premier(2) == True
    assert est_premier(3) == True
    assert est_premier(4) == False
    assert est_premier(5) == True
    assert est_premier(6) == False
    assert est_premier(7) == True
    assert est_premier(8) == False
    assert est_premier(9) == False
    assert est_premier(10) == False
    assert est_premier(11) == True
    assert est_premier(12) == False
    assert est_premier(13) == True
    assert est_premier(14) == False
    assert est_premier(15) == False
    assert est_premier(16) == False
    assert est_premier(17) == True
    assert est_premier(18) == False
    assert est_premier(19) == True
    assert est_premier(20) == False

def test_couple_premier():
    assert couple_premier(10) == [(3, 5), (5, 7)]
    assert couple_premier(20) == [(3, 5), (5, 7), (11, 13), (17, 19)]
    assert couple_premier(50) == [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43)]
    assert couple_premier(100) == [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43), (59, 61), (71, 73)]


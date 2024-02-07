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
    assert est_premier(21) == False
    assert est_premier(22) == False
    assert est_premier(23) == True
    assert est_premier(24) == False
    assert est_premier(25) == False
    assert est_premier(26) == False
    assert est_premier(27) == False
    assert est_premier(28) == False
    assert est_premier(29) == True
    assert est_premier(30) == False
    assert est_premier(31) == True
    assert est_premier(32) == False
    assert est_premier(33) == False
    assert est_premier(34) == False
    assert est_premier(35) == False
    assert est_premier(36) == False
    assert est_premier(37) == True
    assert est_premier(38) == False
    assert est_premier(39) == False
    assert est_premier(40) == False
    assert est_premier(41) == True
    assert est_premier(42) == False
    assert est_premier(43) == True
    assert est_premier(44) == False
    assert est_premier(45) == False
    assert est_premier(46) == False
    assert est_premier(47) == True
    assert est_premier(48) == False
    assert est_premier(49) == False
    assert est_premier(50) == False
    assert est_premier(51) == False
    assert est_premier(52) == False
    assert est_premier(53) == True
    assert est_premier(54) == False
    assert est_premier(55) == False
    assert est_premier(56) == False
    assert est_premier(57) == False
    assert est_premier(58) == False
    assert est_premier(59) == True
    assert est_premier(60) == False
    assert est_premier(61) == True
    assert est_premier(62) == False
    assert est_premier(63) == False
    assert est_premier(64) == False
    assert est_premier(65) == False
    assert est_premier(66) == False
    assert est_premier(67) == True
    assert est_premier(68) == False
    assert est_premier(69) == False
    assert est_premier(70) == False
    assert est_premier(71) == True
    assert est_premier(72) == False
    assert est_premier(73) == True
    assert est_premier(74) == False

def test_couple_premier():
    assert couple_premier(10) == [(3, 5)]
    assert couple_premier(20) == [(3, 5), (5, 7), (11, 13)]
    assert couple_premier(50) == [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43)]
    assert couple_premier(100) == [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43), (59, 61), (71, 73)]
    assert couple_premier(200) == [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43), (59, 61), (71, 73), (101, 103), (107, 109), (137, 139), (149, 151), (179, 181)]
    assert couple_premier(300) == [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43), (59, 61), (71, 73), (101, 103), (107, 109), (137, 139), (149, 151), (179, 181), (191, 193), (197, 199)]
    assert couple_premier(400) == [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43), (59, 61), (71, 73), (101, 103), (107, 109), (137, 139), (149, 151), (179, 181), (191, 193), (197, 199), (227, 229), (239, 241), (269, 271), (281, 283)]
    assert couple_premier(500) == [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43), (59, 61), (71, 73), (101, 103), (107, 109), (137, 139), (149, 151), (179, 181), (191, 193), (197, 199), (227, 229), (239, 241), (269, 271), (281, 283), (311, 313), (347, 349), (419, 421), (431, 433), (461, 463)]

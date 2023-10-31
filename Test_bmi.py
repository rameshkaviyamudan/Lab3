import Lab2.bmi

def test_bmi_normal_weight():
    test_res = 0

    result = Lab2.bmi.calculate_bmi(1.73,57)

    assert (result == test_res)

def test_bmi_over_weight():
    test_res = 1

    result = Lab2.bmi.calculate_bmi(1.73,97)

    assert (result == test_res)

def test_bmi_under_weight():
    test_res = -1

    result = Lab2.bmi.calculate_bmi(1.73,37)

    assert (result == test_res)
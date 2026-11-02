import lab2.lab as bmi

def test_bmi_normal_weight():
    result = []
    height = 1.72
    weight = 65
    test_lab = (21.97,0)
    result = bmi.calculate_bmi(height, weight)
    assert(result == test_lab)

def test_bmi_under_weight():
    result = []
    height = 1.72
    weight = 50
    test_lab = (16.90,-1)
    result = bmi.calculate_bmi(height, weight)
    assert(result == test_lab)

def test_bmi_over_weight():
    result = []
    height = 1.72
    weight = 80
    test_lab = (27.04,1)
    result = bmi.calculate_bmi(height, weight)
    assert(result == test_lab)
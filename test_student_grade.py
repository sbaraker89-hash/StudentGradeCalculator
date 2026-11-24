from student_grade import average, grade, is_pass, valid_mark


def test_average():
    assert average([80, 90, 70]) == 80


def test_grade_s():
    assert grade(95) == "S"


def test_grade_a():
    assert grade(85) == "A"


def test_grade_b():
    assert grade(70) == "B"


def test_grade_c():
    assert grade(55) == "C"


def test_grade_d():
    assert grade(45) == "D"


def test_grade_f():
    assert grade(30) == "F"


def test_valid_mark():
    assert valid_mark(85) is True


def test_invalid_mark():
    assert valid_mark(120) is False


def test_pass():
    assert is_pass([50, 60, 70]) is True


def test_fail():
    assert is_pass([30, 35, 40]) is False
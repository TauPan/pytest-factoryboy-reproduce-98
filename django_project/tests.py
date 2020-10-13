import pytest

pytestmark = [pytest.mark.django_db]


def test_thing(thing):
    assert thing.a == 1
    assert thing.b == 2
    assert thing.sum_ is None


def test_thing_calculate(thing):
    assert thing.a == 1
    assert thing.b == 2
    assert thing.sum_ is None
    thing.calculate_sum()
    assert thing.sum_ == 3


def test_do_calculate(thing_do_calculate):
    assert thing_do_calculate.a == 1
    assert thing_do_calculate.b == 2
    assert thing_do_calculate.sum_ == 3


def test_thing_3_plus_4(thing3_plus4):
    assert thing3_plus4.a == 3
    assert thing3_plus4.b == 4
    assert thing3_plus4.sum_ == 7


def test_do_calculate_arg(thing_calculate_arg):
    assert thing_calculate_arg.a == 1
    assert thing_calculate_arg.b == 2
    assert thing_calculate_arg.sum_ == 3


def test_thing_3_plus_4_arg(thing3_plus4_arg):
    assert thing3_plus4_arg.a == 3
    assert thing3_plus4_arg.b == 4
    assert thing3_plus4_arg.sum_ == 7


def test_do_calculate_direct(do_calculate_direct):
    assert do_calculate_direct.a == 1
    assert do_calculate_direct.b == 2
    assert do_calculate_direct.sum_ == 3


def test_do_calculate_3_plus_4_direct(do_calculate_3_plus_4_direct):
    assert do_calculate_3_plus_4_direct.a == 3
    assert do_calculate_3_plus_4_direct.b == 4
    assert do_calculate_3_plus_4_direct.sum_ == 7

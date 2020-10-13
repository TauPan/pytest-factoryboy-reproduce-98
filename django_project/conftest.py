import pytest
from pytest_factoryboy import register

from django_project import factories

register(
    factories.ThingFactory)
register(
    factories.DoCalculateFactory, 'thing_do_calculate')
register(
    factories.Thing3Plus4Factory, 'thing3_plus4')
register(
    factories.ThingFactory, 'thing_calculate_arg', do_calculate=True)
register(
    factories.ThingFactory, 'thing3_plus4_arg', do_calculate=True, a=3, b=4)


@pytest.fixture
def do_calculate_direct():
    return factories.DoCalculateFactory()


@pytest.fixture
def do_calculate_3_plus_4_direct():
    return factories.Thing3Plus4Factory()

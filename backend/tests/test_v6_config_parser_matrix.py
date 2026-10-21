"""Configuration environment parser behavior across edge values."""
import pytest
from app.config import _bool, _int, _float

@pytest.mark.parametrize("value,expected", [
    ("1",True),("true",True),("TRUE",True),("yes",True),("on",True),("  true  ",True),
    ("0",False),("false",False),("no",False),("off",False),("",False),("random",False),
])
def test_v6_boolean_environment_parser(monkeypatch,value,expected):
    monkeypatch.setenv("FW_TEST_BOOL",value)
    assert _bool("FW_TEST_BOOL",not expected) is expected

@pytest.mark.parametrize("value,expected", [
    ("12",12),("0",0),("-3",-3),("not-int",7),("",7),("3.14",7),
])
def test_v6_integer_environment_parser(monkeypatch,value,expected):
    monkeypatch.setenv("FW_TEST_INT",value)
    assert _int("FW_TEST_INT",7)==expected

@pytest.mark.parametrize("value,expected", [
    ("1.25",1.25),("0",0.0),("-3.5",-3.5),("nan",float("nan")),("invalid",2.5),("",2.5),
])
def test_v6_float_environment_parser(monkeypatch,value,expected):
    monkeypatch.setenv("FW_TEST_FLOAT",value)
    actual=_float("FW_TEST_FLOAT",2.5)
    if expected != expected:
        assert actual != actual
    else:
        assert actual==expected

@pytest.mark.parametrize("name,default", [("FW_MISSING_A",True),("FW_MISSING_B",False)])
def test_v6_environment_parser_uses_default_when_unset(monkeypatch,name,default):
    monkeypatch.delenv(name,raising=False)
    assert _bool(name,default) is default

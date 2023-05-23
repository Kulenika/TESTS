import pytest
@pytest.mark.smoke
def test_mark1():
    assert True
@pytest.mark.regress
def test_mark2():
    assert True
@pytest.mark.regress
def test_mark3():
    assert True
@pytest.mark.regress
def test_mark4():
    assert True
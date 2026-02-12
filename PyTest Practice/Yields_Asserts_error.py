import pytest

@pytest.fixture(scope="function")
def pass_value():
    return 42

@pytest.fixture(scope="function")
def yields():
    return 43
    yield #pause everything after yields
    print("close browser and cookies") #run after completing everything in def test

def test(pass_value, yields):
    print("first test")
    assert pass_value == 42
    assert yields == 42

#What's Happening
#When Python sees return 43, it immediately exits the function and sends back the value 43
#The yield line below never gets executed (it's "unreachable code")
#Pytest expects fixtures with yield to actually yield a value (not return)
#Since the yield never happens, pytest throws the error: "yields did not yield a value"





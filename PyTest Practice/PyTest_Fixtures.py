import pytest

@pytest.fixture(scope="module")
def preWork():
    print("Setup Browser")

#if I enter scope = function next to .fixture
#this tells python that the test fixture
#can run as many times as needed.
#If I use module then this fixture will only run once.

#fixtures are executed first when passed through a function
#as shown below

def test_initialCheck(preWork):
    print("This is the first test")

def test_secondCheck(preWork):
    print("This is the second test")
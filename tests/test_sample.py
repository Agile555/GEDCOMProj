#I'm just here to show that Travis is set up and working
def greet():
    return 'Hello World!'

def test_greeting():
    assert greet() == 'Hello World!'
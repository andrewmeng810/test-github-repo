from app import greet


def test_greet():
    assert greet("GitHub") == "Hello, GitHub!"
    assert greet("Alice") == "Hello, Alice!"
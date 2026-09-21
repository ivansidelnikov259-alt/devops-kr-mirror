from validator import validate_email, validate_phone

# tests/test_validator.py
def test_validate_email():
    assert validate_email("test@example.com") == True
    assert validate_email("invalid") == False


def test_validate_phone_valid():
    assert validate_phone("+7 999 123-45-67") is True
    assert validate_phone("89991234567") is True


def test_validate_phone_invalid():
    assert validate_phone("123") is False
    assert validate_phone("not a phone") is False
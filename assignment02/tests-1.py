
########## MOMINA ATIF DAR P18-0030

from example1.py import check_email, check_domain

def test_username():
    data = "mona/dar07@gmail.com"

    dt = check_email(data)

    assert dt == "Invalid username. Please try again.."

def test_username2():
    data = "farwa.dar1@gmail.com"

    dt = example1.check_email(data)

    assert dt == "Valid email"

def test_domain():
    data = "farwa.dar1@gmil.com"

    dt = check_email(data)

    assert dt == "Invalid domain. Please try again"

def test_domain2():
    data = "farwa.dar1@yahoocom"

    dt = check_email(data)

    assert dt == "Invalid domain. Please try again"

def test_at():
    data = "bushra02outlook.com"

    dt = check_email(data)

    assert dt == "Invalid email. Please try again."

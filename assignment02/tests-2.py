
########## MOMINA ATIF DAR P18-0030

from example2.py import check_date 

def test_date():
    data = "2020-14-10"

    dt = check_date(data)

    assert dt == "Invalid month at: "


def test_date2():
    data = "2020-10-20"

    dt = check_date(data)
    
    assert dt = "Invalid date (future date) at: "_


def test_date3():
    data = "202-05-05"

    dt = check_date(data)

    assert dt = "Invalid format at: "


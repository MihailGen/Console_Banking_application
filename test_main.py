# from main import monyadd
from main import mony_withdr
# from main import pass_check
# from main import account_creation
# from main import transaction_from_file


# def test_monyadd():
#     assert monyadd(1,2, 6) == 3

# def test_monyadd_smallLimit():
#     assert monyadd(1, 2, 2) == 1

def test_money_too_little():
    assert mony_withdr(9, 100) == 9


def test_money_wthdrw():
    assert mony_withdr(12, 4) == 8




#
# def test_pass_check():
#     assert pass_check("zzz", "zzzz") == False
#     assert pass_check("zzz", "zzz") == True
#
# def test_account_creation():
#     assert account_creation() == True
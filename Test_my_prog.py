from main import monyadd
from main import monywithdr
from main import pass_check
from main import transaction_from_file

def test_monyadd():
    assert monyadd(1,2, 6) == 3

def test_monywithdr():
    assert monywithdr(98, 2) == 96

def test_pass_check():
    assert pass_check("zzz", "zzzz") == False


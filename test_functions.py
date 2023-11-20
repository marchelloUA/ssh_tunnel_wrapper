from ssh_tunnel_wrapper import is_positive_integer

def test_is_positive_integer():
    assert is_positive_integer('10') == True
    assert is_positive_integer('-5') == False
    assert is_positive_integer('0') == False
    assert is_positive_integer('abc') == False

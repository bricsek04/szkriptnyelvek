from lista1 import match_ends, front_x

def test_match_ends():
    assert match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']) == 3
    assert match_ends(['', 'x', 'xy', 'xyx', 'xx']) == 2
    assert match_ends(['aaa', 'be', 'abc', 'hello']) == 1

def test_front_x():
    assert front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']) == ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    assert front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']) == ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    assert front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']) == ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
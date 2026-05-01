from string1 import donuts, both_ends, fix_start, mix_up

def test_donuts():
    assert donuts(4) == "Fánkok száma: 4"
    assert donuts(9) == "Fánkok száma: 9"
    assert donuts(10) == "Fánkok száma: sok"
    assert donuts(99) == "Fánkok száma: sok"

def test_both_ends():
    assert both_ends('spring') == 'spng'
    assert both_ends('Hello') == 'Helo'
    assert both_ends('a') == ''
    assert both_ends('xyz') == 'xyyz'

def test_fix_start():
    assert fix_start('babble') == 'ba**le'
    assert fix_start('aardvark') == 'a*rdv*rk'
    assert fix_start('google') == 'goo*le'
    assert fix_start('donut') == 'donut'

def test_mix_up():
    assert mix_up('mix', 'pod') == 'pox mid'
    assert mix_up('dog', 'dinner') == 'dig donner'
    assert mix_up('gnash', 'sport') == 'spash gnort'
    assert mix_up('pezzy', 'firm') == 'fizzy perm'
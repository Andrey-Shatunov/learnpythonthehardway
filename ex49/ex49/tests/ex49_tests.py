from nose.tools import *
from ex49.parser import *

def test_parse_sentence():
    x = Parser().parse_sentence([('stop','run'),('verb','run'), ('direction','north')])
    assert_equal("player", x.subject)
    assert_equal("run", x.verb)
    assert_equal("north", x.object)

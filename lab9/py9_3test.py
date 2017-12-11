import py9_3
import pytest

class Test(object):

    def test_answer_type(self):
        assert isinstance(py9_3.num2text(1), basestring)

    def test_zero(self):
        assert py9_3.num2text(0) == 'zero'

    def test_one(self):
        assert py9_3.num2text(1) == 'jeden'

    def test_two(self):
        assert py9_3.num2text(2) == 'dwa'

    def test_three(self):
        assert py9_3.num2text(3) == 'trzy'

    def test_ValueError(self):
        with pytest.raises(ValueError):
            py9_3.num2text(4)

from application_1.models import *
import pytest
import os
from django.test import TestCase
from pytest import *


@pytest.mark.parametrize('name,function,res', [(1, 2, 3)])
def test_1(name, function, res):
    assert name + function == res

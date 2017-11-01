import pytest
from domainUptime import domainUptime as d


def test_CorrectRequetsUrl():
    status = d.requestUrl('http://sd.mte.gov.br')
    assert type(status) == str


def test_FailRequetsUrl():
    status = d.requestUrl('oisdhfaoijndjsklfank')
    assert type(status) == str

import importlib
import pytest
import csv

def read_from_csv(filename,col1,col2):
    datafile = open(filename, 'r')
    datareader = csv.reader(datafile, delimiter=',')
    data = []
    for row in datareader:
        if(row[0] != 'Level 0'):
            data.append((row[col1],row[col2]))
    return data

softness_pairs = read_from_csv('../scripts/words.csv',0,1)

@pytest.fixture(scope='session')
def RPT():
    loader = importlib.machinery.SourceFileLoader('RPT', '../scripts/RPT.py')
    spec = importlib.util.spec_from_loader(loader.name, loader)
    RPT = importlib.util.module_from_spec(spec)
    loader.exec_module(RPT)
    return RPT

@pytest.mark.parametrize('test_input,expected', softness_pairs)
def test_softness(RPT,test_input,expected):
    assert RPT.softness(test_input) == expected

import pytest
from fixture.application import Application
import importlib
import os
import pandas as pd
import numpy as np


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("C:\\Program Files (x86)\\GAS Softwares\\Free Address Book\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("excel_"):
            testdata = load_from_excel(fixture[6:])
            print("")
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_from_excel(file):
    file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data\\%s.xlsx" % file)
    raw = pd.read_excel(file, index_col=None, na_values=['NA'], usecols = "A,C:AA").values
    res = np.array(raw).tolist()
    list =[]
    for string in res:
        tmp=str(string)
        new_string = tmp.replace("[", "").replace("]", "").replace("'", "")
        list.append(new_string)
    return list





import pytest

from PYTEST.conftest import crossbrowser


@pytest.mark.usefixtures("crossbrowser")
def test_crossbrowser():
    print(crossbrowser)


    
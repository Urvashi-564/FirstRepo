import pytest

@pytest.mark.usefixtures("dataLoad")
class Test1:

    def test_profileInfo(self,dataLoad):
        print(dataLoad[1])
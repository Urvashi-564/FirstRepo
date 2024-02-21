import logging

import pytest
from PYTEST.logger_prac import PracticeLogs


@pytest.mark.usefixtures("setup")
class TestExample(PracticeLogs):

    def test_fixtureDemo(self):
        log=self.getLogger()
        log.info("i will execute steps in fixtureDemo method")
        log.debug("I am debug")
        # print("i will execute steps in fixtureDemo method")

    def test_fixtureDemo1(self):
        print("i will execute steps in fixtureDemo1 method")

    def test_fixtureDemo2(self):
        log = self.getLogger()
        log.info("i will execute steps in fixtureDemo2 method")

    def test_fixtureDemo3(self):
        print("i will execute steps in fixtureDemo3 method")

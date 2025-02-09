import time
import pytest
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from Utils import Utils as Utils
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.JavaScripDelayPage import JavaScriptDelayPage


class TestJavaScriptDelay(BaseClass):

    def test_JavaScriptDelay(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        #hp.closeCookiesWindows()
        driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(1)
        hp.clickBtnJavaScriptDelay()
        time.sleep(1)
        jsd = JavaScriptDelayPage(driver)
        jsd.clickBtnStart()
        assert "rgba(0, 170, 239, 1)" == jsd.checkBtnStartColor()
        print("El botón Start tiene el color celeste")
        time.sleep(2)










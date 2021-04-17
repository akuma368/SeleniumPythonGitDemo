import pytest
from Pages.ProjectPage import ProjectPage
from Pages.LoginPage import LoginPage
from Config.config import TestData
from Tests.test_basic import Basic_test
import time
class Test_Project(Basic_test):

    def test_title_Page(self):
        self.loginpage = LoginPage(self.driver)
        projectpage = self.loginpage.goto_project_page(TestData.USER_NAME,TestData.EMAIL)
        title_driver_gettitle = projectpage.get_page_title(TestData.TITLE_PROJECT)
        assert title_driver_gettitle == TestData.TITLE_PROJECT

    def test_text_display(self):
        self.loginpage = LoginPage(self.driver)
        projectpage = self.loginpage.goto_project_page(TestData.USER_NAME, TestData.EMAIL)
        time.sleep(10)
        assert TestData.TEXT_PROJECT in projectpage.check_text().text


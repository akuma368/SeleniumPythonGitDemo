import pytest
from Pages.ProjectPage import ProjectPage
from Pages.FormPage import FormPage
from Tests.test_basic import Basic_test
from Config.config import TestData

class Test_Form(Basic_test):

    def test_title_Page(self):
        self.projectpage = ProjectPage(self.driver)
        formpage = self.projectpage.goto_form_page()
        title_driver_gettitle = formpage.get_page_title(TestData.TITELE_ANGULAR)
        assert title_driver_gettitle == TestData.TITELE_ANGULAR

    def test_file_form(self):
        self.projectpage = ProjectPage(self.driver)
        formpage = self.projectpage.goto_form_page()
        formpage.submitForm()
        flag = formpage.getSuccessMessage().text
        assert flag

    def test_read_success_message(self):
        self.projectpage = ProjectPage(self.driver)
        formpage = self.projectpage.goto_form_page()
        formpage.submitForm()
        assert "success" in formpage.readSuccessMessage().text

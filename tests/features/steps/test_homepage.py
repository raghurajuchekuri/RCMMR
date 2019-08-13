import pytest
from pytest_bdd import scenario, given, when, then, scenarios
from pytest_bdd.feature import Scenario

from pages.HomePage import HomePage


scenarios('../login.feature')


@pytest.fixture
def home_page(config, browser):
    return HomePage(browser)


@given("I navigate to home page")
def navigate_to_home_page(home_page):
    home_page.load()


@when("I select contact us from menu")
def select_menu(home_page):
    print("Okay mama")


@then("I should see submit form")
def i_should_see_submit_form(home_page):
    print("Vachindi")


# @when("I enter details and submit")
# def enter_details(browser):
#     raise NotImplementedError(u'STEP: When I enter details and submit')
#
#
# @then("I should see details are submitted successfully")
# def should_see_details(browser):
#     raise NotImplementedError(u'STEP: Then I should see details are submitted succesfully')

import json
import os

import pytest
from selenium.webdriver import Chrome, Firefox

from pages.HomePage import HomePage

CONFIG_PATH = 'config.json'
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome', 'firefox']


@pytest.fixture(scope='session')
def config():
    print(os.getcwd())
    # Read the JSON config file and returns it as a parsed dict
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope='session')
def config_browser(config):
    # Validate and return the browser choice from the config data
    if 'browser' not in config:
        raise Exception('The config file does not contain "browser"')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config['browser']


@pytest.fixture(scope='session')
def config_wait_time(config):
    # Validate and return the wait time from the config data
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture
def browser(config_browser, config_wait_time):
    # Initialize WebDriver
    if config_browser == 'chrome':
        driver = Chrome()
    elif config_browser == 'firefox':
        driver = Firefox()
    else:
        raise Exception(f'"{config_browser}" is not a supported browser')
    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(config_wait_time)

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()


def pytest_bdd_before_scenario(request, feature, scenario):
    print("Scenario Called")

def pytest_bdd_after_scenario(request, feature, scenario):
    print("Scenario Finished")


def pytest_bdd_before_step(request, feature, scenario, step, step_func):
    print("Step Called")


def pytest_bdd_before_step_call(request, feature, scenario, step, step_func, step_func_args):
    """Called before step function is executed."""


def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    print("Step Finished")


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print("BDD STEP Error")


def pytest_bdd_step_validation_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print("Validations Error")


def pytest_bdd_step_func_lookup_error(request, feature, scenario, step, exception):
    """Called when step lookup failed."""


@pytest.hookspec(firstresult=True)
def pytest_bdd_apply_tag(tag, function):
    """Apply a tag (from a ``.feature`` file) to the given scenario.

    The default implementation does the equivalent of
    ``getattr(pytest.mark, tag)(function)``, but you can override this hook and
    return ``True`` to do more sophisticated handling of tags.
    """

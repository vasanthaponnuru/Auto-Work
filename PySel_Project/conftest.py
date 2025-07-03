import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    #options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    #driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
# Email the report after session ends
#def pytest_sessionfinish(session, exitstatus):
#   from utils.email_report import send_email_report
#   send_email_report(
#       sender="your_email@example.com",
#       password="your_password",
#       recipient="recipient@example.com",
#       smtp_server="smtp.gmail.com",
#       smtp_port=465,
#       report_path="report.html"
#   )

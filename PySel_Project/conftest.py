import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)

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

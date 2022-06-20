import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

chromedriver_autoinstaller.install()
prox = Proxy()
prox.proxy_type = ProxyType.MANUAL
prox.http_proxy = "85.31.51.143:30036"
prox.ssl_proxy = "85.31.51.143:30036"

capabilities = webdriver.DesiredCapabilities.CHROME
prox.add_to_capabilities(capabilities)

driver = webdriver.Chrome()
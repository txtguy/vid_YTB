#$$ pip install selenium
from selenium import webdriver


#// https://www.whatismybrowser.com/guides/the-latest-user-agent/safari
USER_AGENT="Mozilla/5.0 (PN; Macintosh; Intel Mac OS X 12_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.1"


#// `webdriver.FirefoxProfile()`: https://stackoverflow.com/a/54271641
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", USER_AGENT)

driver = webdriver.Firefox(firefox_profile=profile)

driver.get("http://www.whatsmyua.info")
#driver.get("https://www.youtube.com")


#cookies = driver.get_cookies()
#print(len(cookies))

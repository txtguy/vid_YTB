'''
```sh
pip install selenium
```

Gecko Driver
https://github.com/mozilla/geckodriver/releases
- https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz

```sh
sudo cp -p geckodriver /usr/local/bin/
```

ChromeDriver
https://chromedriver.chromium.org/downloads
- 101.0.4951.41 https://chromedriver.storage.googleapis.com/index.html?path=101.0.4951.41/
    - https://chromedriver.storage.googleapis.com/101.0.4951.41/chromedriver_linux64.zip

```sh
sudo cp -p chromedriver /usr/local/bin
```
'''
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

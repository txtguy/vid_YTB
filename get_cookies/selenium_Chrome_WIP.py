from selenium import webdriver

opt = webdriver.ChromeOptions()
opt.add_argument('--headless')
opt.add_argument('--user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 12_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.1"')

driver = webdriver.Chrome()

driver = webdriver.Chrome(options=opt)
driver.get('https://www.youtube.com')

cookies = driver.get_cookies()
print(len(cookies))


'''
ToDo: // To TRY...
[ ] https://stackoverflow.com/questions/57953240/google-login-is-not-working-in-headless-chrome-selenium-in-jenkins-job
    // https://groups.google.com/a/chromium.org/g/headless-dev/c/D1Fzxe4SH0A

[ ] https://stackoverflow.com/questions/70122366/chromeoptions-import-is-not-working-in-python-selenium-syntax-error
'''

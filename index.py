import time
import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
 
# 手机号
_PHONE  = "15370406515"
 
#设置日志等级
logging.basicConfig(level=logging.INFO)

chromeOptions = webdriver.ChromeOptions()

# 设置代理
chromeOptions.add_argument("--proxy-server=http://49.79.147.193:4218")
 
#打开浏览器
browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options = chromeOptions)
href = 'http://www.dianping.com/'
browser.get(href)
time.sleep(5)
 
# 右上登陆
login_btn = browser.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/div[2]/span[2]/a[1]')
login_btn.click()
time.sleep(5)
 
# 选择账号登录
iframe = browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div/iframe')
browser.switch_to_frame(iframe)   #切换至登录模块iframe
 
#手机验证码登录
mobile_login = browser.find_element_by_xpath('/html/body/div/div[2]/div[5]/span')
mobile_login.click()
phone = browser.find_element_by_xpath('//*[@id="mobile-number-textbox"]')
phone.clear()
phone.send_keys(_PHONE)
time.sleep(5)
        
#点击获取验证码
get_code = browser.find_element_by_xpath('//*[@id="send-number-button"]')
get_code.click()
        
#输入验证码
verify_code = browser.find_element_by_xpath('//*[@id="number-textbox"]')
verify_code_ = input('verify_code > ')
verify_code.clear()
verify_code.send_keys(verify_code_)
        
# 提交登陆
sub_btn = browser.find_element_by_xpath('//*[@id="login-button-mobile"]')
sub_btn.click()
time.sleep(5)
 
 
while True:
    #检测是否有登录失败警告
    try:
        alert = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[1]/div[3]/span')
    except NoSuchElementException:
        break
    
    if alert:
        raise Exception("Mobile login alert!")
        break
    else:
        raise Exception("Mobile login failed!")
               
#切换回主页
browser.switch_to_default_content()
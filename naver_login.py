from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
#드라이버 로딩
driver = webdriver.Chrome('./chromedriver.exe')

##사용할 변수 선언
#네이버 로그인 주소
url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'
uid = 'ta04028'
upw = 'dudwls34!!'

#네이버 로그인 페이지로 이동
driver.get(url)
time.sleep(2) #로딩 대기

#아이디 입력폼
tag_id = driver.find_element_by_name('id')
#패스워드 입력폼
tag_pw = driver.find_element_by_name('pw')

# id 입력
# 입력폼 클릭 -> paperclip에 선언한 uid 내용 복사 -> 붙여넣기
tag_id.click()
pyperclip.copy(uid)
tag_id.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# pw 입력
# 입력폼 클릭 -> paperclip에 선언한 upw 내용 복사 -> 붙여넣기
tag_pw.click()
pyperclip.copy(upw)
tag_pw.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

#로그인 버튼 클릭
login_btn = driver.find_element_by_id('log.login')
login_btn.click()
time.sleep(2)

#로그인이 실패했을 경우 - 예: 아이디나 패스워드 불일치
try:
    #로그인 실패창
    login_error = driver.find_element_by_css_selector('#err_common > div > p')
    print('로그인 실패 > ', login_error.text)
except:
    print('로그인 성공')



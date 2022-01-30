from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import sys

# pyautogui, pyinstaller, selenium 설치해야 함
# pyinstaller 명령어 - 터미널에서 pyinstaller --onefile -w main.py
### 현재 제로페이 웹 페이지 교체로 사용 불가능 ###

driver = webdriver.Chrome('src/chromedriver.exe') # 크롬드라이버
driver.get('https://www.zeropay.or.kr/main.do?pgmId=PGM1592') # 제로페이 로그인 페이지
driver.find_element(By.NAME, 'userId').send_keys("") # 아이디 입력

# 비밀번호를 입력하기 위한 작업
driver.find_element(By.ID, 'e2e_pass_card4_toggle').click()
pyautogui.sleep(1) # 입력하는 확률을 높이기 위한 잠깐의 텀
region = pyautogui.locateOnScreen('src/keyboard.png', confidence=0.9) # 비밀번호 입력 위치 찾기

# 해당 키를 찾아서 클릭하는 함수
def click(key):
    pyautogui.click(pyautogui.locateOnScreen('src/'+key+'.png', grayscale=True, region=region, confidence=0.90))

# selenium으로 입력되지 않는 비밀번호를 억지로 입력하기 위해 마우스 입력을 이용

# click('c') 비밀번호 입력할 때 사용한 함수, 디렉토리 src에 해당 c.png라는 이름을 가지고 있어야 입력가능

driver.find_element(By.CLASS_NAME, 'btn_submit.mo_wp100').click() # 로그인 버튼 클릭으로 로그인 시도
driver.get('https://www.zeropay.or.kr/main.do?pgmId=PGM1569') # 결제 정보 창으로 이동
driver.find_element(By.CLASS_NAME, 'btn-agree').click() # 조회 버튼 클릭
driver.execute_script('window.scrollTo(0, 600);') # 스크롤 이동
sys.exit() # driver.close()를 하면 브라우저 종료됨. 브라우저를 띄워서 결제정보를 사용자가 눈으로 확인하는 것이 목적임


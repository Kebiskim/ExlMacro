
'''
### 0. 모듈 임포트 
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import csv
import time
from datetime import datetime
import os
import signal
import json
from pathlib import Path


# ChromeDriver 버전 동적으로 다운로드
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Set up Chrome options if needed
chrome_options = webdriver.ChromeOptions()

# Add any desired options here, for example:
# chrome_options.add_argument("--headless")

# Initialize the Chrome WebDriver with `webdriver-manager`
service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=chrome_options)

# 크롬 사용 자원 및 설정 초기화
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# WebDriver 인스턴스 생성
driver = webdriver.Chrome(service=service, options=chrome_options)
pid = driver.service.process.pid
# try:
#     os.kill(int(pid), signal.SIGTERM)
#     print("Killed crome using process")
# except ProcessLookupError as ex:
#     pass

'''





import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
from selenium_stealth import stealth
from selenium.webdriver.chrome.service import Service
import time
import csv

# set variables (input vars)
# WebSiteURL = 'https://www.coupang.com/'
WebSiteURL = 'https://www.coupang.com/np/search?q=a4%EC%9A%A9%EC%A7%80&channel=recent'
KeywordToFind = 'A4용지'
FileToWrite = r'C:\CoupangScraper\CSVTest.csv'
# Max page num to search for the product
maxPageNumToSearch = 100
# set variables (inner vars)
# Define the total time to run and the interval between scrolls
nTotalTime = 5  # Total time to run in seconds
nInterval = 0.25  # Interval between each scroll and print operation in seconds
# Calculate the number of iterations
nIterations = int(nTotalTime / nInterval)

# log message function (Will be changed to display on the program later)
def log_message(message):
    print(message)  

# adding options -> disable popup
options = uc.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument('--disable-popup-blocking')
options.add_argument('--remote-debugging-port=9222')

# Create a WebDriver Object
driver = uc.Chrome(options = options,enable_cdp_events=True,incognito=True)

# selenium_stealth setting
stealth(driver,
        vendor="Google Inc. ",
        platform="Win32",
        webgl_vendor="intel Inc. ",
        renderer= "Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

# visit website
driver.get(WebSiteURL)
# wait for HTML to render
driver.implicitly_wait(2)
log_message(f'웹사이트 접속 성공: {WebSiteURL}')

# def search_paging():
#     try:
#         while True:
#             # Find all page number links
#             page_buttons = WebDriverWait(driver, 10).until(
#                 EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.search-pagination a'))
#             )
            
#             log_message('페이지 버튼들 찾기 성공')
            
#             # 지금 1~9까지 한번 찾은 후에 계속 누르는데, 할 때마다 계속 찾아야 함.
            

#             # Click on each page number link
#             for button in page_buttons:
#                 try:
#                     # Re-find the button to avoid stale element reference
#                     button = WebDriverWait(driver, 10).until(
#                         EC.element_to_be_clickable((By.XPATH, f'//a[text()="{button.text}"]'))
#                     )
                    
#                     # Debug: Print detailed information of each page button
#                     print(f"Found {len(page_buttons)} page buttons.")
#                     for index, button in enumerate(page_buttons):
#                         try:
#                             # Fetch and print button details
#                             button_text = button.text
#                             log_message(f"Button {index+1}:")
#                             log_message(f"  Text: {button_text}")
#                             # button_class = button.get_attribute('class')
#                             # button_href = button.get_attribute('href')
#                             # log_message(f"  Class: {button_class}")
#                             # log_message(f"  Href: {button_href}")
#                         except Exception as e:
#                             log_message(f"Error fetching details for button {index+1}: {e}")
                            
#                         # 11번째 요소가 Next 버튼임.. Text가 다음이면 pass해라 
#                         # Button 10:
#                         # Text: 27
#                         '''
#                         Button 10:
#                         Text: 27
#                         Class: btn-last disabled
#                         Href: None
#                         '''
                            
#                         log_message('페이징 버튼 클릭 시도')
                    
#                     # Click the button if it is not the currently selected page
#                     if 'selected' not in button.get_attribute('class'):
#                         button.click()
#                         WebDriverWait(driver, 10).until(
#                             EC.staleness_of(button)
#                         )
#                         driver.implicitly_wait(3)  # Wait for the page to load
#                     else:
#                         print(f"Already on page {button.text}")
#                 except Exception as e:
#                     print(f"Error interacting with page button: {e}")
#                     continue

#             # Find and click the 'Next' button if available
#             try:
#                 next_button = WebDriverWait(driver, 10).until(
#                     EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-next'))
#                 )
#                 if 'disabled' not in next_button.get_attribute('class'):
#                     next_button.click()
#                     WebDriverWait(driver, 10).until(
#                         EC.staleness_of(next_button)  # Wait until the button is no longer present
#                     )
#                     time.sleep(2)  # Wait for the next page to load
#                 else:
#                     # If 'Next' button is disabled, we are on the last page
#                     print("Reached the last page.")
#                     break
#             except Exception as e:
#                 print(f"Error interacting with 'Next' button: {e}")
#                 break
#     finally:
#         pass



def search_paging():
    try:
        # 페이지 번호를 1부터 시작
        page_number = 1
        
        while page_number <= maxPageNumToSearch:
            try:
                log_message(f"숫자에 맞는 페이지 버튼을 찾습니다 - {page_number} 페이지")
                # .search-pagination a 요소를 찾아서 page_buttons 리스트에 저장
                page_buttons = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.search-pagination a'))
                )
                
                log_message(f"페이지 버튼들 찾기 성공")

                # 현재 page_number에 맞는 버튼을 찾음
                for button in page_buttons:
                    button_text = button.text
                    
                    # 페이지 번호와 버튼의 텍스트가 일치하는 경우 클릭
                    if button_text == str(page_number):
                        log_message(f"{page_number} 페이지 클릭 시도")
                        
                        # 클릭 가능한지 확인 후 클릭
                        button = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, f'//a[text()="{button_text}"]'))
                        )
                        button.click()
                        log_message(f"{page_number} 페이지 클릭(이동) 완료 (페이지 로딩을 기다립니다.)")
                        
                        # 버튼이 stale 상태가 될 때까지 기다림
                        WebDriverWait(driver, 10).until(EC.staleness_of(button))
                        time.sleep(3)  # 페이지 로딩을 기다리기 위해 약간의 대기 시간
                        
                        # 페이지를 성공적으로 클릭한 후 반복문 탈출
                        break
                else:
                    # 만약 페이지 번호가 더 이상 없으면 종료
                    log_message(f"페이지 {page_number}를 찾을 수 없습니다. 종료.")
                    break
                
                # 페이지 번호를 증가시켜 다음 페이지로 이동
                page_number += 1
                
            except Exception as e:
                log_message(f"※ 에러 발생: {e}")
                break
    finally:
        log_message("검색 페이징 작업 완료")



search_paging()


log_message(f'검색을 진행합니다. 검색 키워드: {KeywordToFind}')

# Locate the searchtextbox by its ID and set the text to search
driver.find_element("id", "headerSearchKeyword").send_keys(KeywordToFind)
driver.implicitly_wait(5)  # Wait for up to 5 seconds for elements to appear
# Hit the search btn
driver.find_element("id", "headerSearchBtn").click()

# Set the current window to the original (products list window)
original_window = driver.current_window_handle

# Find images of each products
prod_images = driver.find_elements(By.CLASS_NAME, 'search-product-wrap-img')

# Check if there are any elements of image found
if prod_images:
    # Click the first element
    prod_images[1].click()
else:
    log_message('*오류 발생: 제품 목록에서 이미지를 찾지 못했습니다.*')
    # 프로그램 종료하기
    
driver.implicitly_wait(3)
    
# Get all window handles
all_windows = driver.window_handles

# Switch to the new tab
for window in all_windows:
    if window != original_window:
        driver.switch_to.window(window)
        break

driver.implicitly_wait(3)


log_message('상세 페이지에서 댓글 데이터를 추출합니다.')

# CSV file generate if not exist, or re-write
with open(FileToWrite, mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    
    # Loop to scroll and print
    for _ in range(nIterations):
        # Scroll to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
            # 한 페이지 분량씩 위로 3번 스크롤
        for i in range(3):
            # 현재 페이지 크기를 가져와서 1페이지만큼 위로 스크롤 (일반적으로 화면 높이 기준)
            scroll_height = driver.execute_script("return window.innerHeight;")  # 현재 페이지 높이 계산
            driver.execute_script(f"window.scrollBy(0, -{scroll_height});")  # 스크롤 위로 이동
            # print(f"Scrolled up by one page (iteration {i+1}).")
        
        # Wait for the page to load new content
        time.sleep(nInterval)  # Sleep for the interval time
        
        # Find elements
        elements = driver.find_elements(By.CLASS_NAME, 'sdp-review__article__list.js_reviewArticleReviewList')
        
        # Debug: Print the number of elements found
        print(f"Number of review elements found: {len(elements)}")
        
        # If a review element is found
        if len(elements) > 0:
            writer.writerow(["Index", "Review Text"])  # A열에 "Index", B열에 "Review Text"로 헤더 작성
            for index, element in enumerate(elements):
                review_text = element.text  # parse the whole text of a review
                writer.writerow([index, review_text])  # CSV 파일에 쓰기 (A열: index, B열: review_text)
                # print(f"Index {index}: {element.text}")
            log_message(f'[작업 완료]추출한 데이터 파일 쓰기 성공: {FileToWrite}')
            break
        # If review element is not found
        else:
            print("No review element's been found.")
        


print("전체 완료")

print("ㅎㅇ test중")



# 추출한 자료 엑셀 csv 파일 저장

# '''TEST 구간'''
# # 날짜 관련 작업 (금일 날짜 받아오기 등)
# def datework():
#     # 현재 날짜 및 시간 가져오기
#     now = datetime.now()
#     # 원하는 형식으로 날짜 포매팅
#     today_date = now.strftime("%Y-%m-%d")
#     return today_date
# today_date = datework()
# print(today_date)

# '''경로 생성 및 변수 호출'''
# # 사용자 홈 디렉토리 경로를 얻습니다.
# home_directory = Path.home()
# # 홈 디렉토리 내의 다운로드 폴더 경로를 생성합니다.
# downloads_path = os.path.join(home_directory, 'Downloads')
# # chromedriver 실행 경로 지정
# service = Service(executable_path=config['chromedriver_path'])
# # Chrome 옵션 설정
# chrome_options = Options()
# # 여기에 필요한 Chrome 옵션을 추가합니다. 예: chrome_options.add_argument('--headless')



# # 폴더가 존재하지 않는 경우에만 폴더 생성하기 (파라미터로 경로\폴더명 보내야 함)
# def create_folder(folderpath, foldername):
#     # 경로와 날짜를 조합하여 최종 폴더 경로 생성
#     folder_full_path = os.path.join(folderpath, foldername)
    
#     # 폴더가 존재하지 않는 경우에만 폴더 생성
#     if not os.path.exists(folder_full_path):
#         os.makedirs(folder_full_path)
#         print(f"Folder created at {folder_full_path}")
#     else:
#         print("Folder already exists.")

# # 폴더가 존재하지 않는 경우에만 폴더 생성하기 (파라미터로 경로\폴더명 보내야 함)
# create_folder(config['workpath'], today_date)






# '''수정해야 할 란들'''
# '''변수로 어떻게 넣을 것인지 PID 식으로 고민'''
# start_year = '2022' # 시작 연도
# start_month = '11' # 시작 월
# start_date = '-3'
# start_date = int(start_date)
# end_year = '2022' # 끝 연도
# end_month = '12' # 끝 월
# end_date = '-30'
# end_date = int(end_date)
# Down_name = '수입식품조회20221203' # 작업 당일 날짜 
# prd_org_name = 'product_origin_11wol_5'
# crawling_date = '2022년 11월 28일~12월 2일'

# 작업 Flag 지정
# ''''(1) 수입식품조회'에서 주간 수입품목 및 업체 리스트 받아오기'''
# WEEKLY_COMPANY = False
WEEKLY_COMPANY = True



# ''''(1) 수입식품조회'에서 주간 수입품목 및 업체 리스트 받아오기'''
# if WEEKLY_COMPANY == True:
#     options = webdriver.ChromeOptions()
#     user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
#     options.add_argument('user-agent=' + user_agent)
#     options.add_argument('--start-maximized')
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_experimental_option("excludeSwitches", ["enable-logging"])
#     options.add_argument('--blink-settings=imagesEnabled=false') 
#     options.add_argument("disable-gpu") 
#     options.add_argument("lang=ko_KR") # 가짜 플러그인
#     options.add_argument('incognito') 
#     options.add_argument('--mute-audio')
#     driver = webdriver.Chrome(service=service, options=chrome_options)
#     driver.implicitly_wait(1)
    

#     ### 1. 수입식품정보마루 접속 후 대기 
#     driver.get(kidfs_address)
#     driver.implicitly_wait(3)

#     find_class = Select(driver.find_element(By.ID, "dclPrductSeCd"))

#     KIND = '수산물' # or '가공식품'
#     find_class.select_by_visible_text(KIND)
#     magnify = driver.find_element(By.CSS_SELECTOR, 'button.itm-cd-button')
#     magnify.click()
#     driver.implicitly_wait(3)



#     ### 2. 날짜 선택 
#     # 2-1. 시작일 선택
#     driver.switch_to.window(driver.window_handles[0])
#     date_click_1 = driver.find_elements(By.CSS_SELECTOR, 'button.ui-datepicker-trigger')[0]
#     date_click_1.click()
#     year_click = Select(driver.find_element(By.CSS_SELECTOR, "select.ui-datepicker-year"))
#     year_click.select_by_visible_text(start_year)
#     month_click = Select(driver.find_element(By.CSS_SELECTOR, "select.ui-datepicker-month"))
#     month_click.select_by_visible_text(start_month)
#     date_start_click = driver.find_elements(By.CSS_SELECTOR, 'td > a.ui-state-default')[start_date]
#     date_start_click.click()

#     # 2-2. 종료일 선택
#     date_click_2 = driver.find_elements(By.CSS_SELECTOR, 'button.ui-datepicker-trigger')[1]
#     date_click_2.click()
#     year_click = Select(driver.find_element(By.CSS_SELECTOR, "select.ui-datepicker-year"))
#     year_click.select_by_visible_text(end_year)  # start_year가 아니라 end_year가 되어야 할 것 같습니다.
#     month_click = Select(driver.find_element(By.CSS_SELECTOR, "select.ui-datepicker-month"))
#     month_click.select_by_visible_text(end_month)
#     date_end_click = driver.find_elements(By.CSS_SELECTOR, 'td > a.ui-state-default')[end_date]
#     date_end_click.click()
#     search_button = driver.find_element(By.CSS_SELECTOR, 'button#btnSearch.search-i')
#     search_button.click()
#     # 아래 search_click 부분은 중복되므로 제거할 수 있습니다.
#     driver.implicitly_wait(3)
    
#     # 2-3. 다운로드 버튼 클릭
#     download_button = driver.find_element(By.CSS_SELECTOR, 'button.far.fa-file-excel.type2.bt3')
#     download_button.click()
#     time.sleep(10)
#     print('★★★ 주간 수입품목 및 수입업체 리스트 다운로드가 완료되었습니다. ★★★')
    
#     # 다운로드 폴더 내에 저장할 파일 경로 지정
#     file_path = os.path.join(downloads_path, '{}.xlsx')
#     downloaded_exl_path = file_path.format(Down_name)
    
#     ### ★★★ 1. 저장된 EXCEL 파일 날짜, 2. 저장할 CSV 파일 이름 바꿔주기 ★★★
#     excel_load = pd.read_excel(downloaded_exl_path, names=['idx0', 'idx1', 'idx2', 'idx3', 'idx4', 'idx5', 'idx6', 'idx7', 'idx8', 'idx9', 'idx10', 'idx11', 'idx12'], skiprows=[0])
#     excel_load = excel_load.drop(['idx0', 'idx1', 'idx2', 'idx3', 'idx4', 'idx6', 'idx7', 'idx8', 'idx10', 'idx11', 'idx12'], axis=1)
#     excel_load.sort_values(by=['idx5'], ascending=True, inplace=True)
#     print(excel_load)
#     print("★★★주간 수입업체 및 품목 리스트 다운로드가 완료되었습니다.★★★")
#     excel_load.to_csv('C:\\9\\venv\\Fish_import_price\\{}.csv'.format(prd_org_name), header=None, index=False, encoding='cp949') 
#     time.sleep(5)
    
    
    
    
# '''(2) ★★★ 크롤링 - 온라인 조회 통계"-품목별 원산지별 주별 수산물 수입단가 ★★★'''
# '''(3) 주별 단가 전처리 - 원산지, 가격 정보 병합'''

# must_delete_list = ['Plagioscion squamosissimus(냉동)', '갈치꼬치과,Lepidopus caudatus(냉동)', '갑오징어속,Sepia elegans(냉동)',
#                     '검정가자미(냉동,머리_외화획득용)', '까지가자미속,Lepidopsetta  polyxystra(냉동)', 
#                     '꼴뚜기과,Doryteuthis opalescens(냉동)', '꼴뚜기속,Loligo gahi(냉동)', '꼴뚜기속,Loligo vulgaris(냉동)', '꽃게과,Callinectes bellicosus(냉동)', 
#                     '꽃게과,Callinectes bellicosus(냉동)', '꽃게속,Portunus segnis(냉동)', '남방대구과,Macruronus magellanicus알(냉동,알)',
#                     '닭새우,Jasus edwardsii(냉동)', '닭새우속,Panulirus cygnus(냉동)', '닭새우속,Panulirus cygnus(활)', '대맛조개,Solen grandis(냉동)',
#                     '돌기해삼과,Stichopus hermanni(건조)', '돛새치속,Istiophorus albicans(건조)','만두성게과,Loxechinus albus알(냉동,포장횟감)', 
#                     '메기목,PANGASIUS PANGASIUS(냉동)', '물맞이게과,Maja squinado(냉동)', '물맞이게과,Maja squinado(냉동,집게다리,자숙)', '민태속,Johnius dussumieri(냉동)',
#                     '바닷가재과,Homarus americanus(냉동)', '백합,MERCENARIA MERCENARIA(활)', '밴댕이속,Sardinella longiceps(건조)', '볼락,Sebastes viviparus(냉동)',
#                     '뿔소라과,Hexaplex erythrostomus(냉동,살,자숙)',
#                     '빨강오징어과,Illex argentinus(냉동)', '아포돌기해삼속,Apostichus californicus(건조,자숙)', 
#                     '이리치과,Anarhichas denticulatus(냉동)', '전갱이,POMPANO(활)', '청어속,Clupea harengus알(냉동,알)',
#                     '코끼리조개속,Panopea generosa(활)', '피조개속,Anadara antiquata(냉동,살,자숙)', '홍연어,Red salmon(냉동)', '홍연어,Red salmon(냉동,포장횟감,필렛(F))', 
#                     '흉상어속, Carcharhinus limbatus(냉동)']

# WEEKLY = False
# # WEEKLY = True

# if WEEKLY == True:
#     options = webdriver.ChromeOptions()
#     # user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
#     user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37"
#     options.add_argument('user-agent=' + user_agent)
#     options.add_argument('headless')
    
    
#     # options.add_argument('window-size=1920x1080')
#     options.add_argument('--start-maximized')
#     options.add_argument("disable-gpu") 
#     options.add_argument("lang=ko_KR") # 가짜 플러그인
#     options.add_argument('incognito') 
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_experimental_option("excludeSwitches", ["enable-logging"])
#     options.add_argument('--blink-settings=imagesEnabled=false') 
#     options.add_argument('--mute-audio')
#     driver = webdriver.Chrome('C:\\9\\chromedriver', chrome_options=options)
#     driver.implicitly_wait(3)
#     driver.get_screenshot_as_file('KFDA_main_headless.png')
#     start_time = time.time()
#     # 품목별 원산지 csv 파일 로드 및 처리
    
#     ### ★★★★★★★★★[product_origin_8wol_2.csv] 열고, 유형(품목), 원산지 리스트★ (1. ★★★엑셀 전처리 및 검색 안되는 영문값 날리고, 2. ★중복값 제거후 저장)★★★★★★★★★★★
#     csv = pd.read_csv('C:\\9\\venv\\Fish_import_price\\{}.csv'.format(prd_org_name), names=['품목', '원산지'], encoding='cp949')
#     csv = csv.drop_duplicates()
#     KEYWORD_1 = csv['품목']
#     KEYWORD = KEYWORD_1.values.tolist()
#     ORIGIN_1 = csv['원산지']
#     ORIGIN = ORIGIN_1.values.tolist()
#     for must_delete in must_delete_list:     
#         idx = csv[csv['품목'] == must_delete].index
#         csv = csv.drop(idx)
#     result = []
#     counting = 0

#     # 크롤링하는 부분
#     for ORIGIN_get, KEYWORD_get in zip(ORIGIN, KEYWORD):
        
#         ### 1. 온라인 조회 통계 사이트 접속
#         driver.get('https://impfood.mfds.go.kr/CFDDD01F01')
#         driver.implicitly_wait(3)
#         ### 2. 분류 - 품목(유형)별 체크박스 클릭
#         product = driver.find_elements_by_css_selector('span.check')[4]
#         product.click()
#         # 2-1. 분류 - 제품구분 - 수산물 클릭
#         susanmul = Select(driver.find_element_by_id('srchPrductSeCd'))
#         susanmul.select_by_visible_text('수산물')
#         # 2-2. 분류 - 제조국 선택
#         country = Select(driver.find_element_by_id('srchMnfNtncd'))
#         country.select_by_visible_text(ORIGIN_get)
#         # 2-3. 분류 - 돋보기 클릭
#         magnify = driver.find_element_by_xpath('//*[@id="frm"]/table/tbody/tr[4]/td[1]/span/button')
#         magnify.click()
#         driver.implicitly_wait(3)
#         # 2-4. 유형 키워드 검색 (ex.문어)
#         driver.switch_to.window(driver.window_handles[1])
#         input_keyword = driver.find_element_by_css_selector('input#koreanNm')
#         driver.implicitly_wait(3)
#         input_keyword.clear()
#         input_keyword.send_keys(KEYWORD_get)
#         # 2-5. '검색' 버튼 클릭
#         btn_click = driver.find_element_by_name('btnSearch')
#         btn_click.click()
#         driver.implicitly_wait(3)
#         # 2-6. 맨위에 뜨는 체크박스 클릭
#         try:
#             chk_click = driver.find_element_by_id('chk1') # ★★★오류발생★★★
#             chk_click.click()
#         except:
#             cancel_click = driver.find_element_by_css_selector('button.fas.fa-times.type1.bt10')
#             cancel_click.click()
#         # 2-7. '선택품목추가' 클릭
#         add_click = driver.find_element_by_xpath('//*[@id="content_pop"]/div/div[2]/button')
#         add_click.click()
#         # 2-8. '확인' 클릭
#         conf_click = driver.find_element_by_xpath('//*[@id="content_pop"]/div/div[4]/button[1]')
#         conf_click.click()
#         driver.implicitly_wait(3)

#         ### 3. 기간 선택
#         # 3-1. 시작일 선택
#         driver.switch_to.window(driver.window_handles[0])
#         date_click_1 = driver.find_elements_by_css_selector('button.ui-datepicker-trigger')[0]
#         date_click_1.click()
#         year_click = Select(driver.find_element_by_css_selector("select.ui-datepicker-year"))
#         year_click.select_by_visible_text(start_year)
#         month_click = Select(driver.find_element_by_css_selector("select.ui-datepicker-month"))
#         month_click.select_by_visible_text(start_month)
#         # ★★★ 시작일 선택
#         date_start_click = driver.find_elements_by_css_selector('a.ui-state-default')[start_date]   
#         date_start_click.click()

#         # 3-2. 종료일 선택
#         date_click_2 = driver.find_elements_by_css_selector('button.ui-datepicker-trigger')[1]
#         date_click_2.click()
#         year_click = Select(driver.find_element_by_css_selector("select.ui-datepicker-year"))
#         year_click.select_by_visible_text(end_year)
#         month_click = Select(driver.find_element_by_css_selector("select.ui-datepicker-month"))
#         month_click.select_by_visible_text(end_month)
#         # ★★★ 종료일 클릭
#         date_end_click = driver.find_elements_by_css_selector('a.ui-state-default')[end_date]   
#         date_end_click.click()
#         # 중량/금액(kg/$), 조회 클릭
#         dollar = driver.find_elements_by_css_selector('span.check')[6]
#         dollar.click()
#         search_button = driver.find_element_by_css_selector('button.search-i')
#         search_button.click()

#         ### 4-1. 월전체 수입중량, 금액자료 크롤링
#         monthly_price = driver.find_element_by_xpath('//*[@id="tblList"]/tbody')
#         monthly_price_2 = monthly_price.find_elements_by_tag_name('tr')
#         print(monthly_price_2[-1].text)

#         # 리스트에 결과값 순서대로 넣어 주기
#         for td in monthly_price_2:
#             kg_price = td.text
#             kg_price_list = kg_price.split('\n')
#             print(kg_price_list)

#         result.append(kg_price_list)
        
#         result_df = pd.DataFrame(result) 
#         # ★저장될 파일 이름 바꿔주기
#         result_df.to_csv('C:\\9\\venv\\Fish_import_price\\{} 수산물 수입가격.csv'.format(crawling_date), index=False, encoding='utf-8-sig')
#         counting = counting + 100
#         percent = round(counting / len(KEYWORD), 2)
#         print('★ 원산지별 품목별 주간 수입단가 크롤링 중입니다. ★')
#         print('진행 상황입니다.:', percent, '%')
#         print('소요 시간입니다:', time.time()-start_time)
    
#     print('결과는:', result)
#     import winsound as sd
#     def beepsound():
#         fr = 1000    # range : 37 ~ 32767
#         du = 2000     # 1000 ms ==1second
#         sd.Beep(fr, du) # winsound.Beep(frequency, duration)
#     beepsound()
#     time.sleep(5)


# # PREPROCESSING = False
# # PREPROCESSING = True
# # if PREPROCESSING == True:
#     df_1 = pd.read_csv('C:\\9\\venv\\Fish_import_price\\{} 수산물 수입가격.csv'.format(crawling_date), names=['idx1'], skiprows=[0])
#     # 원산지 자료 병합 및 정리
#     df_2 = pd.read_csv('C:\\9\\venv\\Fish_import_price\\{}.csv'.format(prd_org_name), names = ['idx2', 'idx3'], encoding='cp949')
#     df_2 = df_2.drop_duplicates()
#     df_2.reset_index(inplace=True, drop=False)
#     print(df_2)

    
#     # 1열에 모여있는 데이터 분할 - 각 배열이 Series를 리턴하게 apply 적용, Series를 DF로 변환.
#     split = df_1.idx1.str.split(' ')
#     split = split.apply(lambda x: pd.Series(x))
#     df_2 = df_2.drop(['idx2'], axis=1)
#     df_1.info()
#     df_2.info()
    
#     # 열이름 지정 및 순서 변경 (원산지를 품목(유형) 바로 옆으로)
#     df_concat = pd.concat([split, df_2], axis=1)
#     print(df_concat)
    
#     df_concat.columns = ['품목(유형)', '전체 중량(kg)', '전체 수입액($)', '적합 중량(kg)', '적합 수입액($)', '부적합 중량(kg)', '부적합 수입액($)', '제거', '원산지']
#     # ★ 오류 발생해서 추가행 넣은 것
#     df_concat.drop(['제거'], axis=1, inplace=True)
#     # df_concat.columns = ['품목(유형)', '전체 중량(kg)', '전체 수입액($)', '적합 중량(kg)', '적합 수입액($)', '부적합 중량(kg)', '부적합 수입액($)', '원산지']
#     df_concat = df_concat[['품목(유형)', '원산지', '전체 중량(kg)', '전체 수입액($)', '적합 중량(kg)', '적합 수입액($)', '부적합 중량(kg)', '부적합 수입액($)']]
#     # 조회 결과 없는 행 날리기
#     idx = df_concat[df_concat['품목(유형)'] == '조회'].index
#     df_concat = df_concat.drop(idx)
#     df_concat['주간 평균 수입가($/kg)'] = 0
#     print('\n')
#     print(df_concat.head(50))

#     print('\n')
#     df_concat.info()
    
#     print('\n')
#     df_concat.describe()
    
#     print('\n')
#     print(len(df_concat.index))
    
#     # ★★★★★ 에러 발생!!! 
#     # 소숫점이 있으므로 정수형을 int형으로 변환 불가 
#     # 따라서, 각 숫자들의 소숫점 포함 뒤에 3자리 (ex) .000 등 제거
#     for ii_1 in range(2, 8):
#         for i_1 in range(0, len(df_concat.index)):
#             try:
#                 df_concat.iloc[i_1, ii_1] = df_concat.iloc[i_1, ii_1][:-4]
#                 i_1 =+ 1
#             except:
#                 pass
#         ii_1 =+ 1
#     # 소숫점 콤마 제거 
#     for l in range(2, 8):
#         df_concat.iloc[:, l] = df_concat.iloc[:, l].apply(lambda x: str(x).replace(',', ''))
#         l =+ 1
#     # 문자형 숫자들 형태를 int형으로 변환 (astype은 공란 때문에 못씀)
#     for ll in range(2, 6):
#         try:
#             df_concat.iloc[:, ll] = pd.to_numeric(df_concat.iloc[:, ll], errors='coerce')
#             ll =+ 1
#         except:
#             pass

#     df_concat['주간 평균 수입가($/kg)'] = df_concat.apply(lambda x: round(x['적합 수입액($)'] / x['적합 중량(kg)'], 3), axis=1)
#     df_concat = df_concat[['품목(유형)', '원산지', '전체 중량(kg)', '전체 수입액($)', '적합 중량(kg)', '적합 수입액($)', '주간 평균 수입가($/kg)', '부적합 중량(kg)', '부적합 수입액($)']]
#     print('\n')
#     df_concat.info()
#     df_concat.to_csv('C:\\9\\venv\\Fish_import_price\\{} 품목별 원산지별 수산물 수입 가격.csv'.format(crawling_date), index=False, encoding="utf-8-sig")
#     df_concat.to_excel('C:\\9\\venv\\Fish_import_price\\{} 품목별 원산지별 수산물 수입 가격.xlsx'.format(crawling_date), index=False)

#     print('\n')
#     print('★★★ 품목별 원산지별 주간 수입가 파일(업체명 없음) 저장이 완료되었습니다. ★★★')



# '''(4) 수입 업체, 가격 정보 concat'''
# PREPROCESSING_2 = False
# # PREPROCESSING_2 = True

# if PREPROCESSING_2 == True:
#     df_3 = pd.read_csv('C:\\9\\venv\\Fish_import_price\\{} 품목별 원산지별 수산물 수입 가격.csv'.format(crawling_date))
#     df_3.drop(['부적합 중량(kg)', '부적합 수입액($)'], axis=1, inplace=True)
#     '''오류 발생할 경우 팁
#     # ★★★must_delete 다 작성될 까지는 우선은 다운로드 폴더에 수입식품조회20220625 열어서,
#     # ① 0, 1, 11, 12열 날리고, ② '품목(유형)', '원산지', '수입업체', '제품명(한글)', '제품명(영문)', '해외제조업소', '처리일자', '유통기한', '수출국'
#     # 순으로 정렬 후, ③ 품목(유형), 제조국 순으로 오름차순 정렬해 주고, ④ 안쓰는 품목 제거하고, ⑤ 타이틀 날린 후에 csv 저장해 주자.
#     # df_4 = pd.read_csv('C:\\9\\venv\\Fish_import_price\\product_company_6wol_2.csv', header=None, encoding='cp949')
#     '''
    
#     # ★★★★★★★ 간단하게 must_delete_list 복붙해서 가지고 오자!!!!! ★★★★★★ 
#     df_4 = pd.read_excel('C:\\Users\\user\\Downloads\\{}.xlsx'.format(Down_name), header=0)
#     df_4.drop(['NO', '구분', '냉동전환번호', '이력추적번호'], axis=1, inplace=True)    
#     df_4.columns = ['수입업체', '제품명(한글)', '제품명(영문)', '품목(유형)', '해외제조업소', '처리일자', '유통기한', '원산지', '수출국']
#     df_4 = df_4[['품목(유형)', '원산지', '수입업체', '제품명(한글)', '제품명(영문)', '해외제조업소', '처리일자', '유통기한', '수출국']]
#     print(df_4)
#     # 검색안되는 품목 날리기
#     must_delete_list = ['Plagioscion squamosissimus(냉동)', '갈치꼬치과,Lepidopus caudatus(냉동)', '갑오징어속,Sepia elegans(냉동)',
#                         '검정가자미(냉동,머리_외화획득용)', '까지가자미속,Lepidopsetta  polyxystra(냉동)', 
#                         '꼴뚜기과,Doryteuthis opalescens(냉동)', '꼴뚜기속,Loligo gahi(냉동)', '꼴뚜기속,Loligo vulgaris(냉동)', '꽃게과,Callinectes bellicosus(냉동)', 
#                         '꽃게과,Callinectes bellicosus(냉동)', '꽃게속,Portunus segnis(냉동)', '남방대구과,Macruronus magellanicus알(냉동,알)',
#                         '닭새우,Jasus edwardsii(냉동)', '닭새우속,Panulirus cygnus(냉동)', '닭새우속,Panulirus cygnus(활)', '대맛조개,Solen grandis(냉동)',
#                         '돌기해삼과,Stichopus hermanni(건조)', '돛새치속,Istiophorus albicans(건조)','만두성게과,Loxechinus albus알(냉동,포장횟감)', 
#                         '메기목,PANGASIUS PANGASIUS(냉동)', '물맞이게과,Maja squinado(냉동)', '물맞이게과,Maja squinado(냉동,집게다리,자숙)', '민태속,Johnius dussumieri(냉동)',
#                         '바닷가재과,Homarus americanus(냉동)', '백합,MERCENARIA MERCENARIA(활)', '밴댕이속,Sardinella longiceps(건조)', '볼락,Sebastes viviparus(냉동)',
#                         '뿔소라과,Hexaplex erythrostomus(냉동,살,자숙)',
#                         '빨강오징어과,Illex argentinus(냉동)', '아포돌기해삼속,Apostichus californicus(건조,자숙)', 
#                         '이리치과,Anarhichas denticulatus(냉동)', '전갱이,POMPANO(활)', '청어속,Clupea harengus알(냉동,알)',
#                         '코끼리조개속,Panopea generosa(활)', '피조개속,Anadara antiquata(냉동,살,자숙)', '홍연어,Red salmon(냉동)', '홍연어,Red salmon(냉동,포장횟감,필렛(F))', 
#                         '흉상어속, Carcharhinus limbatus(냉동)']
#     for must_delete in must_delete_list:
#         idx = df_4[df_4['품목(유형)'] == must_delete].index
#         df_4 = df_4.drop(idx)
#     df_4.sort_values('품목(유형)', ascending=True)
        
#     # df_4.to_csv('test_2.csv', index=False, encoding='utf-8-sig')
#     # # idx = df_4[df_4['품목(유형)'] == 'Plagioscion squamosissimus(냉동)', '갈치꼬치과,Lepidopus caudatus(냉동)', '까지가자미속,Lepidopsetta  polyxystra(냉동)', '꼴뚜기과,Doryteuthis opalescens(냉동)', '꼴뚜기속,Loligo gahi(냉동)', '꼴뚜기속,Loligo vulgaris(냉동)', '꽃게과,Callinectes bellicosus(냉동)', '꽃게속,Portunus segnis(냉동)', '닭새우속,Panulirus cygnus(냉동)', '닭새우속,Panulirus cygnus(활)', '민태속,Johnius dussumieri(냉동)', '전갱이,POMPANO(활)', '코끼리조개속,Panopea generosa(활)', '홍연어,Red salmon(냉동,포장횟감,필렛(F))'].index

#     # 품목(유형) 열을 기준으로 열방향 병합
#     df_5 = pd.merge(df_3, df_4, on='품목(유형)')
#     df_5.columns = ['품목(유형)', '원산지', '전체 중량(kg)', '전체 수입액($)', '적합 중량(kg)', '적합 수입액($)', '주간 평균 수입가($/kg)', 'del', '수입업체', '제품명(한글)', '제품명(영문)', '해외제조업소', '처리일자', '유통기한', '수출국']
#     df_5.drop(['del'], axis=1, inplace=True)
#     df_5.to_excel('C:\\9\\venv\\★★★Final_result\\{} 수산물 품목별, 원산지별 수입가 (수입업체 정보 포함).xlsx'.format(crawling_date), index=False)

#     print('\n')
#     print('★★★ 주간 품목별 원산지별 수입가 (수입업체 정보 포함)이 저장 완료되었습니다. [최종 완료] ★★★')
#     # ★★★ 최종적으로, 엑셀 다듬어서 업로드 - 끝 






   














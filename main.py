from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from function import health_paid_certi

#Information--------------------------------------------

BUSINESS_NUMBER = "134-81-68980"
CORPORATION_NUMBER = "135011-0113501"
TEL = "031-374-8521/2"
FAX = "031-374-8534"
HEALTH_ID = "mtoo8521"
CERTI_PW = "mtoo68980*"
PDF_PASS = BUSINESS_NUMBER.replace("-", "")
#Function-----------------------------------------------

# 국민연금/건강보험 완납증명서
health_paid_certi(BUSINESS_NUMBER, HEALTH_ID, CERTI_PW, PDF_PASS)

# 국민연금/건강보험 가입증명서
# 산재보험/고용보험 완납증명서
# 산재보험/고용보험 가입증명서
# 국세완납증명서
# 지방세완납증명서
# 프린터출력
# PDF출력

#UI-----------------------------------------------------


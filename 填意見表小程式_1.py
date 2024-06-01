"""
Created on Wed Dec 20 16:15:42 2023

@author: NTPU Computer Center

Hung-Chih Chiang, NTPU STAT
"""

print("## 請填入學生資訊系統的帳號密碼來自動填寫課程意見表")
print("## 使用前記得安裝Firefox跟下載geckodriver.exe")
print("## 填表時電腦可以去做別的事，也可以看進度條來觀察填寫情況")
print("## 這東西只在你的電腦上跑，不會傳東西到我的電腦，所以不用擔心密碼的問題")
print("## 麻煩請確定這個exe檔跟geckodriver.exe裝在同個資料夾，感謝你")
print("## 等他一下哦他馬上就會跳出讓你填學號的了")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from tqdm.auto import tqdm
import numpy as np
import maskpass 
import time

def alert_is_present(driver): # 擋叫你去寫自傳的提示
    try:
        alert = driver.switch_to.alert
        alert.text
        return alert
    except:
        return False

try :
    account = ''
    while(account == '') :
        account = input("Enter Stud. ID: ")
    password = ''
    while(password == '') :
        password = maskpass.askpass()

    options = Options()
    options.add_argument('--headless') # 不打開瀏覽器

    path = "geckodriver.exe"
    service = Service(executable_path=path)
    chcc = 0
    try :
        options.binary_location = 'C:/Program Files/Mozilla Firefox/firefox.exe'
        driver = webdriver.Firefox(service=service, options = options)
    except :
        print("## 先檢查一下你的geckodriver.exe有沒有跟這個檔案在同個地方，檢查完之後重開這個程式")
        print("## 不然就是你沒裝火狐或是你的磁碟不是C槽，請幫我填上你的火狐路徑(例如: 'D:/Program Files/Mozilla Firefox/firefox.exe')，一直失敗的話就關掉重開吧")
        while(chcc == 0) :
            try :
                path1 = input("火狐安裝位置: ")
                options.binary_location = path1
                driver = webdriver.Firefox(service=service, options = options)
                chcc = 1
            except Exception as e :
                print(e)
                print("## 還是錯的欸")
    
    
    print("登入中 請稍後...")

    url = 'https://ohs02.ntpu.edu.tw/student_new.htm'
    driver.get(url)

    driver.find_element("name", "stud_num").send_keys(account)
    driver.find_element("name", "passwd").send_keys(password)
    driver.find_element("id", "loginBtn1").click()
    if alert_is_present(driver) :
        driver.switch_to.alert.accept()

    time_now = time.strftime("%Y %m %d", time.localtime()).split()
    month = int(time_now[1])
    year = int(time_now[0]) - (1912 if month < 9 else 1911) # 九月註冊後當成新的一年
    driver.get('https://ohs02.ntpu.edu.tw/pls/univer/query_all_course.judge?year1=' + str(year))
    
    sub = driver.find_elements(By.XPATH, "//a[@target='mainFrame']")
    href = [s.get_attribute('href') for s in sub]
    class_name = [s.text for s in sub]

    need = [47, 48, 49, 410]
    skip = [15, 16, 17, 18, 22]
    trap = [4, 11]
    p = np.array([0.8, 0.2])
    counter = 0
    for m, obj in enumerate(href) :
        counter += 1
        if(1) :
            driver.get(obj)
            print(f"開始填寫 '{class_name[m]}' ...")

            total = 0
            with tqdm(total = 100, colour = "#0396ff") as pbar:
                pbar.set_description('填寫進度')
                driver.find_element("name", "q03").click()  

                for i in range(1, 25) :   
                    if(not(i in skip)) :
                        if(i in trap) :
                            k = 4
                        else :
                            k = np.random.choice([0, 1], p = p.ravel())
                        elements = driver.find_elements("name", "q"+str(i))
                        elements[k].click()
                        pbar.update(4)
                        total += 4
                
                for t, i in enumerate(need) :   
                    elements = driver.find_elements("name", "qc"+str(i))
                    if(t == 0) :
                        elements[0].click()
                        elements[3].click()
                        elements[4].click()
                    else :
                        elements[t].click()
                    pbar.update(4)
                    total += 4

                pbar.update(100-total)
                driver.find_element("name", "q61").send_keys("謝謝老師!")
                
                for i in range(70, 73) :   
                    try :
                        elements = driver.find_elements("name", "qc"+str(i))
                        if(i==0) :
                            k = 2
                        else :
                            k = 0
                        elements[k].click()
                    except :
                        break
            driver.find_element(By.XPATH, "//input[@type='submit']").click()
            while(1) :
                pbar.update(3)
                if alert_is_present(driver) :
                    driver.switch_to.alert.accept()
                    try :
                        driver.switch_to.alert.accept()
                        break
                    except :
                        break
            print(f"已完成 '{class_name[m]}' 的填寫")
            time.sleep(0.5)
    out_str = "填完啦!" if counter>0 else \
        "! 你帳號密碼打錯了嗎，我沒做防呆，打錯的話就再重開一次吧\n也可能是你之前填完了"
    print(out_str)

    driver.close()
except :
    print("## 哇勒你找到BUG了，麻煩你重開這個程式再試一次吧。")
    print("## 如果還是沒有用的話再麻煩你傳訊息跟我講。")
# pyinstaller -F .\填意見表小程式_1.py --icon=stat.ico
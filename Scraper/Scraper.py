from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


url = 'https://abcnotation.com/browseTunes?n='
s=Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=s)

id = 0
# 1608
for i in range(0, 1608):
    pageNumber = str(i)
    if len(pageNumber) == 1:
        pageNumber = '000' + pageNumber
    elif len(pageNumber) == 2:
        pageNumber = '00' + pageNumber
    elif len(pageNumber) == 3:
        pageNumber = '0' + pageNumber
    # 201
    for j in range(1, 201):
        browser.get(url + pageNumber)
        browser.find_element(By.XPATH, '/html/body/div[2]/div/main/section[2]/pre/a[' + str(j  * 2) + ']').click()
        browser.implicitly_wait(2)
        content = browser.find_element(By.XPATH, '/html/body/div[2]/div/main/section[2]/div[2]/section/pre').text
        try:
            lines = content.split('\n')
            hasValue = False
            linesToDel = []
            for j in range(len(lines)):
                if lines[j][0] == 'W' or lines[j][0] == 'w':
                    linesToDel.append(j)
                elif lines[j][0] == 'V' or lines[j][0] == 'v':
                    hasValue = True
                lines[j] = lines[j] + '\n'
            
            if hasValue:
                linesToDel.sort(reverse=True)
                for line in linesToDel:
                    lines.pop(line)
                open('./Scraper/dataset/'  + str(id) + '.txt', 'w', encoding="utf-8").write(''.join(lines))

        except UnicodeEncodeError:
            print("Couldnt save id: " + str(id) + " beacuse of unicode error.")
        finally:
            id += 1
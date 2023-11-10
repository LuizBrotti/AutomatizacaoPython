from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

# accessing the Dollar value on a website.
driver = webdriver.Chrome()
driver.get('https://www.google.com/search?client=opera-gx&q=dollar+hoje&sourceid=opera&ie=UTF-8&oe=UTF-8')

# extracting dollar value from website. 
dollar_1 = driver.find_elements(By.XPATH,"//span[@class='DFlfde SwHCTb']")

# accessing the value of Argentine Pesos on a website.
driver = webdriver.Chrome()
driver.get('https://www.google.com/search?q=pesos+hoje&sca_esv=580917885&sxsrf=AM9HkKkvgawHagUf1-cKzhEVjAs-zFA94Q%3A1699552465785&ei=0RxNZZ7HL9em5OUPguW2oAY&ved=0ahUKEwje8_-nvreCAxVXE7kGHYKyDWQQ4dUDCBA&uact=5&oq=pesos+hoje&gs_lp=Egxnd3Mtd2l6LXNlcnAiCnBlc29zIGhvamUyBRAAGIAEMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeSN4LUNgGWNgGcAF4AZABAJgBbqABbqoBAzAuMbgBA8gBAPgBAcICChAAGEcY1gQYsAPiAwQYACBBiAYBkAYI&sclient=gws-wiz-serp')

# extracting value in Pesos from the website.
pesos_1 = driver.find_elements(By.XPATH,"//span[@class='DFlfde SwHCTb']")

# accessing the value of gold in reais on the website.
driver = webdriver.Chrome()
driver.get('https://goldrate.com/pt-br/grama-do-ouro-preco-cotacao-valor/')

# extracting Gold value from the website.
gold_1 = driver.find_elements(By.XPATH,'//*[@id="main"]/div/div/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/h2/em')

# Creating a spreadsheet.
workbook = openpyxl.Workbook()
# Creating a 'Valor_Coins' page.
workbook.create_sheet('Valor_Coins')
# Selecting the page.
sheet_Valor_Moedas = workbook['Valor_Coins']
# Creating line names.
sheet_Valor_Moedas['A1'].value = 'Dollar'
sheet_Valor_Moedas['B1'].value = 'Pesos'
sheet_Valor_Moedas['C1'].value = 'Gold'


# entering data into the spreadsheet.
for dollar,pesos,gold in zip(dollar_1,pesos_1,gold_1):
    sheet_Valor_Moedas.append([dollar.text,pesos.text,gold.text])

# saving the spreadsheet.
workbook.save('automate_currencies.xlsx')


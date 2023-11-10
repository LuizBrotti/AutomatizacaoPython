from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

# Paths
dollarPath = 'https://www.google.com/search?client=opera-gx&q=dollar+hoje&sourceid=opera&ie=UTF-8&oe=UTF-8'
pesosPath  = 'https://www.google.com/search?q=pesos+hoje&sca_esv=580917885&sxsrf=AM9HkKkvgawHagUf1-cKzhEVjAs-zFA94Q%3A1699552465785&ei=0RxNZZ7HL9em5OUPguW2oAY&ved=0ahUKEwje8_-nvreCAxVXE7kGHYKyDWQQ4dUDCBA&uact=5&oq=pesos+hoje&gs_lp=Egxnd3Mtd2l6LXNlcnAiCnBlc29zIGhvamUyBRAAGIAEMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeSN4LUNgGWNgGcAF4AZABAJgBbqABbqoBAzAuMbgBA8gBAPgBAcICChAAGEcY1gQYsAPiAwQYACBBiAYBkAYI&sclient=gws-wiz-serp'
euroPath   = 'https://www.google.com/search?q=euro+hoje&oq=euro+hoje&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDcwNDBqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8'
goldPath   = 'https://goldrate.com/pt-br/grama-do-ouro-preco-cotacao-valor/'

# Path of the element in the page
dollarElementPath = "//span[@class='DFlfde SwHCTb']"
pesosElementPath  = "//span[@class='DFlfde SwHCTb']"
euroElementPath   = '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
goldElementPath   = '//*[@id="main"]/div/div/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/h2/em'

# accessing the dollar value in BRL from a website.
driver = webdriver.Chrome()
driver.get(dollarPath)

# extracting dollar value from website. 
dollarValue = driver.find_elements(By.XPATH,dollarElementPath)[0].text

# accessing the value of Argentine pesos in reais from a website.

driver.get(pesosPath);

# extracting value in Pesos from the website.
pesosValue = driver.find_elements(By.XPATH,pesosElementPath)[0].text
# accessing the value of the euro in reais from a website.

driver.get(euroPath);

# extracting value in euro from the website.
euroValue = driver.find_elements(By.XPATH,euroElementPath)[0].text
# accessing the value of gold in reais on the website.

driver.get(goldPath)

# extracting Gold value from the website.
goldValue = driver.find_elements(By.XPATH,goldElementPath)[0].text

# Check values in prompt
print("Dollar: {}, Pesos: {}, Euro: {}, Gold: {}.".format(dollarValue ,pesosValue, euroValue, goldValue));

# Creating a spreadsheet.
workbook = openpyxl.Workbook()
# Creating a 'Valor_Coins' page.
workbook.create_sheet('Valor_Coins')
# Selecting the page.
sheet_Valor_Moedas = workbook['Valor_Coins']
# Creating line names.
sheet_Valor_Moedas['A1'].value = 'Dollar'
sheet_Valor_Moedas['B1'].value = 'Pesos'
sheet_Valor_Moedas['C1'].value = 'Euro'
sheet_Valor_Moedas['D1'].value = 'Gold'

# entering data into the spreadsheet.
sheet_Valor_Moedas.append([dollarValue,pesosValue,euroValue,goldValue])

# saving the spreadsheet.
workbook.save('automate_currencies.xlsx')


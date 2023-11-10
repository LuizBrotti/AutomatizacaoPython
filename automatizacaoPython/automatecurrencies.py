from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

#Methods
# Acess the website and get the value
def getValue(driver, pagePath, elementPath):
    driver.get(pagePath)
    value = driver.find_elements(By.XPATH, elementPath)[0].text
    return value

#Global Attributes
# Path of the pages
dollarPagePath = 'https://www.google.com/search?client=opera-gx&q=dollar+hoje&sourceid=opera&ie=UTF-8&oe=UTF-8'
pesosPagePath  = 'https://www.google.com/search?q=pesos+hoje&sca_esv=580917885&sxsrf=AM9HkKkvgawHagUf1-cKzhEVjAs-zFA94Q%3A1699552465785&ei=0RxNZZ7HL9em5OUPguW2oAY&ved=0ahUKEwje8_-nvreCAxVXE7kGHYKyDWQQ4dUDCBA&uact=5&oq=pesos+hoje&gs_lp=Egxnd3Mtd2l6LXNlcnAiCnBlc29zIGhvamUyBRAAGIAEMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeSN4LUNgGWNgGcAF4AZABAJgBbqABbqoBAzAuMbgBA8gBAPgBAcICChAAGEcY1gQYsAPiAwQYACBBiAYBkAYI&sclient=gws-wiz-serp'
euroPagePath   = 'https://www.google.com/search?q=euro+hoje&oq=euro+hoje&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDcwNDBqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8'
goldPagePath   = 'https://goldrate.com/pt-br/grama-do-ouro-preco-cotacao-valor/'

# Path of the element in the page
dollarElementPath = "//span[@class='DFlfde SwHCTb']"
pesosElementPath  = "//span[@class='DFlfde SwHCTb']"
euroElementPath   = '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
goldElementPath   = '//*[@id="main"]/div/div/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/h2/em'

#Code
# Acess Chrome
driver = webdriver.Chrome()

# Get Values from website using getValues method
dollarValue = getValue(driver,dollarPagePath,dollarElementPath)
pesosValue  = getValue(driver,pesosPagePath,pesosElementPath)
euroValue   = getValue(driver,euroPagePath,euroElementPath)
goldValue   = getValue(driver,goldPagePath,goldElementPath)


# Check values in prompt (for devs)
#print("Dollar: {}, Pesos: {}, Euro: {}, Gold: {}.".format(dollarValue ,pesosValue, euroValue, goldValue));


# Creating a spreadsheet.
workbook = openpyxl.Workbook()

workbook.active.title = 'currenciesBRLQuotation' # Rename the initial sheet
sheet_Valor_Moedas = workbook.active # Select the active sheet

# Creating line names.
sheet_Valor_Moedas['A1'].value = 'Dollar'
sheet_Valor_Moedas['B1'].value = 'Pesos'
sheet_Valor_Moedas['C1'].value = 'Euro'
sheet_Valor_Moedas['D1'].value = 'Gold'


sheet_Valor_Moedas.append([dollarValue,pesosValue,euroValue,goldValue]) # entering data into the spreadsheet.


workbook.save('automate_currencies.xlsx') # saving the spreadsheet.


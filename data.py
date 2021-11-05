from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

browser = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\ChromeDriver\chromedriver.exe")

team = "AC Milan"

get_url = browser.get(r"https://fbref.com/en/")

grab_cur_url = browser.current_url

df = pd.read_html(grab_cur_url)

tbl_fixures = 1
tbl_players = 0


def ExportCSV():
    df[tbl_players].to_csv(rf'C:\Users\User\Desktop\Repos\Footballdb data\{team}.csv')

def SquadList():
    get_url
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="header"]/div[3]/form/div/div/input[2]').send_keys(team)
    browser.find_element_by_xpath('//*[@id="header"]/div[3]/form/div/div/div/div/div[2]/div').click()
    time.sleep(2)
    grab_cur_url
    squad_list = df[tbl_players]
    global squad
    squad = squad_list['Unnamed: 0_level_0','Player'].values.tolist()
    browser.close()


def Fixures():
    fixures_list = df[tbl_fixures]
    global fixures
    fixures = fixures_list['Date'].to_list()
    print(fixures)
    browser.close()

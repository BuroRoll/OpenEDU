import requests as req
from bs4 import BeautifulSoup
from selenium import webdriver
import time


from functools import partial
from pathlib import Path

from selenium.webdriver.chrome.options import Options


class Parser(object):

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

    ROOT_DIR = Path(__file__).parents[0]
    make_path = partial(Path.joinpath, ROOT_DIR)

    driver_path = make_path('chromedriver.exe')

    driver = webdriver.Chrome(executable_path=str(driver_path))
    driver.quit()


    @staticmethod
    def get_Openedu_program(link):
        head = {'user-agent': 'Chrome'}
        resp = req.get(link, headers=head)
        start = resp.text.rfind('Программа курса</h2>')
        end = resp.text.rfind('<h2 id="result_knowledge">')
        program = resp.text[start:end].replace('Программа курса</h2>', '') \
            .replace('.', '') \
            .replace('<br>', '') \
            .replace('<p>', '') \
            .replace('</p>', '') \
            .lower()
        return program

    @staticmethod
    def get_Skillbox_program(link):
        driver = webdriver.Chrome()
        driver.get(link)
        html = driver.page_source
        driver.quit()
        soup = BeautifulSoup(html, 'html.parser')
        res = []
        for elem in soup.find_all('button', class_='accordion__button js-accordion__button'):
            for e in elem.find_all('span'):
                res.append(e.text)
        for elem in soup.find_all('button', class_='accordion__button js-accordion__button accordion__button--empty'):
            for e in elem.find_all('span'):
                res.append(e.text.lower())
        return res

    def get_Stepik_program(self, link):
        print(link)
        self.driver.get(link)
        action = webdriver.ActionChains(self.driver)
        self.driver.implicitly_wait(10)
        e = self.driver.find_elements_by_xpath(
            '//div[@class="toc-promo__section"]')
        action.pause(2000)
        while True:
            try:
                z = 0
                for i, j in enumerate(e):
                    j.click()
                    action.pause(1000)
                    z = i
                if z == len(e) - 1:
                    break
            except Exception as err:
                pass
        time.sleep(4)
        action.pause(5000)
        html = self.driver.page_source
        self.driver.quit()
        soup = BeautifulSoup(html, 'html.parser')
        res = []
        for elem in soup.find_all('div', class_='toc-promo-lesson__title'):
            data = elem.text \
                .replace('\n', '') \
                .replace('.', '') \
                .lower()
            res.append(data)

        return res

    def get_coursera_program(self, link):
        head = {'user-agent': 'Chrome'}
        resp = req.get(link, headers=head)
        soup = BeautifulSoup(resp.content, 'html.parser')
        res = []
        for p in soup.find_all('div', class_='content-inner'):
            res.append(p.text.replace('.', '').lower())
        return res

    def get_beonmax_program(self, link):
        res = []
        head = {'user-agent': 'Chrome'}
        resp = req.get(link, headers=head)
        resp.encoding = 'utf-8'
        soup = BeautifulSoup(resp.text, 'html.parser')
        for p in soup.find_all('span', class_='prog-text'):
            res.append(p.text.replace('.', '').lower())
        return res
import requests as req
from bs4 import BeautifulSoup
from selenium import webdriver


class Parser(object):
    driver = webdriver.Chrome()

    @staticmethod
    def get_Openedu_program(link):
        head = {'user-agent': 'Chrome'}
        resp = req.get(link, headers=head)
        start = resp.text.rfind('Программа курса</h2>')
        end = resp.text.rfind('<h2 id="result_knowledge">')
        program = resp.text[start:end].replace('Программа курса</h2>', '')
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
                res.append(e.text)
        return res

    @staticmethod
    def get_Stepik_program(link):
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
                res.append(e.text)
        return res

    def get_Stepik_program(self, link):
        self.driver.get(link)
        self.driver.implicitly_wait(10)
        e = self.driver.find_elements_by_xpath(
            '//div[@class="toc-promo__section"]')
        print(len(e))
        for i in e:
            i.click()
        # elem.click()
        # html = self.driver.page_source
        # self.driver.quit()
        # soup = BeautifulSoup(html, 'html.parser')
        # print(soup)

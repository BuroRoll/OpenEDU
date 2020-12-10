import requests as req


class Parser(object):
    @staticmethod
    def get_program(link):
        head = {'user-agent': 'Chrome'}
        resp = req.get(link, headers=head)
        start = resp.text.rfind('Программа курса</h2>')
        end = resp.text.rfind('<h2 id="result_knowledge">')
        program = resp.text[start:end].replace('Программа курса</h2>', '')
        return program

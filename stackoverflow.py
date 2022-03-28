import requests

from datetime import datetime
from datetime import timedelta

class StackOverFlow:

    def __init__(self):
        self.url = 'https://api.stackexchange.com/2.3/questions'

    def get_current_date(self):
        current_date = datetime.today()
        result_date = current_date.timestamp()
        return result_date

    def get_last_two_days(self):
        current_date = datetime.today()
        two_days_ago = current_date - timedelta(days=2)
        result_date = two_days_ago.timestamp()
        return result_date

    def get_new_questions(self, tag):
        params = {"fromdate": int(self.get_last_two_days()),
                  "todate": int(self.get_current_date()),
                  "sort": "creation", "tagged": tag,
                  "site": "stackoverflow"}
        response = requests.get(self.url, params=params)
        response.raise_for_status()
        for title in response.json()["items"]:
            print(title["title"])


if __name__ == '__main__':

    question_01 = StackOverFlow()
    question_01.get_new_questions('python')
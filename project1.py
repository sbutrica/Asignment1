from datetime import time

import requests

from bs4 import BeautifulSoup

text_file = open("JobInfo.txt", "a+")
URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Boston'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
job = results.find_all('section', class_='card-content')
for job_elem in job:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue


keyword = input('Please input keyword')

try:
    _ = int(keyword)
except:
    pass
    print("passed test1")
else:
    raise ValueError("Input supplied should be of type 'str' failed Test1")










keyword_jobs = results.find_all('h2',
                                string=lambda text: keyword in text.lower())

print(len(keyword_jobs))
for p_job in keyword_jobs:
    link = p_job.find('a')['href']
    print(company_elem.text.strip())
    print(p_job.text.strip(), )
    print(f"Click here to apply: {link}\n")
    text_file.write(company_elem.text.strip())
    text_file.write("Job Posted: %s\n" % p_job.text.strip(),)
    text_file.write(f"Click here to apply: {link}\n")


def title_elem(keyword):
    pass


def company_elem():
    pass


def main():
    keyword = company_elem()
    title_elem(keyword)


if __name__ == '__main__':
    print("Executed when invoked ")

else:
    print("Did not execute")


def __init__(self, create, JobInfo):
       if(create):
           self._data_fd = open(JobInfo, 'w')

def __del__(self):
       if(self._data_fd != None):
           self._data_fd.close()
text_file.close()


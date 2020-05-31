import requests

from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Boston'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
job_elems = results.find_all('section', class_='card-content')
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue

userInput = input('Please print input keyword')
userInput_jobs = results.find_all('h2',
                                  string=lambda text: userInput in text.lower())

print(len(userInput_jobs))
for p_job in userInput_jobs:
    link = p_job.find('a')['href']
    print(p_job.text.strip())
    print(f"Click here to apply: {link}\n")
    text_file = open("JobInfo.txt", "w+")
    text_file.write("Job Posted: %s\n" % p_job.text.strip())

text_file.close()


def title_elem(userInput):
    pass


def company_elem():
    pass


def main():
    userInput = company_elem()
    title_elem(userInput)


if __name__ == '__main__':
    print("Executed when invoked ")
else:
    print("Did not execute")


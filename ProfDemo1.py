import requests

#todo put these someplace safer
API_ID = '<fill yours in here>'
API_KEY = '<fill yours in here>'

def show_data(data):
    for item in data:
        if 'company' in item:
            corp = item['company']
            print(corp['display_name'])

def get_data(loc:str):
    raw_data = requests.get(loc)
    if raw_data.status_code == 200:
        data = raw_data.json()
        return data['results']
    else: #something went wrong
        return dict()


def main():
    query = f"http://api.adzuna.com/v1/api/jobs/gb/search/1?app_id={API_ID}&app_key={API_KEY}&results_per_page=1000&what=python&content-type=application/json"
    data = get_data(query)
    show_data(data)


if __name__ == '__main__':
    main()

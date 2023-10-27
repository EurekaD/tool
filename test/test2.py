import time

def fetch_data(url):
    print('start fetching', url)
    time.sleep(2)
    print('done fetching', url)
    return {'data': url}

def main():
    print('start')
    res1 = fetch_data('url1') 
    print(res1)
    res2 = fetch_data('url2')
    print(res2)
    print('results:', res1, res2)

main()
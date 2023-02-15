import schedule 
import requests

def greeting():
    todos_dict = {
        '08:00': 'Drink Cofee',
        '11:00': 'Work Meeting'
    }
    
    print("Days's tasks")
    for k, v in todos_dict.items():
        print(f'{k}-{v}')
        
        response = requests.get(url='https://yobit.net/api/3/ticker/btc_usd')
        data = response.json()
        btc_price = f"BTC: {round(data.get('btc_cb').get('last')), 2}$"
        print(btc_price)
        
def main():
    greeting()
    
if __name__ == '__main__':
   main()
import requests
from django.shortcuts import render
from django.views import View
from bs4 import BeautifulSoup

# Create your views here.
class Get_top_100(View):

    def get(self, request):

        limit = 100
        token_contract_address = '0xf3Db5Fa2C66B7aF3Eb0C0b782510816cbe4813b8'
        url = f'https://api.ethplorer.io/getTopTokenHolders/{token_contract_address}?apiKey=freekey&limit={limit}'
        # apikey = '2T7884KTXWP64WEDUQWVFTXNQRNAGDYERZ'
        # url = f'https://api.etherscan.io/api?module=account&action=txlist&address=0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a&startblock=0&endblock=99999999&page=1&offset={offset}&sort=asc&apikey={apikey}'

        res = requests.get(url)

        results = res.json().get('holders')

        address_list = []
        balance_list = []

        for r in results:
            address_list.append(r['address'])
            balance_list.append(r['balance'])

        # print(address_list)
        # print(balance_list)

        return render(request, 'index.html', context={'address': address_list,
                                                      'balance': balance_list
                                                      })

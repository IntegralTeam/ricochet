import json
from brownie import accounts, StreamExchangeHelper

def main():
    with open('scripts\jsonArgs\DistributeArgs.json', 'r') as parser:
        parseArgs = json.load(parser)

    StreamExchangeInstance = StreamExchange.at(parseArgs['address'])
    
    try:
        print('Executing distribute function for StreamExchange contract at ', StreamExchangeInstance.address,'...')
        StreamExchangeInstance.distribute({'from': accounts[0]})
        print('Distribute function executed for StreamExchange contract at ', StreamExchangeInstance.address)
    except Exception as error:
        print('Error for StreamExchange contract at ', StreamExchangeInstance.address,':', error)
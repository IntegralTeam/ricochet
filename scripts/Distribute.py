import json
from brownie import accounts, StreamExchange

def main():
    with open('.\jsonArgs\DistributeArgs.json', 'r') as parser:
        parseArgs = json.load(parser)

    stream_exchange_instance = StreamExchange.at(parseArgs['address'])

    try:
        print('Executing distribute function for StreamExchange contract at ', stream_exchange_instance.address,'...')
        stream_exchange_instance.distribute({'from': accounts[0]})
        print('Distribute function executed for StreamExchange contract at ', stream_exchange_instance.address)
    except Exception as error:
        print('Error for StreamExchange contract at ', stream_exchange_instance.address,':', error)

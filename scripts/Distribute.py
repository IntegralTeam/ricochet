import json
from brownie import accounts, StreamExchange

def main():
    with open('scripts\jsonArgs\DistributeArgs.json', 'r') as parser:
        parse_args = json.load(parser)

    stream_exchange_instance = StreamExchange.at(parse_args['address'])

    try:
        print('Executing distribute function for StreamExchange contract at ', stream_exchange_instance.address,'...')
        stream_exchange_instance.distribute({'from': accounts[0]})
        print('Distribute function executed for StreamExchange contract at ', stream_exchange_instance.address)
    except Exception as error:
        print('Error for StreamExchange contract at ', stream_exchange_instance.address,':', error)

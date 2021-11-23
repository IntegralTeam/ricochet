import json
from brownie import accounts, StreamExchange

def main():
    with open('scripts\jsonArgs\setOracleArgs.json', 'r') as parser:
        parse_args = json.load(parser)

    stream_exchange_instance = StreamExchange.at(parse_args['address'])

    try:
        print('Current Tellor oracle address: ', stream_exchange_instance.getTellorOracle({'from': accounts[0]}))
        print('Setting Tellor oracle address for StreamExchange at ', stream_exchange_instance.address, '...')
        stream_exchange_instance.setOracle(parse_args['oracle'], {'from': accounts[0]})
        print('New Tellor oracle address for StreamExchange at ', stream_exchange_instance.address, ' set to ', stream_exchange_instance.getTellorOracle({'from': accounts[0]}))
    except Exception as error:
        print('Error for StreamExchange contract at ', stream_exchange_instance.address, ': ', error)

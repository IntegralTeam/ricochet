import json
from brownie import accounts

def main():
    with open('.\jsonArgs\SetRateToleranceArgs.json', 'r') as parser:
        parse_args = json.load(parser)

    stream_exchange_instance = StreamExchange.at(parse_args['address'])

    try:
        print('Current rate tolerance: %s', stream_exchange_instance.getRateTolerance({'from': accounts[0]}))
        print('Setting rate tolerance to: %s...', parse_args['rate'])
        stream_exchange_instance.setRateTolerance(parse_args['rate'], {'from': accounts[0]})
        print('Rate tolerance set to %s', stream_exchange_instance.getRateTolerance({'from': accounts[0]}))
    except Exception as error:
        print('Error for StreamExchange contract at %s: %s', stream_exchange_instance.address, error)

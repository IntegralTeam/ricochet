import json
from brownie import accounts, StreamExchange

def main():
    with open('.\jsonArgs\SetSubsidyRateArgs.json', 'r') as parser:
        parse_args = json.load(parser)

    stream_exchange_instance = StreamExchange.at(parse_args['address'])

    try:
        print('Current subsidy rate: %s', stream_exchange_instance.getSubsidyRate({'from': accounts[0]}))
        print('Setting subsidy rate to: %s...', parse_args['rate'])
        stream_exchange_instance.setSubsidyRate(parse_args['rate'], {'from': accounts[0]})
        print('Subsidy rate set to %s', stream_exchange_instance.getSubsidyRate({'from': accounts[0]}))
    except Exception as error:
        print('Error for StreamExchange contract at %s: %s', stream_exchange_instance.address, error)

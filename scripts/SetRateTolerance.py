import json
from brownie import accounts

def main():
    with open('scripts\jsonArgs\SetRateToleranceArgs.json', 'r') as parser:
        parseArgs = json.load(parser)

    StreamExchangeInstance = StreamExchange.at(parseArgs['address'])

    try:
        print('Current rate tolerance: %s', StreamExchangeInstance.getRateTolerance('from': accounts[0]))
        print('Setting rate tolerance to: %s...', parseArgs['rate'])
        StreamExchangeInstance.setRateTolerance(parseArgs['rate'], 'from': accounts[0])
        print('Rate tolerance set to %s', StreamExchangeInstance.getRateTolerance('from': accounts[0]))
    except Exception as error:
        print('Error for StreamExchange contract at %s: %s', StreamExchangeInstance.address, error)
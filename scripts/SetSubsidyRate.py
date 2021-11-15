import json
from brownie import accounts

def main():
    with open('scripts\jsonArgs\SetSubsidyRateArgs.json', 'r') as parser:
        parseArgs = json.load(parser)

    StreamExchangeInstance = StreamExchange.at(parseArgs['address'])

    try:
        print('Current subsidy rate: %s', StreamExchangeInstance.getSubsidyRate('from': accounts[0]))
        print('Setting subsidy rate to: %s...', parseArgs['rate'])
        StreamExchangeInstance.setSubsidyRate(parseArgs['rate'], 'from': accounts[0])
        print('Subsidy rate set to %s', StreamExchangeInstance.getSubsidyRate('from': accounts[0]))
    except Exception as error:
        print('Error for StreamExchange contract at %s: %s', StreamExchangeInstance.address, error)
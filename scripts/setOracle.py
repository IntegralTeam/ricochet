import json
from brownie import accounts

def main():
    with open('scripts\jsonArgs\setOracleArgs.json', 'r') as parser:
        parseArgs = json.load(parser)

    StreamExchangeInstance = StreamExchange.at(parseArgs['address'])

    try:
        print('Current Tellor oracle address: %s', StreamExchangeInstance.getTellorOracle('from': accounts[0]))
        print('Setting Tellor oracle address for StreamExchange at %s...', StreamExchangeInstance.address)
        StreamExchangeInstance.setOracle(parseArgs['oracle'], 'from': accounts[0])
        print('New Tellor oracle address for StreamExchange at %s set to %s', StreamExchangeInstance.address, StreamExchangeInstance.getTellorOracle('from': accounts[0]))
    except Exception as error:
        print('Error for StreamExchange contract at %s: %s', StreamExchangeInstance.address, error)
import json
from brownie import accounts

def main():
    with open('scripts\jsonArgs\TransferOwnershipArgs.json', 'r') as parser:
        parseArgs = json.load(parser)

    StreamExchangeInstance = StreamExchange.at(parseArgs['address'])

    try:
        print('Current owner: %s', StreamExchangeInstance.owner('from': accounts[0]))
        StreamExchangeInstance.transferOwnership(parseArgs['owner'], 'from': accounts[0])
        print('New owner: %s',  StreamExchangeInstance.owner('from': accounts[0]))
    except Exception as error:
        print('Error for StreamExchange contract at %s: %s', StreamExchangeInstance.address, error)
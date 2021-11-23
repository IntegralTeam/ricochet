import json
from brownie import accounts, StreamExchange

def main():
    with open('scripts\jsonArgs\TransferOwnershipArgs.json', 'r') as parser:
        parse_args = json.load(parser)

    stream_exchange_instance = StreamExchange.at(parse_args['address'])

    try:
        print('Current owner: ', stream_exchange_instance.owner({'from': accounts[0]}))
        stream_exchange_instance.transferOwnership(parse_args['owner'], {'from': accounts[0]})
        print('New owner: ',  stream_exchange_instance.owner({'from': accounts[0]}))
    except Exception as error:
        print('Error for StreamExchange contract at ', stream_exchange_instance.address, ': ', error)

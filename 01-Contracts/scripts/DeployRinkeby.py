import json
from brownie import StreamExchangeHelper, StreamExchange, accounts


HOST_ADDRESS = "0x3D7CD28EfD08FfE9Ce8cA329EC2e67822C756526"
CFA_ADDRESS = "0xF4C5310E51F6079F601a5fb7120bC72a70b96e2A"
IDA_ADDRESS = "0x32E0ecb72C1dDD92B007405F8102c1556624264D"
RIC_CONTRACT_ADDRESS = "0x369A77c1A8A38488cc28C2FaF81D2378B9321D8B"

def main():
    with open('scripts\jsonArgs\DeployRinkebyArgs.json', 'r') as parser:
        parse_args = json.load(parser)

    stream_exchage_helper_instance = StreamExchangeHelper.deploy({'from': accounts[0]})
    print("Deployed StreamExchangeHelper at: ", stream_exchage_helper_instance.address)

    stream_exchange_instance = StreamExchange.deploy(
        HOST_ADDRESS,
        CFA_ADDRESS,
        IDA_ADDRESS,
        parse_args['input'],
        parse_args['output'],
        RIC_CONTRACT_ADDRESS,
        parse_args['router'],
        parse_args['oracle'],
        parse_args['requestid'],
        "",
        {'from': accounts[0]}
    )
    print("Deployed StreamExchange at: ", stream_exchange_instance.address)

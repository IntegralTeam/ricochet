import json
from brownie import StreamExchangeHelper, StreamExchange, accounts


HOST_ADDRESS = "0x3E14dC1b13c488a8d5D310918780c983bD5982E7"
CFA_ADDRESS = "0x6EeE6060f715257b970700bc2656De21dEdF074C"
IDA_ADDRESS = "0xB0aABBA4B2783A72C52956CDEF62d438ecA2d7a1"
RIC_CONTRACT_ADDRESS = "0x263026e7e53dbfdce5ae55ade22493f828922965"

def main():
    with open('.\jsonArgs\DeployRinkebyArgs.json', 'r') as parser:
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

import json
from brownie import StreamExchangeHelper, StreamExchange, accounts


HOST_ADDRESS = "0x3E14dC1b13c488a8d5D310918780c983bD5982E7"
CFA_ADDRESS = "0x6EeE6060f715257b970700bc2656De21dEdF074C"
IDA_ADDRESS = "0xB0aABBA4B2783A72C52956CDEF62d438ecA2d7a1"
RIC_CONTRACT_ADDRESS = "0x263026e7e53dbfdce5ae55ade22493f828922965"

def main(): 
    with open('scripts\jsonArgs\DeployPolygonArgs.json', 'r') as parser:
        parseArgs = json.load(parser)

    StreamExchangeHelperInstance = StreamExchangeHelper.deploy({'from': accounts[0]})
    print("Deployed StreamExchangeHelper at: ", StreamExchangeHelperInstance.address)

    StreamExchangeInstance = StreamExchange.deploy(
        HOST_ADDRESS, 
        CFA_ADDRESS, 
        IDA_ADDRESS, 
        parseArgs['input'], 
        parseArgs['output'], 
        RIC_CONTRACT_ADDRESS, 
        parseArgs['router'], 
        parseArgs['oracle'], 
        parseArgs['requestid'], 
        parseArgs['key'], 
        {'from': accounts[0]}
        )
    print("Deployed StreamExchange at: ", StreamExchangeInstance.address)
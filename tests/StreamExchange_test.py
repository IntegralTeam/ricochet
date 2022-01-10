########################
# THIS TEST SCRIPT REQUIRES Superfluid JS-SDK translation
########################

from web3 import Web3
# from brownie import StreamExchange, StreamExchangeHelper, ISuperfluid, accounts, Contract
from brownie import accounts, network, Contract
from datetime import datetime
import pytest

network.connect('polygon-main-alchemy-fork')

##########################################
# ALL ADDRESSES ARE FROM POLYGON
##########################################

names = ['Admin', 'Alice', 'Bob', 'Carl', 'Spender']

ric = None
usdc = None
app = None
tp = None # Tellor playground

ricAddress = '0x263026e7e53dbfdce5ae55ade22493f828922965'
u = dict() # object with all users
aliases = dict()

spender = None

SF_HOST = '0x3E14dC1b13c488a8d5D310918780c983bD5982E7'

SF_RESOLVER = '0xE0cc76334405EE8b39213E620587d815967af39C'
RIC_TOKEN_ADDRESS = '0x263026E7e53DBFDce5ae55Ade22493f828922965'
SUSHISWAP_ROUTER_ADDRESS = '0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff'
TELLOR_ORACLE_ADDRESS = '0xACC2d27400029904919ea54fFc0b18Bf07C57875'
TELLOR_REQUEST_ID = 60

# random address from polygonscan that have a lot of usdcx
USDCX_SOURCE_ADDRESS = '0x02757cf1281db2f16b08b90636d11db3a5f6d09a'

CARL_ADDRESS = '0x8c3bf3EB2639b2326fF937D041292dA2e79aDBbf'
BOB_ADDRESS = '0x00Ce20EC71942B41F50fF566287B811bbef46DC8'
ALICE_ADDRESS = '0x9f348cdD00dcD61EE7917695D2157ef6af2d7b9B'
OWNER_ADDRESS = '0x3226C9EaC0379F04Ba2b1E1e1fcD52ac26309aeA'

CFA_ADDRESS = ''

carl = accounts.at(CARL_ADDRESS, force=True)
bob = accounts.at(BOB_ADDRESS, force=True)
alice = accounts.at(ALICE_ADDRESS, force=True)
owner = accounts.at(OWNER_ADDRESS, force=True)

oraclePrice = None

wbtc = Contract.from_explorer("0x1BFD67037B42Cf73acF2047067bd4F2C47D9BfD6")
ethx = Contract.from_explorer("0x27e1e4e6bc79d93032abef01025811b7e4727e85")
wbtcx = Contract.from_explorer("0x4086ebf75233e8492f1bcda41c7f2a8288c2fb92")
usdcx = Contract.from_explorer("0xcaa7349cea390f89641fe306d93591f87595dc1f")

appBalances = {
    'ethx': [],
    'wbtcx': [],
    'daix': [],
    'usdcx': [],
    'ric': [],
}
ownerBalances = {
    'ethx': [],
    'wbtcx': [],
    'daix': [],
    'usdcx': [],
    'ric': [],
}
aliceBalances = {
    'ethx': [],
    'wbtcx': [],
    'daix': [],
    'usdcx': [],
    'ric': [],
}
bobBalances = {
    'ethx': [],
    'wbtcx': [],
    'daix': [],
    'usdcx': [],
    'ric': [],
}


class CFA:


    def __init__(self, superfluid, cfa):
        self.superfluid = superfluid
        self.cfa = cfa


    def deleteFlow(self, superToken, sender, receiver, by, userData, onTransaction=lambda: pass):
        resultingBy = by if by == None else sender
        userData = userData if userData != None else "0x"
        self.superfluid.callAgreement(
            cfa.address,
            cfa.encodeABI(fn_name="deleteFlow", args=[
                superToken, sender, receiver, "0x"
            ]),
            userData,
            {
                "from": resultingBy
            }
        )


    def sanitizeFlowInfo(self, flowInfo):
        return {
            'timestamp': flowInfo.times
        }


    def getFlow(self, superToken, sender, receiver):
        result = self.cfa.getFlow(superToken, sender, receiver)
        return self.sanitizeFlowInfo(result )


    def updateFlow(self):
        ...


    def createFlow(self):
        ...


class User:


    def __init__(self, cfa, address, token):
        self.cfa = cfa
        self.address = address
        self.token = token


    def flow(self, recipient, flowRate, options):
        if flowRate == '0':
            cfa.deleteFlow(options)

# for i in range(len(names)):
#     u[names[i].lower()] =

@pytest.fixture(autouse=True)
def isolation(fn_isolation):
    pass

# def web3tx(fn, msg):
#     def result():
#         ...
#     return result

# def approveSubscriprions(users = [alice, bob, owner], tokens = [wbtcx, ricAddress]): # [accounts[1].address, accounts[2].address, accounts[0].address]
#     print('Approving subscriptions...')
#     sf = Contract.from_explorer(SF_HOST)
#     for tokenIndex in range(0, len(tokens) - 1):
#         for userIndex in range(0, len(users) - 1):
#             index = 0
#             if (tokens[tokenIndex] == ricAddress):
#                 index = 1
#             sf.agreements.ida =
#             sf.callAgreement()
#             await web3tx(
#               sf.host.callAgreement,
#               `${users[userIndex]} approves subscription to the app ${tokens[tokenIndex]} ${index}`,
#             )(
#               sf.agreements.ida.address,
#               sf.agreements.ida.contract.methods
#                 .approveSubscription(tokens[tokenIndex], app.address, tokenIndex, '0x')
#                 .encodeABI(),
#               '0x', # user data
#               {
#                 from: users[userIndex],
#               },
#             );
#             #web3tx?
#     # contract_instance = Contract.at('0x3E14dC1b13c488a8d5D310918780c983bD5982E7')
#
#
# def takeMeasurements():
#     appBalances.ethx.push(str(ethx.balanceOf(app.address)))
#     ownerBalances.ethx.push(str(ethx.balanceOf(owner.address)))
#     aliceBalances.ethx.push(str(ethx.balanceOf(alice.address)))
#     bobBalances.ethx.push(str(ethx.balanceOf(bob.address)))
#
#     appBalances.wbtcx.push(str(wbtcx.balanceOf(app.address)))
#     ownerBalances.wbtcx.push(str(wbtcx.balanceOf(owner.address)))
#     aliceBalances.wbtcx.push(str(wbtcx.balanceOf(alice.address)))
#     bobBalances.wbtcx.push(str(wbtcx.balanceOf(bob.address)))
#
#     appBalances.usdcx.push(str(usdcx.balanceOf(app.address)))
#     ownerBalances.usdcx.push(str(usdcx.balanceOf(owner.address)))
#     aliceBalances.usdcx.push(str(usdcx.balanceOf(alice.address)))
#     bobBalances.usdcx.push(str(usdcx.balanceOf(bob.address)))
#
#     appBalances.ric.push(str(ric.balanceOf(app.address)))
#     ownerBalances.ric.push(str(ric.balanceOf(owner.address)))
#     aliceBalances.ric.push(str(ric.balanceOf(alice.address)))
#     bobBalances.ric.push(str(ric.balanceOf(bob.address)))
#
#
# def test_should_be_correctly_configured():
#     assert (app.isAppJailed()) == False
#     assert (app.getInputToken()) == usdcx.address
#     assert (app.getOutputToken()) == wbtcx.address
#     assert (app.getOutputIndexId()) == 0
#     assert (app.getSubsidyToken()) == ric.address
#     assert (app.getSubsidyIndexId()) == 1
#     assert (app.getSubsidyRate()) == '400000000000000000'
#     assert (app.getTotalInflow()) == 0
#     assert (app.getSushiRouter()) == SUSHISWAP_ROUTER_ADDRESS
#     assert (app.getTellorOracle()) == TELLOR_ORACLE_ADDRESS
#     assert (app.getRequestId()) == 60
#     assert (app.getOwner()) == owner.address
#     assert (app.getFeeRate()) == 20000
#
# def test_should_create_a_stream_exchange_with_the_correct_parameters():
#     inflowRate = '77160493827160'
#     inflowRateIDAShares = '77160'
#
#     approveSubscriprions([owner.address])
#     owner.flow({flowRate: inflowRate, recipient: app})
#
#     assert (app.getStreamRate(owner.address)) == inflowRate
#     assert str(app.getIDAShares(0, owner.address)) == 'True,True,77160,0'
#
# def test_approval_should_be_unlimited():
#     approveSubscriprions()
#     assert (wbtc.allowance(app.address, SUSHISWAP_ROUTER_ADDRESS)) == ethers.constants.MaxUint256
#     assert (usdc.allowance(app.address, SUSHISWAP_ROUTER_ADDRESS)) == ethers.constants.MaxUint256
#     assert (wbtc.allowance(app.address, wbtcx.address)) == ethers.constants.MaxUint256
#     assert (usdc.allowance(app.address, usdcx.address)) == ethers.constants.MaxUint256
#
# def test_should_let_keepers_close_streams_with_less_than_8_hours_left():
#     approveSubscriprions([bob.address])
#     bobUsdcxBalance = usdcx.balanceOf(bob.address)
#     initialDeposit = bobUsdcxBalance / 13 * 4
#     inflowRate = str((bobUsdcxBalance - initialDeposit) / (9 * 3600))
#     bob.flow({flowRate: inflowRate, recipient: app })
#
#     assert app.getStreamRate(bob.address) == inflowRate
#
#     with brownie.revert('!closable'):
#         app.closeStream(bob.address)
#
#     brownie.chain.sleep(3600)
#
#     app.closeStream(bob.address)
#     assert (app.getStreamRate(bob.address)) == '0'
#
# def test_should_distribute_tokens_to_streamers():
#     approveSubscriprions([alice, bob])
#
#     usdcx.transfer(alice.address, 400*(10**18), {'from': spender})
#     usdcx.transfer(bob.address, 400*(10**18), {'from': spender})
#
#     checkBalances([alice, bob])
#
#     inflowRate = '1000000000000000'
#     inflowRatex2 = '2000000000000000'
#     inflowRateIDAShares = '1000000'
#     inflowRateIDASharesx2 = '2000000'
#
#     alice.flow({flowRate: inflowRate, recipient: app })
#     bob.flow({ flowRate: inflowRatex2, recipient: app })
#
#     assert (app.getStreamRate(alice.address)) == inflowRate
#     assert str(app.getIDAShares(0, alice.address)) == 'True,True,1000000,0'
#     assert (app.getStreamRate(bob.address)) == inflowRatex2
#     assert str(app.getIDAShares(0, bob.address)) == 'True,True,2000000,0'
#
#     brownie.chain.sleep(3600)
#     tp.submitValue(60, oraclePrice)
#     app.distribute()
#     checkBalances([alice.address, bob.address])
#
#     takeMeasurements()
#     delta('alice', aliceBalances)
#     delta('bob', bobBalances)
#
# def test_getters_and_setters_should_work_properly():
#     app.setFeeRate(30000, {'from': owner})
#     app.setRateTolerance(30000, {'from': owner})
#     app.setSubsidyRate('500000000000000000', {'from': owner})
#     app.setOracle(owner.address, {'from': owner})
#     app.setRequestId(61, {'from': owner})
#     app.transferOwnership(alice.address, {'from': owner})
#
#     assert (app.getSubsidyRate()) == '500000000000000000'
#     assert (app.getFeeRate()) == 30000
#     assert (app.getRateTolerance()) == 30000
#     assert (app.getTellorOracle()) == owner.address
#     assert (app.getRequestId()) == 61
#     assert (app.getOwner()) == alice.address
#
# def test_should_correctly_emergency_drain():
#     approveSubscriprions([bob.address])
#     inflowRate = '77160493827160'
#     bob.flow({flowRate: inflowRate, recipient : app})#?
#     brownie.chain.sleep(60*60*12)
#
#     assert str(usdcx.balanceOf(app.address)) != '0'
#     with brownie.revert('!zeroStreamers'):
#         app.emergencyDrain()
#
#     bob.flow({ flowRate: '0', recipient: app })#?
#     app.emergencyDrain()
#
#     assert str(usdcx.balanceOf(app.address)) == '0'
#     assert str(wbtcx.balanceOf(app.address)) == '0'
#
# def test_should_emergency_close_stream_if_app_jailed():
#     inflowRate = '100000000'
#     owner.flow({ flowRate: inflowRate, recipient: app })#?
#     assert (app.getStreamRate(owner.address)) == inflowRate
#     with brownie.revert('!jailed'):
#         app.emergencyCloseStream(owner.address)
#
#     #w3 = Web3(Web3.EthereumTesterProvider())
#     #w3.eth.default_account = '0xF4C5310E51F6079F601a5fb7120bC72a70b96e2A'
#     #contract_instance = Contract('0x3E14dC1b13c488a8d5D310918780c983bD5982E7')
#     #contract_instance.jailApp('0x', app.address, 0, {'from': "0xF4C5310E51F6079F601a5fb7120bC72a70b96e2A"})
#
#     assert (SF_HOST.isAppJailed(app.address)) == True
#     app.emergencyCloseStream(owner.address)
#     assert (app.getStreamRate(owner.address)) == '0'
#
# def test_should_distribute_tokens_to_streamers_correctly():
#     inflowRate1 = '77160493827160'
#     inflowRate2 = '964506172839506'
#     inflowRate3 = '38580246913580'
#     inflowRateIDAShares1 = '77160'
#     inflowRateIDAShares2 = '964506'
#     inflowRateIDAShares3 = '38580'
#
#     approveSubscriprions()
#
#     usdcx.transfer(bob.address, 400*(10**18), {'from': spender.address})
#     usdcx.transfer(alice.address, 400*(10**18), {'from': spender.address})
#     usdcx.transfer(owner.address, 400*(10**18), {'from': spender.address})
#
#     takeMeasurements()
#
#     with brownie.revert('!enoughTokens'):
#         owner.flow({ flowRate: 10000*(10**18), recipient: app })#?
#
#     owner.flow({ flowRate: inflowRate1, recipient: app })#?
#
#     assert (app.getStreamRate(owner.address)) == inflowRate1
#     assert str(app.getIDAShares(0, owner.address)) == 'True,True,77160,0'
#     brownie.chain.sleep(60*60*12)
#     tp.submitValue(60, oraclePrice)
#     app.distribute()
#     brownie.chain.sleep(60*60*1)
#     tp.submitValue(60, oraclePrice)
#
#     owner.flow({ flowRate: inflowRate2, recipient: app })#?
#     assert (app.getStreamRate(owner.address)) == inflowRate2
#     assert str(app.getIDAShares(0, owner.address)) == 'True,True,964506,0'
#     assert str(app.getIDAShares(0, owner.address)) == 'True,True,964506,0'
#     brownie.chain.sleep(60*60*2)
#     tp.submitValue(60, oraclePrice)
#     app.distribute()

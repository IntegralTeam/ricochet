from web3 import Web3
from chai import Chai
from brownie.network.state import Chain
from brownie import StreamExchange, StreamExchangeHelper, MockERC20, MockSuperToken, MockSuperfluid, accounts
from datetime import datetime
import pytest


sf
daix
ethx
wbtc
wbtcx
usdcx
ric
usdc
app
tp # Tellor playground
ricAddress = '0x263026e7e53dbfdce5ae55ade22493f828922965'
owner = accounts[0]
alice = accounts[1]
bob = accounts[2]
carl = accounts[3]
spender = accounts[4].address = USDCX_SOURCE_ADDRESS
SF_HOST = '0x3E14dC1b13c488a8d5D310918780c983bD5982E7'
SF_RESOLVER = '0xE0cc76334405EE8b39213E620587d815967af39C'
RIC_TOKEN_ADDRESS = '0x263026E7e53DBFDce5ae55Ade22493f828922965'
SUSHISWAP_ROUTER_ADDRESS = '0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff'
TELLOR_ORACLE_ADDRESS = '0xACC2d27400029904919ea54fFc0b18Bf07C57875'
TELLOR_REQUEST_ID = 60
USDCX_SOURCE_ADDRESS = '0x02757cf1281db2f16b08b90636d11db3a5f6d09a'
CARL_ADDRESS = '0x8c3bf3EB2639b2326fF937D041292dA2e79aDBbf'
BOB_ADDRESS = '0x00Ce20EC71942B41F50fF566287B811bbef46DC8'
ALICE_ADDRESS = '0x9f348cdD00dcD61EE7917695D2157ef6af2d7b9B'
OWNER_ADDRESS = '0x3226C9EaC0379F04Ba2b1E1e1fcD52ac26309aeA'
oraclePrice

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

        
@pytest.fixture(scope="module", autouse=True)

def before():
    accountsArray = [owner, alice, bob, carl, spender]

    sf = MockSuperfluid.deploy({'from': owner})

    mock_eth = MockERC20.deploy('name1', 'symbol1', {'from': owner})
    ethx = MockSuperToken.deploy({'from': owner})
    ethx.setInputToken(mock_eth.address)

    mock_wbtc = MockERC20.deploy('name2', 'symbol2', {'from': owner})
    wbtcx = MockSuperToken.deploy({'from': owner})
    wbtcx.setInputToken(mock_wbtc.address)

    mock_daix = MockERC20.deploy('name3', 'symbol3', {'from': owner})
    daix = MockSuperToken.deploy({'from': owner})
    daix.setInputToken(mock_daix.address)

    mock_usdcx = MockERC20.deploy('name4', 'symbol4', {'from': owner})
    usdcx = MockSuperToken.deploy({'from': owner})
    usdcx.setInputToken(mock_usdcx.address)

    

    #tp = TellorPlayground()

def createSFRegistrationKey(sf, deployer):
    registrationKey
    appKey
    governance
    sfGovernanceRo
    govOwner
    sfGovernance

    registrationKey = 'testKey-{}'.format(datetime.now())
    appKey = Web3.solidityKeccak(
        web3.eth.abi.encodeParameters(
            ['string','address','string'],
            [
            'org.superfluid-finance.superfluid.appWhiteListing.registrationKey',
            str(deployer),
            registrationKey,
            ]
            )
        )

    governance = SF_HOST.getGovernance.call()
    print('SF Governance:', governance)

    sfGovernanceRo = Contract.from_abi(str(governance), SuperfluidGovernanceBase.abi)
    
    govOwner = sfGovernanceRo.owner()
    #impersonateAndSetBalance(govOwner)
    owner.transfer(govOwner, "10 ether")  #for initialization

    sfGovernance = Contract.from_abi(str(governance), SuperfluidGovernanceBase.abi, {'from': govOwner})

    sfGovernance.whiteListNewApp(SF_HOST.address, appKey)

    return registrationKey

def approveSubscriprions(users = [alice.address, bob.address, owner.address], tokens = [wbtcx.address, ricAddress]): # [accounts[1].address, accounts[2].address, accounts[0].address]
    print('Approving subscriptions...')

    for tokenIndex in range(0, len(tokens) - 1):
        for userIndex in range(0, len(users) - 1):
            index = 0
            if (tokens[tokenIndex] == ricAddress):
                index = 1

            #web3tx?
    #contract_instance = Contract.at('0x3E14dC1b13c488a8d5D310918780c983bD5982E7')

@pytest.fixture(autouse=True)
def isolation(fn_isolation):
    pass

def beforeEach():
    sed = StreamExchangeHelper.deploy({'from': owner})

    registrationKey = createSFRegistrationKey(sf, owner)

    app = StreamExchange.deploy(
        "0x3D7CD28EfD08FfE9Ce8cA329EC2e67822C756526",
        "0xF4C5310E51F6079F601a5fb7120bC72a70b96e2A",
        "0x32E0ecb72C1dDD92B007405F8102c1556624264D",
        usdcx.address,
        wbtcx.address,
        "0x369A77c1A8A38488cc28C2FaF81D2378B9321D8B",
        "0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff",
        "0xACC2d27400029904919ea54fFc0b18Bf07C57875",
        "60",
        registrationKey,
        {'from': owner}
    )

""" @pytest.fixture(scope="module", autouse=True)
def beforeEach(StreamExchangeHelper, accounts):
    a = owner.deploy(StreamExchangeHelper)
    b = owner.deploy(
        StreamExchange,
        "0x3D7CD28EfD08FfE9Ce8cA329EC2e67822C756526",
        "0xF4C5310E51F6079F601a5fb7120bC72a70b96e2A",
        "0x32E0ecb72C1dDD92B007405F8102c1556624264D",

        )
    yield a,b

@pytest.fixture(autouse=True)
def isolation(fn_isolation):
    pass """

def checkBalance(user): 
    print('Balance of ', user.address)
    print('usdcx: ', str(usdcx.balanceOf(user.address)))
    print('wbtcx: ', str(wbtcx.balanceOf(user.address)))
    
def checkBalances(accountsArray):
    for i in range(0, len(accountsArray)):
        checkBalance(accountsArray[i])
    
def delta():
    length = len(balances.wbtcx) #is len reserved?
    changeInOutToken = balances.wbtcx[length - 1] - balances.wbtcx[length - 2]
    changeInInToken = balances.usdcx[length - 1] - balances.usdcx[length - 2]

def takeMeasurements():
    appBalances.ethx.push(str(ethx.balanceOf(app.address)))
    ownerBalances.ethx.push(str(ethx.balanceOf(owner.address)))
    aliceBalances.ethx.push(str(ethx.balanceOf(alice.address)))
    bobBalances.ethx.push(str(ethx.balanceOf(bob.address)))

    appBalances.wbtcx.push(str(wbtcx.balanceOf(app.address)))
    ownerBalances.wbtcx.push(str(wbtcx.balanceOf(owner.address)))
    aliceBalances.wbtcx.push(str(wbtcx.balanceOf(alice.address)))
    bobBalances.wbtcx.push(str(wbtcx.balanceOf(bob.address)))

    appBalances.usdcx.push(str(usdcx.balanceOf(app.address)))
    ownerBalances.usdcx.push(str(usdcx.balanceOf(owner.address)))
    aliceBalances.usdcx.push(str(usdcx.balanceOf(alice.address)))
    bobBalances.usdcx.push(str(usdcx.balanceOf(bob.address)))

    appBalances.ric.push(str(ric.balanceOf(app.address)))
    ownerBalances.ric.push(str(ric.balanceOf(owner.address)))
    aliceBalances.ric.push(str(ric.balanceOf(alice.address)))
    bobBalances.ric.push(str(ric.balanceOf(bob.address)))

def test_should_be_correctly_configured():
    assert (app.isAppJailed()) == False
    assert (app.getInputToken()) == usdcx.address
    assert (app.getOutputToken()) == wbtcx.address
    assert (app.getOutputIndexId()) == 0
    assert (app.getSubsidyToken()) == ric.address
    assert (app.getSubsidyIndexId()) == 1
    assert (app.getSubsidyRate()) == '400000000000000000'
    assert (app.getTotalInflow()) == 0
    assert (app.getSushiRouter()) == SUSHISWAP_ROUTER_ADDRESS
    assert (app.getTellorOracle()) ==TELLOR_ORACLE_ADDRESS
    assert (app.getRequestId()) == 60
    assert (app.getOwner()) == owner.address #u.owner.address
    assert (app.getFeeRate()) == 20000

def test_should_create_a_stream_exchange_with_the_correct_parameters():
    inflowRate = '77160493827160'
    inflowRateIDAShares = '77160'

    approveSubscriprions([owner.address]) #u.owner.address

    owner.flow({flowRate: inflowRate, recipient: app}) #u.owner.flow___and___u.app?

    assert (app.getStreamRate(owner.address)) == inflowRate
    assert str(app.getIDAShares(0, owner.address)) == 'True,True,77160,0'

def test_approval_should_be_unlimited():
    approveSubscriprions()
    assert (wbtc.allowance(app.address, SUSHISWAP_ROUTER_ADDRESS)) == ethers.constants.MaxUint256
    assert (usdc.allowance(app.address, SUSHISWAP_ROUTER_ADDRESS)) == ethers.constants.MaxUint256
    assert (wbtc.allowance(app.address, wbtcx.address)) == ethers.constants.MaxUint256
    assert (usdc.allowance(app.address, usdcx.address)) == ethers.constants.MaxUint256

def test_should_let_keepers_close_streams_with_less_than_8_hours_left():
    approveSubscriprions([bob.address]) #u.bob.address

    bobUsdcxBalance = usdcx.balanceOf(bob.address) #u.bob.address

    initialDeposit = bobUsdcxBalance / 13 * 4
    inflowRate = str((bobUsdcxBalance - initialDeposit) / (9 * 3600))

    bob.flow({flowRate: inflowRate, recipient: app }) #u.bob.flow()____and____u.app?
    assert app.getStreamRate(bob.address) == inflowRate

    with brownie.revert('!closable'):
        app.closeStream(bob.address)
    
    brownie.chain.sleep(3600)

    app.closeStream(bob.address)
    assert (app.getStreamRate(bob.address)) == '0'

def test_should_distribute_tokens_to_streamers():
    approveSubscriprions([alice.address, bob.address]) #alice, bob

    usdcx.transfer(alice.address, 400*(10**18), {'from': spender}) #spender? toWad(400)?
    usdcx.transfer(bob.address, 400*(10**18), {'from': spender}) #spender? toWad?

    checkBalances([alice.address, bob.address]) #u.alice, u.bob

    inflowRate = '1000000000000000'
    inflowRatex2 = '2000000000000000'
    inflowRateIDAShares = '1000000'
    inflowRateIDASharesx2 = '2000000'

    alice.flow({flowRate: inflowRate, recipient: app })
    bob.flow({ flowRate: inflowRatex2, recipient: app })

    assert (app.getStreamRate(alice.address)) == inflowRate
    assert str(app.getIDAShares(0, alice.address)) == 'True,True,1000000,0' #or T in lowcase?
    assert (app.getStreamRate(bob.address)) == inflowRatex2
    assert str(app.getIDAShares(0, bob.address)) == 'True,True,2000000,0'

    brownie.chain.sleep(3600)
    tp.submitValue(60, oraclePrice)
    app.distribute()
    checkBalances([alice.address, bob.address])

    takeMeasurements()
    delta('alice', aliceBalances) #?
    delta('bob', bobBalances) #?

def test_getters_and_setters_should_work_properly():
    app.setFeeRate(30000, {'from': owner})
    app.setRateTolerance(30000, {'from': owner})
    app.setSubsidyRate('500000000000000000', {'from': owner})
    app.setOracle(owner.address, {'from': owner})
    app.setRequestId(61, {'from': owner})
    app.transferOwnership(alice.address, {'from': owner})

    assert (app.getSubsidyRate()) == '500000000000000000'
    assert (app.getFeeRate()) == 30000
    assert (app.getRateTolerance()) == 30000
    assert (app.getTellorOracle()) == owner.address
    assert (app.getRequestId()) == 61
    assert (app.getOwner()) == alice.address

def test_should_correctly_emergency_drain():
    approveSubscriprions([bob.address])
    inflowRate = '77160493827160'
    bob.flow({flowRate: inflowRate, recipient : app})#?
    brownie.chain.sleep(60*60*12)
    assert str(usdcx.balanceOf(app.address)) != '0'
    with brownie.revert('!zeroStreamers'):
        app.emergencyDrain()
    bob.flow({ flowRate: '0', recipient: app })#?
    app.emergencyDrain()
    assert str(usdcx.balanceOf(app.address)) == '0'
    assert str(wbtcx.balanceOf(app.address)) == '0'

def test_should_emergency_close_stream_if_app_jailed():
    inflowRate = '100000000'
    owner.flow({ flowRate: inflowRate, recipient: app })#?
    assert (app.getStreamRate(owner.address)) == inflowRate
    with brownie.revert('!jailed'):
        app.emergencyCloseStream(owner.address)
    
    #w3 = Web3(Web3.EthereumTesterProvider())
    #w3.eth.default_account = '0xF4C5310E51F6079F601a5fb7120bC72a70b96e2A'
    #contract_instance = Contract('0x3E14dC1b13c488a8d5D310918780c983bD5982E7')
    #contract_instance.jailApp('0x', app.address, 0, {'from': "0xF4C5310E51F6079F601a5fb7120bC72a70b96e2A"})
    """ Web3(
        SF_HOST.jailApp,#host address
        'CFA jails App',
        )
        (
        '0x',
        app.address,
        0,
        {'from': "0xF4C5310E51F6079F601a5fb7120bC72a70b96e2A"}, #CFA Address sf.agreements.cfa.address
        ) """

    assert (SF_HOST.isAppJailed(app.address)) == True
    app.emergencyCloseStream(owner.address)
    assert (app.getStreamRate(owner.address)) == '0'

def test_should_distribute_tokens_to_streamers_correctly():
    inflowRate1 = '77160493827160'
    inflowRate2 = '964506172839506'
    inflowRate3 = '38580246913580'
    inflowRateIDAShares1 = '77160'
    inflowRateIDAShares2 = '964506'
    inflowRateIDAShares3 = '38580'

    approveSubscriprions()

    usdcx.transfer(bob.address, 400*(10**18), {'from': spender.address})#? toWad
    usdcx.transfer(alice.address, 400*(10**18), {'from': spender.address})#? toWad
    usdcx.transfer(owner.address, 400*(10**18), {'from': spender.address})#? toWad

    takeMeasurements()

    with brownie.revert('!enoughTokens'):
        owner.flow({ flowRate: 10000*(10**18), recipient: app })#? toWad

    owner.flow({ flowRate: inflowRate1, recipient: app })#?

    assert (app.getStreamRate(owner.address)) == inflowRate1
    assert str(app.getIDAShares(0, owner.address)) == 'True,True,77160,0'
    brownie.chain.sleep(60*60*12)
    tp.submitValue(60, oraclePrice)
    app.distribute()
    brownie.chain.sleep(60*60*1)
    tp.submitValue(60, oraclePrice)

    owner.flow({ flowRate: inflowRate2, recipient: app })#?
    assert (app.getStreamRate(owner.address)) == inflowRate2
    assert str(app.getIDAShares(0, owner.address)) == 'True,True,964506,0'
    assert str(app.getIDAShares(0, owner.address)) == 'True,True,964506,0'
    brownie.chain.sleep(60*60*2)
    tp.submitValue(60, oraclePrice)
    app.distribute()
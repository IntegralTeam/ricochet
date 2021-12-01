from web3 import Web3
from chai import Chai
from brownie.network.state import Chain
from brownie import StreamExchange, StreamExchangeHelper, MockERC20, MockSuperToken, MockSuperfluid, accounts
import pytest
from datetime import datetime


global sf
global daix
global ethx
global wbtc
global wbtcx
global usdcx
global ric
global usdc
global app
global tp # Tellor playground
ricAddress = '0x263026e7e53dbfdce5ae55ade22493f828922965'
u = {} # object with all users
aliases = {}
global owner
global alice
global bob
global carl
global spender
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
global oraclePrice

async def createSFRegistrationKey(sf, deployer):
    global registrationKey
    global appKey
    global governance
    global sfGovernanceRo
    global govOwner
    global sfGovernance

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

    governance = await SF_HOST.getGovernance.call()
    print('SF Governance:', governance)

    sfGovernanceRo = await Contract.from_abi(str(governance), SuperfluidGovernanceBase.abi)
    
    govOwner = await sfGovernanceRo.owner()
    #impersonateAndSetBalance(govOwner)
    owner.transfer(govOwner, "10 ether")  #for initialization

    sfGovernance = await Contract.from_abi(str(governance), SuperfluidGovernanceBase.abi, {'from': govOwner})

    await sfGovernance.whiteListNewApp(SF_HOST.address, appKey)

    return registrationKey

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

async def approveSubscriprions(users = [alice.address, bob.address, owner.address], tokens = [wbtcx.address, ricAddress]):
    print('Approving subscriptions...')

    for tokenIndex in range(0, len(tokens) - 1):
        for userIndex in range(0, len(users) - 1):
            index = 0
            if (tokens[tokenIndex] == ricAddress):
                index = 1

            #await web3tx?
            await 

def before():
    owner = accounts[0]
    alice = accounts[1]
    bob = accounts[2]
    carl = accounts[3]
    spender = accounts[4].address = USDCX_SOURCE_ADDRESS
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

def beforeEach():
    sed = StreamExchangeHelper.deploy({'from': owner})

    registrationKey = await createSFRegistrationKey(sf, owner)

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

async def checkBalance(user): 
    print('Balance of ', user.address)
    print('usdcx: ', str(await usdcx.balanceOf(user.address)))
    print('wbtcx: ', str(await wbtcx.balanceOf(user.address)))
    
async def checkBalances(accountsArray):
    for i in range(0, len(accountsArray)):
        await checkBalance(accountsArray[i])
    
async def delta():
    length = len(balances.wbtcx) #is len reserved?
    changeInOutToken = balances.wbtcx[length - 1] - balances.wbtcx[length - 2]
    changeInInToken = balances.usdcx[length - 1] - balances.usdcx[length - 2]

async def takeMeasurements():
    appBalances.ethx.push(str(await ethx.balanceOf(app.address)))
    ownerBalances.ethx.push(str(await ethx.balanceOf(owner.address)))
    aliceBalances.ethx.push(str(await ethx.balanceOf(alice.address)))
    bobBalances.ethx.push(str(await ethx.balanceOf(bob.address)))

    appBalances.wbtcx.push(str(await wbtcx.balanceOf(app.address)))
    ownerBalances.wbtcx.push(str(await wbtcx.balanceOf(owner.address)))
    aliceBalances.wbtcx.push(str(await wbtcx.balanceOf(alice.address)))
    bobBalances.wbtcx.push(str(await wbtcx.balanceOf(bob.address)))

    appBalances.usdcx.push(str(await usdcx.balanceOf(app.address)))
    ownerBalances.usdcx.push(str(await usdcx.balanceOf(owner.address)))
    aliceBalances.usdcx.push(str(await usdcx.balanceOf(alice.address)))
    bobBalances.usdcx.push(str(await usdcx.balanceOf(bob.address)))

    appBalances.ric.push(str(await ric.balanceOf(app.address)))
    ownerBalances.ric.push(str(await ric.balanceOf(owner.address)))
    aliceBalances.ric.push(str(await ric.balanceOf(alice.address)))
    bobBalances.ric.push(str(await ric.balanceOf(bob.address)))

async def test_should_be_correctly_configured():
    assert (await app.isAppJailed()) == False
    assert (await app.getInputToken()) == usdcx.address
    assert (await app.getOutputToken()) == wbtcx.address
    assert (await app.getOutputIndexId()) == 0
    assert (await app.getSubsidyToken()) == ric.address
    assert (await app.getSubsidyIndexId()) == 1
    assert (await app.getSubsidyRate()) == '400000000000000000'
    assert (await app.getTotalInflow()) == 0
    assert (await app.getSushiRouter()) == SUSHISWAP_ROUTER_ADDRESS
    assert (await app.getTellorOracle()) ==TELLOR_ORACLE_ADDRESS
    assert (await app.getRequestId()) == 60
    assert (await app.getOwner()) == owner.address #u.owner.address
    assert (await app.getFeeRate()) == 20000

async def test_should_create_a_stream_exchange_with_the_correct_parameters():
    inflowRate = '77160493827160'
    inflowRateIDAShares = '77160'

    await approveSubscriprions([owner.address]) #u.owner.address

    await owner.flow({flowRate: inflowRate, recipient app}) #u.owner.flow___and___u.app?

    assert (await app.getStreamRate(owner.address)) == inflowRate
    assert str(await app.getIDAShares(0, owner.address)) == 'True,True,77160,0'

async def test_approval_should_be_unlimited():
    await approveSubscriprions()
    assert (await wbtc.allowance(app.address, SUSHISWAP_ROUTER_ADDRESS)) == ethers.constants.MaxUint256
    assert (await usdc.allowance(app.address, SUSHISWAP_ROUTER_ADDRESS)) == ethers.constants.MaxUint256
    assert (await wbtc.allowance(app.address, wbtcx.address)) == ethers.constants.MaxUint256
    assert (await usdc.allowance(app.address, usdcx.address)) == ethers.constants.MaxUint256

async def test_should_let_keepers_close_streams_with_less_than_8_hours_left():
    await approveSubscriprions([bob.address]) #u.bob.address

    bobUsdcxBalance = await usdcx.balanceOf(bob.address) #u.bob.address

    initialDeposit = bobUsdcxBalance / (new BN('13')) * (new BN('4'))
    inflowRate = str((bobUsdcxBalance - initialDeposit) / (new BN(9 * 3600)))

    await bob.flow({flowRate: inflowRate, recipient: u.app }) #u.bob.flow()____and____u.app?
    assert app.getStreamRate(bob.address) == inflowRate

    with brownie.revert('!closable'):
        await app.closeStream(bob.address)
    
    await brownie.chain.sleep(3600)

    await app.closeStream(bob.address)
    assert (await app.getStreamRate(bob.address)) == '0'

async def test_should_distribute_tokens_to_streamers():
    await approveSubscriprions(alice.address, bob.address]) #alice, bob

    await usdcx.transfer(alice.address, 400*(10**18), {'from': }) #spender? toWad(400)?
    await usdcx.transfer(bob.address, 400*(10**18), {'from': }) #spender? toWad?

    await checkBalances([alice.address, bob.address]) #u.alice, u.bob

    inflowRate = '1000000000000000'
    inflowRatex2 = '2000000000000000'
    inflowRateIDAShares = '1000000'
    inflowRateIDASharesx2 = '2000000'

    await alice.flow({flowRate: inflowRate, recipient: u.app })
    await bob.flow({ flowRate: inflowRatex2, recipient: u.app })

    assert (await app.getStreamRate(alice.address)) == inflowRate
    assert str(await app.getIDAShares(0, alice.address)) == 'True,True,1000000,0' #or T in lowcase?
    assert (await app.getStreamRate(bob.address)) == inflowRatex2
    assert str(await app.getIDAShares(0, bob.address)) == 'True,True,2000000,0'

    await brownie.chain.sleep(3600)
    await tp.submitValue(60, oraclePrice)
    await app.distribute()
    await checkBalances([alice.address, bob.address])

    await takeMeasurements()
    delta('alice', aliceBalances) #?
    delta('bob', bobBalances) #?

async def test_getters_and_setters_should_work_properly():
    await app.setFeeRate(30000, {'from': owner})
    await app.setRateTolerance(30000, {'from': owner})
    await app.setSubsidyRate('500000000000000000', {'from': owner})
    await app.setOracle(owner.address, {'from': owner})
    await app.setRequestId(61, , {'from': owner})
    await app.transferOwnership(alice.address, {'from': owner})

    assert (await app.getSubsidyRate()) == '500000000000000000'
    assert (await app.getFeeRate()) == 30000
    assert (await app.getRateTolerance()) == 30000
    assert (await app.getTellorOracle()) == owner.address
    assert (await app.getRequestId()) == 61
    assert (await app.getOwner()) == alice.address

async def test_should_correctly_emergency_drain():
    await approveSubscriprions([bob.address])
    inflowRate = '77160493827160'
    await bob.flow({flowRate: inflowRate, recipient : app})#?
    await brownie.chain.sleep(60*60*12)
    assert str(await usdcx.balanceOf(app.address)) != '0'
    with brownie.revert('!zeroStreamers'):
        await app.emergencyDrain()
    await bob.flow({ flowRate: '0', recipient: app })#?
    await app.emergencyDrain()
    assert str(await usdcx.balanceOf(app.address)) == '0'
    assert str(await wbtcx.balanceOf(app.address)) == '0'

async def test_should_emergency_close_stream_if_app_jailed():
    inflowRate = '100000000'
    await owner.flow({ flowRate: inflowRate, recipient: u.app })#?
    assert (await app.getStreamRate(owner.address)) == inflowRate
    with brownie.revert('!jailed'):
        await app.emergencyCloseStream(owner.address)
    
    await Web3(
        SF_HOST.jailApp,#host address
        'CFA jails App',
        )
            (
                '0x',
                app.address.
                0,
                {'from': "0xF4C5310E51F6079F601a5fb7120bC72a70b96e2A"}, #CFA Address sf.agreements.cfa.address
            )

    assert (await SF_HOST.isAppJailed(app.address)) == True
    await app.emergencyCloseStream(owner.address)
    assert (await app.getStreamRate(owner.address)) == '0'

async def test_should_distribute_tokens_to_streamers_correctly():
    inflowRate1 = '77160493827160'
    inflowRate2 = '964506172839506'
    inflowRate3 = '38580246913580'
    inflowRateIDAShares1 = '77160'
    inflowRateIDAShares2 = '964506'
    inflowRateIDAShares3 = '38580'

    await approveSubscriprions()

    await usdcx.transfer(bob.address, 400*(10**18), {'from': spender.address})#? toWad
    await usdcx.transfer(alice.address, 400*(10**18), {'from': spender.address})#? toWad
    await usdcx.transfer(owner.address, 400*(10**18), {'from': spender.address})#? toWad

    await takeMeasurements()

    with brownie.revert('!enoughTokens'):
        owner.flow({ flowRate: 10000*(10**18), recipient: u.app })#? toWad

    await owner.flow({ flowRate: inflowRate1, recipient: u.app })#?

    assert (await app.getStreamRate(owner.address)) == inflowRate1
    assert str(await app.getIDAShares(0, owner.address)) == 'True,True,77160,0'
    await brownie.chain.sleep(60*60*12)
    await tp.submitValue(60, oraclePrice)
    await app.distribute()
    await brownie.chain.sleep(60*60*1)
    await tp.submitValue(60, oraclePrice)

    await owner.flow({ flowRate: inflowRate2, recipient: u.app })#?
    assert (await app.getStreamRate(owner.address)) == inflowRate2
    assert str(await app.getIDAShares(0, owner.address)) == 'True,True,964506,0'
    assert str(await app.getIDAShares(0, owner.address)) == 'True,True,964506,0'
    await brownie.chain.sleep(60*60*2)
    await tp.submitValue(60, oraclePrice)
    await app.distribute()
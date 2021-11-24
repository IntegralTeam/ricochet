import "@superfluid-finance/ethereum-contracts/contracts/interfaces/superfluid/ISuperToken.sol";
import "@superfluid-finance/ethereum-contracts/contracts/interfaces/superfluid/ISuperAgreement.sol";
import "@openzeppelin/contracts/token/ERC777/IERC777.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";


contract MockInputSuperToken is ISuperToken {
 
    address public inputToken;
    address[] mockAddress = [0x1305F6B6Df9Dc47159D12Eb7aC2804d4A33173c2,
        0x27e1e4E6BC79D93032abef01025811B7E4727e85];
        
    function setInputToken(address _inputToken) public {
        inputToken = _inputToken;
    }

    function getUnderlyingToken() external view override returns(address) {
        return inputToken;
    }



    function initialize(
        IERC20 underlyingToken,
        uint8 underlyingDecimals,
        string calldata n,
        string calldata s
    ) external override{
        
    }

    function name() external view override returns (string memory){
        string memory mock = 'abc';
        return mock;
    }
    
    function symbol() external view override returns (string memory){
        string memory mock = 'a';
        return mock;
    }

    function decimals() external view override returns (uint8){
        uint8 mock = 1;
        return mock;
    }
   
    function totalSupply() external view override returns (uint256){
        uint256 mock = 1;
        return mock;
    }
    
    function balanceOf(address account) external view override returns(uint256 balance){
        uint256 mock = 1;
        return mock;
    }
    
    function transfer(address recipient, uint256 amount) external override returns (bool){
        return true;
    }

    function allowance(address owner, address spender) external override view returns (uint256){
        uint256 mock = 1;
        return mock;
    }
    
    function approve(address spender, uint256 amount) external override returns (bool){
        return true;
    }
  
    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool){
        return true;
    }
   
    function increaseAllowance(address spender, uint256 addedValue) external override returns (bool){
        return true;
    }
    
    function decreaseAllowance(address spender, uint256 subtractedValue) external override returns (bool){
        return true;
    }
    
    function granularity() external view override returns (uint256)
    {
        uint256 mock = 1;
        return mock;
    }
    
    function send(address recipient, uint256 amount, bytes calldata data) external override{

    }
   
    function burn(uint256 amount, bytes calldata data) external override{

    }
   
    function isOperatorFor(address operator, address tokenHolder) external override view returns (bool)
    {
        return true;
    }
    
    function authorizeOperator(address operator) external override{

    }
    
    function revokeOperator(address operator) external override{

    }
   
    function defaultOperators() external override view returns (address[] memory)
    {
        return  mockAddress;
    }

    function operatorSend(
        address sender,
        address recipient,
        uint256 amount,
        bytes calldata data,
        bytes calldata operatorData
    ) external override
    {

    }
    
    function operatorBurn(
        address account,
        uint256 amount,
        bytes calldata data,
        bytes calldata operatorData
    ) external override
    {

    }
    
    function selfMint(
        address account,
        uint256 amount,
        bytes memory userData
    ) external override 
    {

    }
   
   function selfBurn(
       address account,
       uint256 amount,
       bytes memory userData
   ) external override 
   {

   }
   
    function transferAll(address recipient) external override {

    }
   
    function upgrade(uint256 amount) external override {

    }
   
    function upgradeTo(address to, uint256 amount, bytes calldata data) external override {

    }
    
   
    function downgrade(uint256 amount) external override {

    }


    function operationApprove(
        address account,
        address spender,
        uint256 amount
    ) external override 
    {

    }

    function operationTransferFrom(
        address account,
        address spender,
        address recipient,
        uint256 amount
    ) external override 
    {

    }

    function operationUpgrade(address account, uint256 amount) external override {

    }

    function operationDowngrade(address account, uint256 amount) external override {

    }

    function getHost() external view override returns(address host) {
        return address(0x3E14dC1b13c488a8d5D310918780c983bD5982E7);
        }

   
    function realtimeBalanceOf(
       address account,
       uint256 timestamp
    )
        external view override
        returns (
            int256 availableBalance,
            uint256 deposit,
            uint256 owedDeposit)
    {

    }

    function realtimeBalanceOfNow(
       address account
    )
        external view override
        returns (
            int256 availableBalance,
            uint256 deposit,
            uint256 owedDeposit,
            uint256 timestamp) 
    {
               
    }

    function isAccountCritical(
        address account,
        uint256 timestamp
    )
        external view override
        returns(bool isCritical) 
    {
           
    }

    function isAccountCriticalNow(
        address account
    )
        external view override
        returns(bool isCritical) 
    {
           
    }
    
    function isAccountSolvent(
        address account,
        uint256 timestamp
    )
        external view override
        returns(bool isSolvent) 
    {

    }

    function isAccountSolventNow(
        address account
    )
        external view override
        returns(bool isSolvent) 
    {

    }

    function getAccountActiveAgreements(address account)
       external view override
       returns(ISuperAgreement[] memory activeAgreements) 
    {

    }

    function createAgreement(
        bytes32 id,
        bytes32[] calldata data
    )
        external override
    {

    }

    function getAgreementData(
        address agreementClass,
        bytes32 id,
        uint dataLength
    )
        external view override
        returns(bytes32[] memory data) 
    {

    }

    function updateAgreementData(
        bytes32 id,
        bytes32[] calldata data
    )
        external override
    {

    }
    
    function terminateAgreement(
        bytes32 id,
        uint dataLength
    )
        external override
    {

    }

    function updateAgreementStateSlot(
        address account,
        uint256 slotId,
        bytes32[] calldata slotData
    )
        external override
    {

    }

    function getAgreementStateSlot(
        address agreementClass,
        address account,
        uint256 slotId,
        uint dataLength
    )
        external view override
        returns (bytes32[] memory slotData) 
    {
        
    }

    function settleBalance(
        address account,
        int256 delta
    )
        external override
    {

    }

    function makeLiquidationPayouts
    (
        bytes32 id,
        address liquidator,
        address penaltyAccount,
        uint256 rewardAmount,
        uint256 bailoutAmount
    )
        external override
    {

    }

}
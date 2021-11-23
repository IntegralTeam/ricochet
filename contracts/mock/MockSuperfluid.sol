import "@superfluid-finance/ethereum-contracts/contracts/interfaces/superfluid/ISuperfluid.sol";


contract MockSuperfluid is ISuperfluid{

    function isApp(ISuperApp app) public view override returns(bool) {
        return false;
    }

    function getGovernance() external view override returns(ISuperfluidGovernance governance) {

    }

    function replaceGovernance(ISuperfluidGovernance newGov) external override {

    }

    function registerAgreementClass(ISuperAgreement agreementClassLogic) external override {

    }

    function updateAgreementClass(ISuperAgreement agreementClassLogic) external override {

    }

    function isAgreementTypeListed(bytes32 agreementType) external view override returns(bool yes) {

    }

    function isAgreementClassListed(ISuperAgreement agreementClass) external view override returns(bool yes) {

    }

    function getAgreementClass(bytes32 agreementType) external view override returns(ISuperAgreement agreementClass) {

    }
   
    function mapAgreementClasses(uint256 bitmap)
        external view override
        returns (ISuperAgreement[] memory agreementClasses) {

    }

    function addToAgreementClassesBitmap(uint256 bitmap, bytes32 agreementType)
        external view override
        returns (uint256 newBitmap) {

    }

    function removeFromAgreementClassesBitmap(uint256 bitmap, bytes32 agreementType)
        external view override
        returns (uint256 newBitmap) {

    }

    function getSuperTokenFactory() external view override returns (ISuperTokenFactory factory) {

    }

    function getSuperTokenFactoryLogic() external view override returns (address logic) {

    }

    function updateSuperTokenFactory(ISuperTokenFactory newFactory) external override {

    }

    function updateSuperTokenLogic(ISuperToken token) external override {

    }
 
    function registerApp(uint256 configWord) external override {

    }

    function registerAppWithKey(uint256 configWord, string calldata registrationKey) external override {

    }
  
    function getAppLevel(ISuperApp app) external view override returns(uint8 appLevel) {

    }

    function getAppManifest(
        ISuperApp app
    )
        external view override
        returns (
            bool isSuperApp,
            bool isJailed,
            uint256 noopMask
        ) {

    }

    function isAppJailed(ISuperApp app) external view override returns (bool isJail) {

    }

    function allowCompositeApp(ISuperApp targetApp) external override {

    }

    function isCompositeAppAllowed(
        ISuperApp app,
        ISuperApp targetApp
    )
        external view override
        returns (bool isAppAllowed) {

    }

    function callAppBeforeCallback(
        ISuperApp app,
        bytes calldata callData,
        bool isTermination,
        bytes calldata ctx
    )
        external override
        // onlyAgreement
        // isAppActive(app)
        returns(bytes memory cbdata) {

    }

    function callAppAfterCallback(
        ISuperApp app,
        bytes calldata callData,
        bool isTermination,
        bytes calldata ctx
    )
        external override
        // onlyAgreement
        // isAppActive(app)
        returns(bytes memory appCtx) {

    }

    function appCallbackPush(
        bytes calldata ctx,
        ISuperApp app,
        uint256 appAllowanceGranted,
        int256 appAllowanceUsed,
        ISuperfluidToken appAllowanceToken
    )
        external override
        // onlyAgreement
        returns (bytes memory appCtx) {

    }

    function appCallbackPop(
        bytes calldata ctx,
        int256 appAllowanceUsedDelta
    )
        external override
        // onlyAgreement
        returns (bytes memory newCtx) {

    }

    function ctxUseAllowance(
        bytes calldata ctx,
        uint256 appAllowanceWantedMore,
        int256 appAllowanceUsedDelta
    )
        external override
        // onlyAgreement
        returns (bytes memory newCtx) {

    }

    function jailApp(
        bytes calldata ctx,
        ISuperApp app,
        uint256 reason
    )
        external override
        // onlyAgreement
        returns (bytes memory newCtx) {

    }

     function callAgreement(
         ISuperAgreement agreementClass,
         bytes calldata callData,
         bytes calldata userData
     )
        external override
        //cleanCtx
        returns(bytes memory returnedData) {

    }

    function callAppAction(
        ISuperApp app,
        bytes calldata callData
    )
        external override
        //cleanCtx
        //isAppActive(app)
        returns(bytes memory returnedData) {

    }

    function callAgreementWithContext(
        ISuperAgreement agreementClass,
        bytes calldata callData,
        bytes calldata userData,
        bytes calldata ctx
    )
        external override
        // validCtx(ctx)
        // onlyAgreement(agreementClass)
        returns (bytes memory newCtx, bytes memory returnedData) {

    }

    function callAppActionWithContext(
        ISuperApp app,
        bytes calldata callData,
        bytes calldata ctx
    )
        external override
        // validCtx(ctx)
        // isAppActive(app)
        returns (bytes memory newCtx) {

    }

    function decodeCtx(bytes calldata ctx)
        external pure override
        returns (Context memory context) {

    }

    function isCtxValid(bytes calldata ctx) external view override returns (bool) {
        return true;
    }

    function batchCall(Operation[] memory operations) external override{

    }

    function forwardBatchCall(Operation[] memory operations) external override{

    }
}
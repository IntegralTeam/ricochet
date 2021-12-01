import "@openzeppelin/contracts/token/ERC20/ERC20.sol";


contract MockERC20 is ERC20{

    constructor(string memory _tokenName, string memory _tokenSymbol) ERC20(_tokenName, _tokenSymbol) {

    }

}
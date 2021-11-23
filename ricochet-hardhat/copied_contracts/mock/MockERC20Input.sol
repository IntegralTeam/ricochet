import "@openzeppelin/contracts/token/ERC20/ERC20.sol";


contract MockERC20Input is ERC20{

    constructor() ERC20("a", "b") {

    }

}
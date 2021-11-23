import "@openzeppelin/contracts/token/ERC20/ERC20.sol";


contract MockERC20Output is ERC20{

    constructor() ERC20("c", "d") {

    }

}
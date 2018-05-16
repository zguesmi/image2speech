pragma solidity ^0.4.11;
import "iexec-oracle-contract/contracts/IexecOracleAPI.sol";
contract MyContract is IexecOracleAPI{

    uint public constant DAPP_PRICE = 1;
    string public constant DAPP_NAME = "image2speech";
    
    function MyContract (address _iexecOracleAddress) IexecOracleAPI(_iexecOracleAddress,DAPP_PRICE,DAPP_NAME){

    }

}

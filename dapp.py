from web3 import Web3
import json

infuraRinkeby_url = "https://rinkeby.infura.io/v3/"
infuraMain_url = "https://mainnet.infura.io/v3/"
ganache_url = "HTTP://127.0.0.1:7545"
wallet_address = ""

account_1 = "0x6987D593d0f55898A0783Db044375199AF3C9a2D"
account_2 = "0xB2F2b242DF0Ca0b28C2054bb80aD6D388303ad7f"

private_key_acc1 = ""

web3 = Web3(Web3.HTTPProvider(ganache_url)) # Connect to the blockchain network

#print(web3.isConnected()) # check if we are connected or not
#balance = web3.eth.getBalance(wallet_address) # get balance of the given address
#print(balance)

## ----------------------- Interact with smart contract and use it's functions and get it's info.

"""

abi = '[{"constant":true,"inputs":[],"name":"mintingFinished","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"unpause","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"mint","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"paused","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"finishMinting","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"pause","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"},{"name":"_releaseTime","type":"uint256"}],"name":"mintTimelocked","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[],"name":"MintFinished","type":"event"},{"anonymous":false,"inputs":[],"name":"Pause","type":"event"},{"anonymous":false,"inputs":[],"name":"Unpause","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]'
# the abi information, so our script can understand how to interact with the smart contract

contract_address = "0xd26114cd6EE289AccF82350c8d8487fedB8A0C07"

contract = web3.eth.contract(address=contract_address, abi=abi) # connect to the smart contract

#print(contract)

contractTotalSupply = contract.functions.totalSupply().call() # get the total supply for the contract
print(web3.fromWei(contractTotalSupply, 'ether')) # convert the result of the contract suppploy to ether presentation.
print(contract.functions.name().call()) # get the name of the contract
print(contract.functions.symbol().call()) # get the symbol of the contract
balance = contract.functions.balanceOf(wallet_address).call() # this balanceOf is an already existed function in the smart contract, and here we are using it and checking the balance of our address
print(web3.fromWei(balance, 'ether'))
"""

## ------------------  Make a transaction using python and Ganache

"""
 "Nonce" is a portmanteau of "number used only once." It is a four-bit number added to a hashed—or encrypted—block in a blockchain that, when rehashed, meets the difficulty level restrictions. The nonce is the number that blockchain miners are solving for.
"""

"""

# get th nonce

nonce = web3.eth.getTransactionCount(account_1)

# build a transaction

transaction = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas':200000,
    'gasPrice': web3.toWei('50', 'gwei')
}

# sign transaction
signed_transaction = web3.eth.account.signTransaction(transaction, private_key_acc1)

"""

#A Bitcoin raw transaction is a chunk of bytes that contains the info about a Bitcoin transaction. That raw transaction will become part of the blockchain when a miner adds it to a block. 

"""

# send transaction
tx_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)

# get transaction hash
print(web3.toHex(tx_hash))
"""

## -------------- Interact with our contract that's deployed on remix.

"""
web3.eth.default_account = web3.eth.accounts[0]

abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"greet","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"greeting","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
address = web3.toChecksumAddress("0x0500c1eB0a5f55A35019AFD236f39518ad4103e3") # toChecksumAddress. web3. toChecksumAddress(address) Will convert an upper or lowercase Ethereum address to a checksum address.
                                     # so basically remix and ganache has a specific form of the address upper case or lowe therefore this function will adjust this.

contract = web3.eth.contract(address=address, abi=abi)
print(contract.functions.greet().call())                                  

setGeetingCall = contract.functions.setGreeting('ChangedAgain').transact()
#print(setGeetingCall)

web3.eth.waitForTransactionReceipt(setGeetingCall) # we use this to wait for a transaction to be mined.

#print(contract.functions.greet().call())

print('Updated greeting: {}'.format(
    contract.functions.greet().call()
))
"""

## ------------- Deploy smart contract using python

web3.eth.defaultAccount = web3.eth.accounts[0]

abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"greet","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"greeting","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
bytecode = "608060405234801561001057600080fd5b506040518060400160405280600581526020017f48656c6c6f0000000000000000000000000000000000000000000000000000008152506000908051906020019061005c929190610062565b50610166565b82805461006e90610105565b90600052602060002090601f01602090048101928261009057600085556100d7565b82601f106100a957805160ff19168380011785556100d7565b828001600101855582156100d7579182015b828111156100d65782518255916020019190600101906100bb565b5b5090506100e491906100e8565b5090565b5b808211156101015760008160009055506001016100e9565b5090565b6000600282049050600182168061011d57607f821691505b6020821081141561013157610130610137565b5b50919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b61055f806101756000396000f3fe608060405234801561001057600080fd5b50600436106100415760003560e01c8063a413686214610046578063cfae321714610062578063ef690cc014610080575b600080fd5b610060600480360381019061005b91906102eb565b61009e565b005b61006a6100b8565b604051610077919061036d565b60405180910390f35b61008861014a565b604051610095919061036d565b60405180910390f35b80600090805190602001906100b49291906101d8565b5050565b6060600080546100c790610443565b80601f01602080910402602001604051908101604052809291908181526020018280546100f390610443565b80156101405780601f1061011557610100808354040283529160200191610140565b820191906000526020600020905b81548152906001019060200180831161012357829003601f168201915b5050505050905090565b6000805461015790610443565b80601f016020809104026020016040519081016040528092919081815260200182805461018390610443565b80156101d05780601f106101a5576101008083540402835291602001916101d0565b820191906000526020600020905b8154815290600101906020018083116101b357829003601f168201915b505050505081565b8280546101e490610443565b90600052602060002090601f016020900481019282610206576000855561024d565b82601f1061021f57805160ff191683800117855561024d565b8280016001018555821561024d579182015b8281111561024c578251825591602001919060010190610231565b5b50905061025a919061025e565b5090565b5b8082111561027757600081600090555060010161025f565b5090565b600061028e610289846103b4565b61038f565b9050828152602081018484840111156102aa576102a9610509565b5b6102b5848285610401565b509392505050565b600082601f8301126102d2576102d1610504565b5b81356102e284826020860161027b565b91505092915050565b60006020828403121561030157610300610513565b5b600082013567ffffffffffffffff81111561031f5761031e61050e565b5b61032b848285016102bd565b91505092915050565b600061033f826103e5565b61034981856103f0565b9350610359818560208601610410565b61036281610518565b840191505092915050565b600060208201905081810360008301526103878184610334565b905092915050565b60006103996103aa565b90506103a58282610475565b919050565b6000604051905090565b600067ffffffffffffffff8211156103cf576103ce6104d5565b5b6103d882610518565b9050602081019050919050565b600081519050919050565b600082825260208201905092915050565b82818337600083830152505050565b60005b8381101561042e578082015181840152602081019050610413565b8381111561043d576000848401525b50505050565b6000600282049050600182168061045b57607f821691505b6020821081141561046f5761046e6104a6565b5b50919050565b61047e82610518565b810181811067ffffffffffffffff8211171561049d5761049c6104d5565b5b80604052505050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b600080fd5b600080fd5b600080fd5b600080fd5b6000601f19601f830116905091905056fea264697066735822122034476518dbc6fb068a73b1c45308163ade8b09c1c0df8f7203141ef14198354f64736f6c63430008070033"

Greeter = web3.eth.contract(abi=abi, bytecode=bytecode)

tx_hash = Greeter.constructor().transact()
#print(tx_hash)

tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

contract = web3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi
)

print(contract.functions.greet().call())

tx_hash = contract.functions.setGreeting('HIIIIIIIIIIIII').transact()
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

print(contract.functions.greet().call())

import web3

# Set up the Web3 providers for BNB Chain and Avalanche Chain
bnb_chain_provider = web3.providers.HttpProvider('https://bsc-dataseed.binance.org/')
avalanche_chain_provider = web3.providers.HttpProvider('https://api.avax.network/ext/bc/C/rpc')

# Define the token swap contracts
token_swap_contracts = {
    'MAMO': '0x02e7cb8b1b2844424da9979148b9374269fd0768',
    'BSC Coin': '0xe3e1147acd39687a25ca7716227c604500f5c31a',
    'AIT': '0x4238e5ccc619dcc8c00ade4cfc5d3d9020b24898',
    'Minereum AVAX': '0xf9d922c055a3f1759299467dafafdf43be844f7a'
}

# Define the function to swap all tokens to BNB
def swap_all_tokens_to_bnb(wallet_address):
    # Get the wallet balance for all tokens
    wallet_balance = {}
    for token_name, contract_address in token_swap_contracts.items():
        if token_name == 'Minereum AVAX':
            # Use Avalanche Chain provider
            web3 = avalanche_chain_provider
        else:
            # Use BNB Chain provider
            web3 = bnb_chain_provider

        # Get the token balance
        token_balance = web3.eth.get_balance(wallet_address, contract_address)
        wallet_balance[token_name] = token_balance

    # Swap all tokens to BNB
    bnb_balance = 0
    for token_name, token_balance in wallet_balance.items():
        if token_balance > 0:
            # Perform the token swap using Web3
            if token_name == 'Minereum AVAX':
                # Use Avalanche Chain provider
                web3 = avalanche_chain_provider
            else:
                # Use BNB Chain provider
                web3 = bnb_chain_provider

            # Create a transaction to swap the token
            tx = web3.eth.account.sign_transaction({
                'from': wallet_address,
                'to': token_swap_contracts[token_name],
                'value': web3.utils.to_wei(token_balance, 'ether'),
                'gas': 20000,
                'gasPrice': web3.utils.to_wei(20, 'gwei')
            }, private_key='0xYourEthereumPrivateKey')

            # Send the transaction and wait for it to be mined
            tx_hash = web3.eth.send_raw_transaction(tx.rawTransaction)
            web3.eth.wait_for_transaction_receipt(tx_hash)

            # Get the BNB balance
            bnb_balance += web3.eth.get_balance(wallet_address)

    return bnb_balance

# Test the function
wallet_address = '0xYourWalletAddress'
bnb_balance = swap_all_tokens_to_bnb(wallet_address)
print(f'Swapped all tokens to {bnb_balance} BNB')

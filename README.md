# Django Ethereum RPC Connect API


## Test Ethereum Node

> 172.31.19.85 port 8545

## To setup your own Ethereum Node

 - Install `geth` by following the official <a href="https://github.com/ethereum/go-ethereum/wiki/Building-Ethereum" target="_blank">instructions</a>
 - Start Ethereum node with RPC by running the command `geth --rpcapi="db,eth,net,web3,personal,web3" --rpc`
 
## RPC will be exposed on
 > 127.0.0.1 port 8545
 
 > If you want to change host and port, use `geth --rpcapi="db,eth,net,web3,personal,web3" --rpc --rpcaddr <ip> --rpcport <portnumber>` 

### API Documentation

API has been documented using API blueprint.

 - API blueprint file is located in `api/api.apib`
 - To build static html documentation, run `npm run-script build-docs`, static documentation is stored in `artifacts/index.html` 
 
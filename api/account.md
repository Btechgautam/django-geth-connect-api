## Personal: Account Management

The personal API manages private keys in the key store.

## Create an account [/api/account/new]

### Create a new account [POST]

Create a new account

+ Request (application/json)

    + Attributes

        + passphrase: h4ck3r (string) - Passphrase for the new account and empty passphrases are allowed
    
    + Body

        ```
        {
            "passphrase": "h4ck3r"
        }
        ```
+ Response 200 (application/json)
    
    {
        "jsonrpc": "2.0",
        "id": 1,
        "result": "0x14d3d482f867aaf6dac5bad888058d507071ed00"
    }

## Lock an account [/api/account/lock]

### Lock an account [POST] 

Lock an account

+ Request (application/json)

    + Attributes

        + address: 0x14d3d482f867aaf6dac5bad888058d507071ed00 (string) - (Private key of the account)
    
    + Body

        ```
        {
            "address": "0x14d3d482f867aaf6dac5bad888058d507071ed00"
        }
        ```
+ Response 200 (application/json)
    
    {
        "jsonrpc": "2.0",
        "id":1,
        "result":true
    }


## Unlock account [/api/account/unlock]

### Unlock an account [POST]

Unlock an account

+ Request (application/json)

    + Attributes

        + address: 0x14d3d482f867aaf6dac5bad888058d507071ed00 (string) - Private key of the account
        + passphrase: h4ck3r (string) - Passphrase of the account
        + duration: 600 (number) - optional and defaults to 300s
    
    + Body

        ```
        {
            "address": "0x14d3d482f867aaf6dac5bad888058d507071ed00",
            "passphrase": "h4ck3r",
            "duration": 600
        }
        ```
+ Response 200 (application/json)
    
    {
        "jsonrpc": "2.0",
        "id": 1,
        "result":true
    }

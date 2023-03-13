class Config:
    GANACHE_URL = "http://127.0.0.1:7545"
    ABI_ADDRESS = "0x1f440b1f4197248aeDcF58E71983ce19BCC0466b"
    ABI = [
        {
            "inputs": [
                {
                    "internalType": "string",
                    "name": "_firstName",
                    "type": "string"
                },
                {
                    "internalType": "string",
                    "name": "_lastName",
                    "type": "string"
                },
                {
                    "internalType": "int256",
                    "name": "_salary",
                    "type": "int256"
                }
            ],
            "name": "setEmployee",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "employee",
            "outputs": [
                {
                    "internalType": "string",
                    "name": "firstName",
                    "type": "string"
                },
                {
                    "internalType": "string",
                    "name": "lastName",
                    "type": "string"
                },
                {
                    "internalType": "int256",
                    "name": "salary",
                    "type": "int256"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "retrieveAll",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "string",
                            "name": "firstName",
                            "type": "string"
                        },
                        {
                            "internalType": "string",
                            "name": "lastName",
                            "type": "string"
                        },
                        {
                            "internalType": "int256",
                            "name": "salary",
                            "type": "int256"
                        }
                    ],
                    "internalType": "struct storageUserData.Employee",
                    "name": "",
                    "type": "tuple"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "retrieveFname",
            "outputs": [
                {
                    "internalType": "string",
                    "name": "",
                    "type": "string"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "retrieveLname",
            "outputs": [
                {
                    "internalType": "string",
                    "name": "",
                    "type": "string"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "retrieveSalary",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        }
    ]

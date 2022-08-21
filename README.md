
### LICENCE
```
MIT License

Copyright (c) 2022 FREDERIK NIELSEN

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Link to project
* https://github.com/freddyblockchain/Soulbound-Tokens

## Project Description
This project holds the arc-0070 proposal for soulboundable
NFTs, and an example smartcontract capable of soulbounding 
ASA NFTs. 

## Smart Contract Description

The smartcontract used in this project is created with 
pyTeal, and the code for it is in "soulbound.py". The Application id is: 102154604 and it lives on the testnet.

The smart contract has a single endpoint, that takes an asset, and validates if the asset is a soulboundable NFT, 
as per the definition in arc-0070 in this repository. 
If the asset is valid, it executes a soulbinding transaction,
as defined in arc-0070.

## Demo of soulbounding a token

https://www.youtube.com/watch?v=aPvINFTCdUc&ab_channel=FrederikNielsen

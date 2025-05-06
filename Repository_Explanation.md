# Lighter Python SDK - Comprehensive Guide

## Overview
Lighter Python is a Python SDK (Software Development Kit) for interacting with the Lighter decentralized exchange platform. This SDK provides a comprehensive set of tools and APIs for developers to interact with the Lighter platform programmatically, enabling trading, account management, and data retrieval operations.

## Prerequisites
- Python 3.8 or higher
- Basic knowledge of Python programming
- Understanding of APIs and asynchronous programming
- Familiarity with cryptocurrency trading concepts

## Installation
You can install the Lighter Python SDK directly from the GitHub repository:

```bash
pip install git+https://github.com/elliottech/lighter-python.git
```

## Repository Structure
```
├── .github/              # GitHub workflows and configuration
├── .openapi-generator/   # OpenAPI generator files
├── docs/                 # API documentation
├── examples/             # Example code demonstrating SDK usage
├── lighter/              # Main SDK package
│   ├── api/              # API client implementations
│   ├── models/           # Data models
│   ├── signers/          # Transaction signing utilities
│   ├── transactions/     # Transaction handling
│   ├── __init__.py       # Package initialization
│   ├── api_client.py     # Core API client 
│   ├── configuration.py  # SDK configuration
│   ├── exceptions.py     # Custom exceptions
│   ├── rest.py           # REST API interactions
│   ├── signer_client.py  # Client for signing operations
│   └── ws_client.py      # WebSocket client
├── test/                 # Test suite
├── LICENSE               # License information
├── README.md             # Basic usage instructions
├── openapi.json          # OpenAPI specification
├── pyproject.toml        # Project configuration
├── requirements.txt      # Dependencies
├── setup.cfg             # Setup configuration
├── setup.py              # Package setup script
└── test-requirements.txt # Test dependencies
```

## In-Depth Explanation

### Core Components

#### API Client
The `ApiClient` class in `lighter/api_client.py` is the main entry point for interacting with the Lighter API. It handles authentication, request formatting, and response parsing. The client supports both REST and WebSocket connections.

#### Configuration
The SDK's behavior can be customized using the `Configuration` class in `lighter/configuration.py`. This includes setting the API endpoint, timeouts, and authentication credentials.

#### API Modules
The SDK is organized into several API modules, each handling a specific aspect of the Lighter platform:

- `AccountApi`: Account management, including retrieving account information, API keys, and fee information
- `BlockApi`: Block-related operations, such as fetching block data and checking the current block height
- `CandlestickApi`: Market data in the form of candlesticks and funding rates
- `InfoApi`: General platform information
- `OrderApi`: Order book management, including viewing order books and placing orders
- `TransactionApi`: Transaction handling, including sending transactions and viewing transaction history

#### WebSocket Client
The `ws_client.py` module provides a WebSocket client for subscribing to real-time data feeds, such as order book updates and account balance changes.

#### Models
The `models/` directory contains data classes representing the various entities in the Lighter ecosystem, such as accounts, orders, and transactions.

### Key Functionality

1. **Account Management**: Query account information, retrieve API keys, and check fee structures
2. **Market Data**: Access real-time and historical market data, including order books, trades, and candlestick charts
3. **Order Management**: Create, modify, and cancel orders
4. **Transaction Handling**: Send transactions, check transaction status, and view transaction history
5. **WebSocket Streaming**: Subscribe to real-time data feeds for instant updates

## Usage Examples

### Basic Connection
```python
import lighter
import asyncio

async def main():
    # Create an API client
    client = lighter.ApiClient()
    
    # Use the client to interact with the API
    # ...
    
    # Close the client when done
    await client.close()

if __name__ == "__main__":
    asyncio.run(main())
```

### Account Information
```python
import lighter
import asyncio

async def main():
    client = lighter.ApiClient()
    account_api = lighter.AccountApi(client)
    
    # Get account by index
    account = await account_api.get_account(by="index", value="1")
    print(account)
    
    await client.close()

if __name__ == "__main__":
    asyncio.run(main())
```

### Order Book Data
```python
import lighter
import asyncio

async def main():
    client = lighter.ApiClient()
    order_api = lighter.OrderApi(client)
    
    # Get order book details for a specific market
    order_book = await order_api.order_book_details(market_id=0)
    print(order_book)
    
    await client.close()

if __name__ == "__main__":
    asyncio.run(main())
```

### WebSocket Streaming
```python
import lighter
import asyncio

async def main():
    client = lighter.ApiClient()
    
    # Create a WebSocket client
    ws_client = client.ws_client()
    
    # Subscribe to order book updates
    async def on_order_book(data):
        print(f"Order book update: {data}")
    
    await ws_client.subscribe_order_book(market_id=0, callback=on_order_book)
    
    # Keep the connection open for a while
    await asyncio.sleep(60)
    
    # Unsubscribe and close
    await ws_client.unsubscribe_all()
    await client.close()

if __name__ == "__main__":
    asyncio.run(main())
```

## Advanced Topics

### Transaction Signing
The SDK provides utilities for signing transactions before sending them to the Lighter platform. This is essential for security and authentication.

### Error Handling
The SDK defines custom exceptions in `exceptions.py` that provide detailed information about any errors that occur during API interactions.

### API Rate Limiting
The SDK includes built-in rate limiting to prevent exceeding the API's request limits.

## Documentation
For detailed documentation on all available API endpoints, refer to the `docs/` directory or explore the API modules directly. Each method in the API modules is documented with parameters and return types.

## Resources
- [Lighter Platform Documentation](https://mainnet.zklighter.elliot.ai)
- [OpenAPI Specification](./openapi.json)
- [Example Code](./examples/)

## License
This SDK is licensed under the terms in the [LICENSE](./LICENSE) file. 
#!/usr/bin/env python3
import asyncio
import lighter
import logging

# Set up logging to see what's happening
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('lighter-test')

async def test_lighter_sdk():
    logger.info("Starting simple test of Lighter Python SDK")
    
    # Initialize the API client with testnet
    logger.info("Initializing API client with testnet endpoint")
    client = lighter.ApiClient(
        configuration=lighter.Configuration(host="https://testnet.zklighter.elliot.ai")
    )
    
    try:
        # 1. Test basic platform info
        logger.info("Testing platform information retrieval")
        info_api = lighter.InfoApi(client)
        layer2_info = await info_api.layer2_basic_info()
        logger.info(f"Layer 2 basic info: {layer2_info}")
        
        # 2. Test order book data retrieval
        logger.info("Testing order book data retrieval")
        order_api = lighter.OrderApi(client)
        order_books = await order_api.order_books()
        logger.info(f"Found {len(order_books.order_books)} order books")
        
        # If order books exist, get details for the first one
        if order_books.order_books and len(order_books.order_books) > 0:
            first_market_id = order_books.order_books[0].market_id
            logger.info(f"Getting details for market ID: {first_market_id}")
            order_book_details = await order_api.order_book_details(market_id=first_market_id)
            logger.info(f"Order book details: {order_book_details}")
            
            # Get recent trades for this market
            recent_trades = await order_api.recent_trades(market_id=first_market_id, limit=5)
            logger.info(f"Recent trades: {recent_trades}")
        
        # 3. Test block data retrieval
        logger.info("Testing block data retrieval")
        block_api = lighter.BlockApi(client)
        
        # Get current height
        current_height = await block_api.current_height()
        logger.info(f"Current block height: {current_height.height}")
        
        # Get information about the latest block
        block = await block_api.block(by="height", value=str(current_height.height))
        logger.info(f"Latest block info: {block}")
        
        logger.info("All tests completed successfully!")
        
    except Exception as e:
        logger.error(f"Error during testing: {e}")
        raise
    finally:
        # Always close the client to clean up resources
        logger.info("Closing API client")
        await client.close()

if __name__ == "__main__":
    logger.info("Running Lighter SDK test")
    asyncio.run(test_lighter_sdk())
    logger.info("Test completed") 
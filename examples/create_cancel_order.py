import asyncio
import logging
import lighter

logging.basicConfig(level=logging.DEBUG)

# The API_KEY_PRIVATE_KEY provided belongs to a dummy account registered on Testnet.
# It was generated using the setup_system.py script, and servers as an example.
BASE_URL = "https://testnet.zklighter.elliot.ai"
API_KEY_PRIVATE_KEY = "0xc0a06468a5bbc9a7b785065a8b227a37fdfa18e2b81d51b018cb03ddd99bfbef4b7551f0f0765639"
ACCOUNT_INDEX = 595
API_KEY_INDEX = 1


def trim_exception(e: Exception) -> str:
    return str(e).strip().split("\n")[-1]


async def main():
    api_client = lighter.ApiClient(configuration=lighter.Configuration(host=BASE_URL))

    client = lighter.SignerClient(
        url=BASE_URL,
        private_key=API_KEY_PRIVATE_KEY,
        account_index=ACCOUNT_INDEX,
        api_key_index=API_KEY_INDEX,
    )

    err = client.check_client()
    if err is not None:
        print(f"CheckClient error: {trim_exception(err)}")
        return

    # create order
    tx, tx_hash, err = await client.create_order(
        market_index=0,
        client_order_index=123,
        base_amount=100000,
        price=200000,
        is_ask=True,
        order_type=lighter.SignerClient.ORDER_TYPE_LIMIT,
        time_in_force=lighter.SignerClient.ORDER_TIME_IN_FORCE_GOOD_TILL_TIME,
        reduce_only=0,
        trigger_price=0,
    )
    print(f"Create Order {tx=} {tx_hash=} {err=}")
    if err is not None:
        raise Exception(err)

    auth, err = client.create_auth_token_with_expiry(lighter.SignerClient.DEFAULT_10_MIN_AUTH_EXPIRY)
    print(f"{auth=}")
    if err is not None:
        raise Exception(err)

    active_orders = await lighter.OrderApi(api_client).account_active_orders(
        account_index=client.account_index, market_id=0, auth=auth
    )
    if len(active_orders.orders) == 0:
        print("No active orders")
        return

    print(f"{active_orders.orders=}")

    # cancel order
    tx, tx_hash, err = await client.cancel_order(
        market_index=0,
        order_index=123,
    )
    print(f"Cancel Order {tx=} {tx_hash=} {err=}")
    if err is not None:
        raise Exception(err)

    await client.close()
    await api_client.close()


if __name__ == "__main__":
    asyncio.run(main())

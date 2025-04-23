from asyncio import sleep
from random import randbytes, randint

from reduct import Client

BLOB = randbytes(100 * 1024)  # 100 KB of random bytes

async def send_data():
    async with Client("http://127.0.0.1:8383") as client:
        # Get bucket
        bucket = await client.get_bucket("data")

        while True:
            # Generate score
            score = randint(1, 100) / 100.0

            # Write record
            await bucket.write(
                "scored_data",
                BLOB,
                labels={
                    "score": score,
                },
            )

            print(f"Record with score {score} written")
            await sleep(1)


if __name__ == "__main__":
    import asyncio
    loop = asyncio.new_event_loop()
    loop.run_until_complete(send_data())
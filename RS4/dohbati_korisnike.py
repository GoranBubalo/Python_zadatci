import aiohttp, asyncio

# Getting user information
async def fetch_users(session):
    response = await session.get("https://jsonplaceholder.typicode.com/users")
    fetch_user = await response.json()
    return fetch_user


async def main():
    # Starting a Client session
    async with aiohttp.ClientSession() as session:
        users_task = [asyncio.create_task(fetch_users(session)) for _ in range(5)]
        list_of_users = await asyncio.gather(*users_task)

        # Getting individual user list from collective list of all users
        all_users = []
        for users in list_of_users:
            for user in users:
                all_users.append(user)

        # Getting unique values from the main list
        names = list(map(lambda user: user["username"], all_users))
        unique_names = list(set(names))
        email = list(map(lambda user: user["email"], all_users))
        unique_email = list(set(email))
        username = list(map(lambda user: user["username"], all_users))
        unique_username = list(set(username))

    # Printing out unique lists
    print(unique_names)
    print(unique_email)
    print(unique_username)


asyncio.run(main())

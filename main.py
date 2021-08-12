import asyncio

import matplotlib.pyplot as plt
import yaml

from jobsdb import jobs_db_scrap

fig = plt.figure(figsize=(10, 5))


async def main():
    opens = []
    with open("keywords.yml", "r") as file:
        keywords = yaml.load(file, Loader=yaml.FullLoader)["keywords"]
        tasks = await asyncio.gather(
            *[jobs_db_scrap(keyword=keyword) for keyword in keywords]
        )

        for data in tasks:
            opens.append(data["data"]["jobs"]["total"])

    plt.bar(keywords, opens, color="maroon", width=0.4)
    plt.xlabel("Keyword")
    plt.ylabel("No. of opening jobs")
    plt.title("Number of opening jobs by keyword in jobsdb")
    plt.show()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

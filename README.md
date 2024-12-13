## Unofficial YLE bot for Bluesky

Despite growing user numbers, the social media platform Bluesky still lacks finnish language media outlets. To remedy this untill they join the platform, I thought it might be interesting to make a bot that does just that.

The idea is to first query the finnish public broadcasting company YLE's webpage for most recent news, save the title and link of a new article, and save them into a database. From there, they can be posted to Bluesky.

So far the bot only has the ability to fetch and parse the contents of the latest YLE news, but next I will be working on the database and bot logic itself.

You can set up and run the bot by if you have Python 3.13.1 installed, have cloned the repo and have navigated to the root directory. After that, finish setup with.

`pip install -r requirements.txt`

You can run all the tests with

`pytest tests/`

Or a single one with 
`pytest tests/test_fetchHTML.py`

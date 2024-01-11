import os
import discord
import praw
import asyncio
from keep_alive import keep_alive

keep_alive()

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

reddit = praw.Reddit(
    client_id='SIFUutap4841n7woBb-XZw',
    client_secret='-xOqLjMGwGSWYx9N9hg0lXc4qJ5jtQ',
    user_agent='SweetBun/0.0.1 by Alarming_Court3150',
    check_for_async=False)  # Fill in your Reddit app's credentials here

# Dictionary mapping subreddit names to channel IDs
subreddit_channels = {

    #Actresess
    'jerkofftoceleb': 1185638059706945608,
    'Celebhub': 1185638059706945608,
    'Celebswithbigtits': 1185638059706945608,

    #singers
    'SexyMusicians': 1185638059706945608,
    'ArianaGrande': 1185638059706945608,
    'dualipa': 1185638059706945608,
    'HaileeSteinfeld': 1185638059706945608,
    'MadisonBeerLewd': 1185638059706945608,

    #Models/Influencers
    'Models': 1185638059706945608,
    'SommerRay': 1185638059706945608,
    'Elite_Models': 1185638059706945608,
    'SISwimsuitGirls': 1185638059706945608,
    'KylieJennerPics': 1185638059706945608,
    #kpop
    'kpopfap': 1185644926516605068,
    'KpopHotties': 1185644926516605068,
    'Twice_Fap': 1185644926516605068,
    'BlackpinkFap': 1185644926516605068,
    'GIDLE_Hotties': 1185644926516605068,
    'ITZY_NSFW': 1185644926516605068,
    'KpopRoleplays': 1185644926516605068,
    'KpopBeautiful': 1185644926516605068,

    #asian
    'prettyasiangirls': 1185644926516605068,
    'KoreanHotties': 1185644926516605068,
    'asianfitgirls': 1185644926516605068,

    #pornstars
    'HardcoreNSFW': 1185643561358741544,
    'lesbians': 1185643561358741544,
    'PornGifs': 1185643561358741544,
    'PornStarHQ': 1185643561358741544,
    'PornStars': 1185643561358741544,

    #Cosplay
    'cosplaybabes': 1185643759531204629,
    'CosplayLewd': 1185643759531204629,
    'CosplayNsfw': 1185643759531204629,
    'CosplayNation': 1185643759531204629,
    'cosplaygirls': 1185643759531204629,

    #Hentai
    'hentai': 1185643689595392010,
    'HENTAI_GIF': 1185643689595392010,
    'jerkbudsHentai': 1185643689595392010,
    'HentaiAndRoleplayy': 1185643689595392010,
}

# Dictionary to store fetched post IDs for different subreddits
fetched_post_ids = {subreddit: set() for subreddit in subreddit_channels}


async def post_new_subreddit_media():
  await bot.wait_until_ready()

  while not bot.is_closed():
    for subreddit_name, channel_id in subreddit_channels.items():
      subreddit = reddit.subreddit(subreddit_name)
      new_posts = subreddit.new(limit=3)  # Adjust the limit as needed

      for submission in new_posts:
        if submission.id not in fetched_post_ids[subreddit_name]:
          # Check if the submission URL is media (image, gif, video)
          if submission.url.lower().endswith(
              ('.jpg', '.jpeg', '.png', '.gif', '.mp4')):
            channel = bot.get_channel(channel_id)
            if channel:
              await channel.send(submission.url)
            fetched_post_ids[subreddit_name].add(submission.id)

    await asyncio.sleep(30)  # Check for new posts every 60 seconds


@bot.event
async def on_ready():
  print(f'Logged in as {bot.user.name} - {bot.user.id}')
  bot.loop.create_task(post_new_subreddit_media())


# Replace 'YOUR_BOT_TOKEN' with your bot's actual token (as a string)
bot.run(os.environ['token'])

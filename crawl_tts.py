import time
import datetime
import pytz
import pandas as pd

from tweepy import API
from tweepy import OAuthHandler

import src.twitter_config as get_api




def save_trends():
    api = get_api.get_auth_api('./settings/twitter_config.txt')
    trends_list = api[1].trends_place(id=23424768)
    time_now = datetime.datetime.now(pytz.timezone('Brazil/East'))
    trends_df = pd.DataFrame(trends_list[0]['trends'])
    trends_df['time'] = time_now
    trends_df.to_csv(time_now.strftime("./data/trends/%Y%m%d_%H%M_trends.csv"))


# for test purposes
if __name__ == "__main__":
    save_trends()
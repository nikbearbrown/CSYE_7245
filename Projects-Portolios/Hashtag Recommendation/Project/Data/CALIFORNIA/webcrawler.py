import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'xE5rQKgl43y7hsYEHVK6xfPhD'
consumer_secret = 'UZ0YELUFQRLrI08kM2jS4EOCVzp4kN2H4XbmyZptxHSt7Gjbm1'
access_token = '971850294962393089-HiM8wvFzLZQ9hRlLCtMEbsQ3CJNoirS'
access_token_secret = 'KOAm02mlcwTIklMWBr4VNpjKVrsKrEP3QISS3uhiz0mfZ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data


trends = api.trends_place(2442047)
place = "California"

hash_trends = []
for	trend in trends[0]['trends']:
	if(trend['name'].startswith('#')):
		hash_trends.append(trend['name'])

#print(hash_trends)


#for tweet in search_hashtag:
#    print (tweet)



for trend in hash_trends:
	
	file_name = trend.replace("#", "")
	csvFile = open(file_name+'.csv', 'a')
	#Use csv Writer
	csvWriter = csv.writer(csvFile)
	
	for tweet in tweepy.Cursor(api.search,q=trend,count=100,
								   lang="en",
								   since="2018-01-01").items(1000):
		#    print (tweet.created_at, tweet.text)
			if trend.lower() not in tweet.text.lower():
				text = " "+ trend + " " + tweet.text.strip()
				csvWriter.writerow([tweet.created_at, text.encode('utf-8'), place])
			else:
				text = tweet.text
				csvWriter.writerow([tweet.created_at, text.encode('utf-8'), place])

print("\n")
print("Done")


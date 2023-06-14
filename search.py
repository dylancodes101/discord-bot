from googleapiclient.discovery import build

# API Key
API_KEY = 'AIzaSyCQXpsgYCTmdP_dl0FJE6tOjuyU6EHAacQ'  # Replace with your own API key

def get_youtube_subscriber_count(channel_name):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    response = youtube.search().list(
        part='id',
        q=channel_name,
        type='channel',
        maxResults=1
    ).execute()
    
    if 'items' in response:
        channel_id = response['items'][0]['id']['channelId']
        channel_response = youtube.channels().list(
            part='statistics',
            id=channel_id
        ).execute()
        subscriber_count = int(channel_response['items'][0]['statistics']['subscriberCount'])
        return subscriber_count
    else:
        return None

def main():
    # YouTube Channel Name
    CHANNEL_NAME = 'CHANNEL_NAME'  # Replace with the name of the YouTube channel

    # Get subscriber count
    subscriber_count = get_youtube_subscriber_count(CHANNEL_NAME)
    if subscriber_count is not None:
        print(f"The channel '{CHANNEL_NAME}' has {subscriber_count:,} subscribers.")
    else:
        print(f"No channel found with the name '{CHANNEL_NAME}'.")

if __name__ == "__main__":
    main()

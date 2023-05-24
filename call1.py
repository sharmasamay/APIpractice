from googleapiclient.discovery import build
key = 'AIzaSyCuzIj1MVMGC4hN2gM6stn5I7BKx0EvGPg'
youtube = build('youtube','v3',developerKey='AIzaSyCuzIj1MVMGC4hN2gM6stn5I7BKx0EvGPg')
request = youtube.channels().list(
    part='statistics',
    forUsername = 'NickWhite'
)
response = request.execute()
print(response)
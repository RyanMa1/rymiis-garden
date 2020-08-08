Make a heroku app and connect this repository to it (fork this repository first)

run rasp.py on your raspberry pi

use the following command for the camera on the raspberry pi:
raspivid -n -t 0 -w 1920 -h 1080 -fps 30 -b 3500000 -g 60 -o - | ffmpeg -f lavfi -i anullsrc -c:a aac -r 30 -i - -g 60 -strict experimental -threads 4 -vcodec copy -map 0:a -map 1:v -b:v 3500000 -preset ultrafast -f flv "rtmp://live-ams02.twitch.tv/app/YOUR_TWITCH_KEY"

to see the sensoe=r data, install heroku CLI, login and use this command:
heroku logs -a YOUR_APP_NAME -s app -t

# Chat Volume Control

This Python script allows you to dynamically control the volume of Ubuntu using `amixer`
based on commands received in the Twitch chat. It is designed to lower the system
volume temporarily in response to specific events in the chat.

> **Note**: This script was specifically made for me when watching Rubius' Twitch,
where he has points rewards, which produces a loud noise. The script lowers my volume
for five seconds when triggered.

## Features

- Adjusts system volume based on Twitch chat points rewards.
- Web service implemented with FastAPI for browser-triggered commands.

## Set up steps

1. **Clone the Repository**  
   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/jeyg20/chat_volume_control.git
   ```

2. **Create python enviromet and install the Dependencies**  

   ```bash
   cd chat_volume_control
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Create a `.env` File**  

   ```bash
   touch .env
   ```

   - **Paste the following and add Your Credentials**  

   ```env
   NICKNAME="<YOUR_USERNAME>"          # Your Twitch username
   TOKEN="<YOUR_OAUTH_TOKEN>"          # Your Twitch OAuth token
   CHANNEL="<CHANNEL_NAME_TO_TRACK_CHAT>"  # The Twitch channel you want to monitor
   ```

   You can obtain your Twitch authentication token by visiting
   [Twitch Authentication Token Generator](https://twitchapps.com/tmi/).

4. **Run the service**

   ```bash
   uvicorn web_service.service:app --host 0.0.0.0 --port 80
   ```

5. **Set the following script in GreaseMonkey**

   ```javascript
   (function() {

   'use strict';

   const currentURL = window.location.href;

   if (currentURL.includes("twitch.tv/<TARGET_CHANNEL>")) {

     fetch("http://localhost:80/in-stream", {
             method: 'GET',
             mode: 'no-cors'
         })
         .then(response => console.log('In-stream API triggered successfully'))
         .catch(error => console.error('Error triggering in-stream API:', error));

     window.addEventListener('beforeunload', function(e) {
         fetch("http://localhost:80/out-of-stream", {
                method: 'GET',
                mode: 'no-cors'
            })
            .then(response => console.log('Out-of-stream API triggered successfully'))
            .catch(error => console.error('Error triggering out-of-stream API:', error));
        });
      }
   })();

   ```

# Chat volume control
This Python script allows you to control the volume of Ubuntu using `amixer` based on commands received in the Twitch chat.

## Set up steps
1. **Clone the Repository**  
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/jeyg20/chat_volume_control.git
   ```

2. **Install Python Dependencies**  
   ```bash
   cd chat_volume_control
   pip install -r requirements.txt
   ```

3. **Create a `.env` File**  
   ```bash
   touch .env
   ```

4. **Add Your Credentials**  
   ```env
   NICKNAME="<YOUR_USERNAME>"          # Your Twitch username
   TOKEN="<YOUR_OAUTH_TOKEN>"          # Your Twitch OAuth token
   CHANNEL="<CHANNEL_NAME_TO_TRACK_CHAT>"  # The Twitch channel you want to monitor
   ```

   You can obtain your Twitch authentication token by visiting [Twitch Authentication Token Generator](https://twitchapps.com/tmi/).

5. **Run the Script**  
   ```bash
   python main.py
   ```
## Additional Information

- Ensure you have `amixer` installed on your system for volume control.


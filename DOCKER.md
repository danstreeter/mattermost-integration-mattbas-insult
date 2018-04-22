## How to
The following procedure shows how to install this project using Docker. It describe procedure to easily build your custom image and deploy.

To install this project using Docker, you will need Docker Engine install on your machine. Procedure to install Docker can be found [here](https://docs.docker.com/engine/installation/)

Here's how to start:

1. **Build your Docker image**
 1. Clone this GitHub repo with
    - `git clone https://github.com/danstreeter/mattermost-integration-mattbas-insult.git`
    - `cd mattermost-integration-mattbas-insult`
 2. Build and tag Docker image using the Dockerfile provided
    - `docker build -t mattermost-integration-mattbas-insult .`
    _or you can use any image name you wish, changing it below as required_

2. **Set up your Mattermost slash command**
 1. Log in to your Mattermost account. Click the three dot menu at the top of the left-hand side and go to **Integrations** > **Slash Commands**
 2. Under *Add a new command*, enter `insult` into **Command Trigger Word**
 3. Paste your Web Server domain into *Callback URLs*, making sure to add `http://` to the beginning and `/insult` to the end so it looks similar to `http://<your-web-server-domain>:<MATTERMOST_INSULT_PORT>/insult` and click **Add**
 4. Select `POST` method
 5. (optional) Choose a username and icon url (more details [here](https://docs.mattermost.com/developer/slash-commands.html#set-up-a-custom-command))
 6. Copy the *Token* from your newly created slash command that appears under the *Existing commands* section

3. **Run the integration with Docker**  
  Back on your server, you only need to run your container, with some environnement variables
    - `MATTERMOST_INSULT_TOKEN=<your-token-here>` : this is the token you copied in the last section (you can specify multiple tokens which are separated by a colon)
    - `MATTERMOST_INSULT_HOST=<your-host>`  : the host you want the integration (defaults to 0.0.0.0)
    - `MATTERMOST_INSULT_PORT=<your-port-number>` : the port number you want the integration to listen on (defaults to 5000)
  Your container can be run with the following command :
  ```
  docker run -d \
  --name mattermost-insult \
  -p 5000:5000 \
  -e MATTERMOST_INSULT_TOKEN=<your-token-here> \
  -e MATTERMOST_INSULT_HOST=0.0.0.0 \
  -e MATTERMOST_INSULT_PORT=5000 \
  mattermost-integration-mattbas-insult
  ```

That's it! You should be able to type `/insult` or `/insult @username` into any channel and see an insult be returned.

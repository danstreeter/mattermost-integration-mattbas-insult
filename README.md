# Insult Integration Service for Mattermost
This integratin serivce can utilise Mattia Basaglia's amazing LibInsult API to fire an insult at one of your chat friends a Mattermost channel using Mattermost [slash commands](https://docs.mattermost.com/developer/slash-commands.html). 

Once implemented, users can type `/insult @username` to request an insult from [insult.mattbas.org](https://insult.mattbas.org/api/), return it and mention that user. (It can also be called without the `@username` to just get an insult.)

## Requirements
To run this integration you need:

1. A **web server** supporting Python 2.7 or compatible versions.
2. A **[Mattermost account](http://www.mattermost.org/)** [where slash commands are enabled]([slash commands](https://docs.mattermost.com/developer/slash-commands.html)

Many web server options will work, below we provide instructions for [**Docker**](DOCKER.md).
There is an image hosted on the [Docker Hub](https://hub.docker.com/r/danstreeter/mattermost-integration-mattbas-insult/) that can be used, however if you prefer to use the repository and build your own container you may.

### Docker Installation
The following procedure shows how to install this project using Docker. It describe procedure to use the public image which is kept up to date with this repository's `master` branch and also easily build your custom image to use.

To install this project using Docker, you will need Docker Engine install on your machine. Procedure to install Docker can be found [here](https://docs.docker.com/engine/installation/)

Here's how to start:

_If wanting to build the image yourself follow this step, if you are using the public image, skip to step 2_
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
 
  Your container can be run with the following command, changing `<image-preference>` as required:
  `mattermost-integration-mattbas-insult` - for your own built image as above
  `danstreeter/mattermost-integration-mattbas-insult` - for the public hosted image on the Docker Hub.
  ```
  docker run -d \
  --name mattermost-insult \
  -p 5000:5000 \
  -e MATTERMOST_INSULT_TOKEN=<your-token-here> \
  -e MATTERMOST_INSULT_HOST=0.0.0.0 \
  -e MATTERMOST_INSULT_PORT=5000 \
  <image-preference>
  ```

## Usage
Once installed, you will be able to type `/insult` or `/insult @username` into any channel and see an insult be returned either by itself, or with a mention for the `@username` given.

# Credits
This project was inspired by the amazing mattermost-giphy integration by numberly: [Repo](https://github.com/numberly/mattermost-integration-giphy) using the also awesome Insult api by mbasaglia: [Repo](https://github.com/mbasaglia/LibInsult) & [API](https://insult.mattbas.org/)
I dont take any credit for the work on this project and have meerly just modified the Giphy projct to work with the public LibInsult API.

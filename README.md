# Insult Integration Service for Mattermost
This integratin serivce can utilise Mattia Basaglia's amazing LibInsult API to fire an insult at one of your chat friends a Mattermost channel using Mattermost [slash commands](https://docs.mattermost.com/developer/slash-commands.html). 

Once implemented, users can type `/insult @username` to request an insult from [insult.mattbas.org](https://insult.mattbas.org/api/), return it and mention that user. (It can also be called without the `@username` to just get an insult.)

## Requirements
To run this integration you need:

1. A **web server** supporting Python 2.7 or compatible versions.
2. A **[Mattermost account](http://www.mattermost.org/)** [where slash commands are enabled]([slash commands](https://docs.mattermost.com/developer/slash-commands.html))

Many web server options will work, below we provide instructions for [**Docker**](DOCKER.md).

### Docker install
[**Here**](DOCKER.md)

# Credits
This project was inspired by the amazing mattermost-giphy integration by numberly: [Repo](https://github.com/numberly/mattermost-integration-giphy) using the also awesome Insult api by mbasaglia: [Repo](https://github.com/mbasaglia/LibInsult) & [API](https://insult.mattbas.org/)
I dont take any credit for the work on this project and have meerly just modified the Giphy projct to work with the public LibInsult API.

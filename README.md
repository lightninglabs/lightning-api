# Lightning Network Daemon API Documentation Site
API Documentation for the Lightning Network Daemon, powered by
[Slate](https://github.com/lord/slate)

## Overview

This repository contains functionality for programmatically pulling API
information from `lncli -h` and `rpc.proto` on the lnd Github, using a Python
script and Jinja2 template to output Slate markdown, which itself generates the
fully rendered static site. 

Pay special attention to the files inside the `templates` directory. They contain
the Jinja2 templates fed into the Python script, holding the basic format and
introductory information for the site.

## Running the site locally

**Important**: You need to run all commands from the root directory!

### Prerequisites

You're going to need:
 - **Docker CE** installed

### Building the docker image

This step is only necessary if a file inside the `docker/` folder was changed.
To just run everything, you can skip this step as the scripts will just use the
image `guggero/lightning-api` from Docker Hub.

```shell script
./docker/9-rebuild-image.sh
```

### Regenerating the markdown from the proto files

This step will check out the latest sources, copy the `*.proto` files and then
regenerate the documentation markdown.

```shell script
./docker/1-render-markdown.sh
```

You should now see updated `*.html.md` files in the `sources` folder.

### Running locally

To verify everything was updated/generated correctly, a local server can be spun
up with the following command:

```shell script
./docker/2-serve-locally.sh
```

You can now see the docs at `http://localhost:4567`.

### Deployment

The Lightning API is deployed with Google Cloud Platform. Visit [this blog
post](https://little418.com/2015/07/jekyll-google-cloud-storage.html) for more
information.

#### Steps

1. Install Google Cloud SDK and authenticate into it (this must only be done once per machine):

**macOS**:
```shell script
brew cask install google-cloud-sdk
gcloud auth login
```

**Debian/Ubuntu**:

```shell script
# Add the Cloud SDK distribution URI as a package source
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

# Import the Google Cloud Platform public key
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -

# Update the package list and install the Cloud SDK
sudo apt-get update && sudo apt-get install google-cloud-sdk
```

2. Run the build and deploy script:
```shell script
./docker/3-build-html.sh
./docker/4-deploy-gcloud.sh
```

### Running the server locally

The server uses Flask in order to receive POST requests from GitHub whenever a
new commit has been pushed to the respository. These POST requests will include
the HMAC of a secret token set up within the Webhook settings of a repository.
This token will need to be exported so that the server can verify the request
from GitHub has been authenticated.

The server can be run with:

```shell script
export WEBHOOK_SECRET_TOKEN=YOUR_TOKEN_HERE
./docker/5-run-webhook-server.sh
```

Once a POST request from GitHub has been received, the server will check if
there were any commits which included a change to the protobuf definitions. If
there was, then the documentation will be automatically regenerated and
deployed.

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

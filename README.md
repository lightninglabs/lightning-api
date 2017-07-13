# Lightning Network Daemon API Documentation Site
API Documentation for the Lightning Network Daemon

## Running the site locally

### Prerequisites

You're going to need:

 - **Linux or OS X** — Windows may work, but is unsupported.
 - **Ruby, version 2.2.5 or newer**
 - **Bundler** — If Ruby is already installed, but the `bundle` command doesn't work, just run `gem install bundler` in a terminal.

### Getting Set Up

```shell
git clone https://github.com/MaxFangX/lightning-api

# either run this to run locally
bundle install
bundle exec middleman server
```

You can now see the docs at `http://localhost:4567`.

## Deployment

The Lightning API is deployed with `s3_website`. Visit their [github
repo](https://github.com/laurilehmijoki/s3_website) for more information.

### Steps

1. Install `s3_website`
```bash
gem install s3_website
```

2. Add the deployment credentials for `s3_config.yml`
```
export LN_S3_ID="YOUR_S3_ID"
export LN_S3_SECRET="YOUR_S3_SECRET"
export LN_CLOUDFRONT_DISTRIBUTION_ID="YOUR_CLOUDFRONT_DISTRIBUTION_ID"
```

3. Build the website:
```
bundle exec middleman build --clean
```

4. Deploy the site from local changes:

```
s3_website push
```

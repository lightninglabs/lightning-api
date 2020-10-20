FROM golang:1.13-buster

# Install all required packages. We need Ruby >= 2.3.1 and Python >= 2.7.0.
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
  && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg  add - \
  && apt-get -y update \
  && apt-get -y install \
    ruby-full \
    zlib1g-dev \
    python3 \
    python3-pip \
    git \
    build-essential \
    rsync \
    nodejs \
    google-cloud-sdk \
  && rm -rf /var/lib/apt/lists/*

RUN gem install bundler \
 && pip3 install Jinja2 flask

RUN mkdir /tmp/work && cd /tmp/work
WORKDIR /tmp/work

COPY config.rb Gemfile Gemfile.lock /tmp/work/
RUN bundle config set path 'vendor/bundle' \
  && bundle install

COPY install_proto.sh /tmp/work/
RUN /tmp/work/install_proto.sh

# Compile both projects to have most dependencies and build steps cached.
RUN git clone https://github.com/lightningnetwork/lnd /tmp/lnd \
  && cd /tmp/lnd \
  && make \
  && git clone https://github.com/lightninglabs/loop /tmp/loop \
  && cd /tmp/loop \
  && make \
  && git clone https://github.com/lightninglabs/faraday /tmp/faraday \
  && cd /tmp/faraday \
  && make \
  && git clone https://github.com/lightninglabs/pool /tmp/pool \
  && cd /tmp/pool \
  && make

# Copy the rest of the files last so changes won't trigger a full rebuild of the image.
COPY . /tmp/work

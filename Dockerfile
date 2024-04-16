from python:3.12-bullseye as builder

copy . /tmp/pkg
workdir /tmp/pkg
run pip3 install .
run rm -rf /tmp/pkg

from python:3.12-slim-bullseye as runner

run apt-get update \
  && apt-get install -y \
    iputils-ping \
    net-tools \
  && rm -rf /var/lib/apt/lists/*

copy --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
copy --from=builder /usr/local/bin/secpg /usr/local/bin/secpg

# agent-py

![Coverage](coverage.svg)


[![Contributors](https://img.shields.io/gitlab/url=https://devops.telecomste.fr/api/v4/projects/3747/repository/contributors/badge?private_token=glpat-hybcv5GQSsoxXabqizE6)](https://devops.telecomste.fr/printerfaceadmin/2023-24/group4/agent/-/project_members)





## Requirements

- Python 3.X
- virtualenv [intall](https://virtualenv.pypa.io/en/latest/installation.html)

## Run project

```sh
make environment
make help
make run
#or
make debug
```

## Configuration

Environment variable:

- AGENT_ENV: local/production
- AGENT_VERSION: app version, default 1.0.0, endpoint /version
- AGENT_DESCRIPTION: app description
- AGENT_DEBUG: activate debug mode (boolean)

local : enable reload mode (default)
prod : no hot reload

## Usage

Run project with `make debug` and consult url in log for api doc at `/docs` or `/redoc`.

Application is running 2 threads, one for the API to expose metrics and one for collecting metrics.

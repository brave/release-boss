# Github Brave Stats

## Setup

`pipenv install`

## Running tests

`pipenv run pytest`

## Commands

### Linting

`pipenv run lint`

### Find PR counts per release data

`GITHUB_ACCESS_TOKEN=<token-here> pipenv run main --action=pr-milestone`

### Plot PR counts per release data

`GITHUB_ACCESS_TOKEN=<token-here> pipenv run plot`

### Detect PRs that have a missing milestone

`GITHUB_ACCESS_TOKEN=<token-here> pipenv run main --action=pr-milestone`

### Detect issues that have a missing milestone

`GITHUB_ACCESS_TOKEN=<token-here> pipenv run main --action=issues-milestone`

### Getting help

`GITHUB_ACCESS_TOKEN=<token-here> pipenv run main --help`

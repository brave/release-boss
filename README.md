# Release Boss

[![Build Status](https://travis-ci.org/brave-experiments/release-boss.svg?branch=master)](https://travis-ci.org/brave-experiments/release-boss)

Feeling like you need another boss? We've got you covered. 
Release boss is your all in one automated boss. It will nag you for triage things you should have done but didn't do.

> It's just that we're putting new coversheets on all the TPS reports *before* they go out now. So if you could just remember to do that from now on, that'd be great ...

## Setup

`pipenv install`

## Running tests

`pipenv run pytest`

## Environment

```
SLACK_ACCESS_TOKEN=<token-here>
GITHUB_ACCESS_TOKEN=<token-here>
```

## Commands

### Linting

`pipenv run lint`

### Find PR counts per release data

`pipenv run main --action=pr-milestone`

### Checks for missing labels and notifies people of those issues on Slack

`pipenv run main --action=fix-missing-issue-labels`

### Detect PRs that have a missing milestone

`pipenv run main --action=pr-milestone`

### Detect issues that have a missing milestone

`pipenv run main --action=issues-milestone`

### Other not fully supported commands without tweaking code

- Plot PR counts per release data: `pipenv run plot`


### Getting help

`GITHUB_ACCESS_TOKEN=<token-here> pipenv run main --help`

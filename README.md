# Release Boss

![Build Status](https://github.com/brave/adblock-rust/actions/workflows/ci.yml/badge.svg)

Feeling like you need another boss? We've got you covered. 
Release boss is your all in one automated boss. It will nag you for triage things you should have done but didn't do.

> It's just that we're putting new coversheets on all the TPS reports *before* they go out now. So if you could just remember to do that from now on, that'd be great ...

## Setup

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then:

`uv sync`

## Running tests

`uv run pytest`

## Environment

```
SLACK_ACCESS_TOKEN=<token-here>
GITHUB_ACCESS_TOKEN=<token-here>
```

## Commands

### Linting

`uv run pycodestyle -r .`

### Find PR counts per release data

`uv run python main.py --action=pr-milestone`

### Checks for missing labels and notifies people of those issues on Slack

`uv run python main.py --action=fix-missing-issue-labels`

### Detect PRs that have a missing milestone

`uv run python main.py --action=pr-milestone`

### Detect issues that have a missing milestone

`uv run python main.py --action=issues-milestone`

### Other not fully supported commands without tweaking code

- Plot PR counts per release data: `uv run python plot.py`


### Getting help

`uv run python main.py --help`

# tap-hightouch

`tap-hightouch` is a Singer tap for [Hightouch.io](https://hightouch.io/docs/integrations/api/).

Built with the Meltano [SDK](https://gitlab.com/meltano/sdk) for Singer Taps.

## Installation

To install this tap, run:

```bash
pip install git+https://github.com/immuta/tap-hightouch.git
```

## Configuration

### Accepted Config Options

Config options include:

- api_key: Hightouch API key
- sync_id_list: A list of integer values for the syncs to export data from


A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-hightouch --about
```

## Usage

You can easily run `tap-hightouch` by itself or in a pipeline using [Meltano](www.meltano.com).

### Executing the Tap Directly

```bash
tap-hightouch --version
tap-hightouch --help
tap-hightouch --config CONFIG --discover > ./catalog.json
```

## Developer Resources

Below are instructions for working on this package.

### Initialize your Development Environment

First install the package using `poetry`. Refer to that package's installation instructions.

```bash
poetry install
```

### Create and Run Tests

Create tests within the `tap_hightouch/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-hightouch` CLI interface directly using `poetry run`:

```bash
poetry run tap-hightouch --help
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to 
develop your own taps and targets.

# Usage

Now that the project exists, make a virtual environment:
```bash
$ cd tap-conversor
$ python3 -m venv ~/.virtualenvs/tap-conversor
$ source ~/.virtualenvs/tap-conversor/bin/activate
```
Install the package:
```bash
$ pip install -e .
```

And invoke the tap in discovery mode to get the catalog:
```bash
$ tap-conversor -c sample_config.json --discover
```
Or, if you prefer to save this file in the catalogs directory, use the following command;
```bash
$ tap-conversor -c sample_config.json --discover > tap_conversor/catalogs/catalog.json
```
The output should be a catalog with the single sample stream (from the schemas folder):
```bash
{
  "streams": [
    {
      "stream_alias": "Last",
      "tap_stream_id": "Last",
      "key_properties": [],
      "schema": {
        "properties": {
          "code": {
            "type": [
              "string",
              "null"
            ]
          },
          "codein": {
            "type": [
              "string",
              "null"
            ]
          },
          "name": {
            "type": [
              "string",
              "null"
            ]
          },
          "high": {
            "type": [
              "string",
              "null"
            ]
          },
          "low": {
            "type": [
              "string",
              "null"
            ]
          },
          "varBid": {
            "type": [
              "string",
              "null"
            ]
          },
          "pctChange": {
            "type": [
              "string",
              "null"
            ]
          },
          "bid": {
            "type": [
              "string",
              "null"
            ]
          },
          "ask": {
            "type": [
              "string",
              "null"
            ]
          },
          "timestamp": {
            "type": [
              "string",
              "null"
            ]
          },
          "create_date": {
            "type": [
              "string",
              "null"
            ]
          }
        },
        "type": [
          "object",
          "null"
        ]
      },
      "stream": "last",
      "metadata": [
        {
          "metadata": {
            "selected": true,
            "table-key-properties": []
          },
          "breadcrumb": []
        }
      ]
    },
    {
      "stream_alias": "Daily",
      "tap_stream_id": "Daily",
      "key_properties": [],
      "schema": {
        "properties": {
          "varBid": {
            "type": [
              "string",
              "null"
            ]
          },
          "code": {
            "type": [
              "string",
              "null"
            ]
          },
          "codein": {
            "type": [
              "string",
              "null"
            ]
          },
          "name": {
            "type": [
              "string",
              "null"
            ]
          },
          "high": {
            "type": [
              "string",
              "null"
            ]
          },
          "low": {
            "type": [
              "string",
              "null"
            ]
          },
          "pctChange": {
            "type": [
              "string",
              "null"
            ]
          },
          "bid": {
            "type": [
              "string",
              "null"
            ]
          },
          "ask": {
            "type": [
              "string",
              "null"
            ]
          },
          "timestamp": {
            "type": [
              "string",
              "null"
            ]
          },
          "create_date": {
            "type": [
              "string",
              "null"
            ]
          }
        },
        "type": [
          "object",
          "null"
        ]
      },
      "stream": "daily",
      "metadata": [
        {
          "metadata": {
            "selected": true,
            "table-key-properties": []
          },
          "breadcrumb": []
        }
      ]
    }
  ]
}
```
If this catalog is saved to a `catalog.json` file, it can be passed back into the tap in sync mode:
```
tap-conversor -c sample_config.json --catalog tap_conversor/catalogs/catalog.json
```

Now you build the tap!

# Testing

Before testing the Tap we need to generate all catalogs that will be validated during the tests, 
make sure to create and commit all catalogs.
With everything created, run:
```
make test
```

# Docker

Tap is done? Nice!
To publish our tap we just need to run the following steps:

Docker Build:
```sh
make TAP_NAME=tap-conversor build_tap
```
Publishing a Docker Image:
```sh
make TAP_NAME=tap-conversor publish_tap
```
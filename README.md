# Configuration Files
Please copy the `config_defaults.toml` file to a `config.toml` file for storing your private configurations.

This can be done using:
`Copy-Item config_defaults.toml config.toml`

or

`cp config_defaults.toml config.toml`

```toml
[discord]
TOKEN="<your discord token here>"
PREFIX="<your command prefix here>"
```


# Operation
First you must install the ADAMA package to support module namespacing

`pip install -e .`

Then you can run the main.py entrypoint located in `src/adama/main.py`

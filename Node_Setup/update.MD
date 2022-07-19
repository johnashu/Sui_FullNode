# Shut down your currently running fullnode.

```bash
cd into your local Sui repository:
cd sui
```

Remove the old on-disk database and 'genesis.blob' file:
```bash
rm -r suidb genesis.blob
```

Fetch the source from the latest release:
```bash
git fetch upstream
```

Reset your branch:
```bash
git checkout -B devnet --track upstream/devnet
```

Download the latest genesis state for Devnet as described above.
Update your fullnode.yaml configuration file if needed.
Restart your Sui fullnode:

```bash
cargo run --release --bin sui-node -- --config-path fullnode.yaml
```


# Summary
```bash
cd sui
rm -r suidb genesis.blob
git fetch upstream
git checkout -B devnet --track upstream/devnet
curl -fLJO https://github.com/MystenLabs/sui-genesis/raw/main/devnet/genesis.blob
sudo service suiFullNode restart
```
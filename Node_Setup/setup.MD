# install rustup

```bash
sudo curl https://sh.rustup.rs -sSf | sh
```

To configure your current shell, run:

```bash
source "$HOME/.cargo/env"

```
REBOOT

# Prerequistes.
```bash

sudo apt install net-tools

sudo apt install curl

sudo rustup update stable

sudo apt install libssl-dev

sudo apt install cmake

sudo apt install libclang-dev

sudo apt-get update \
    && DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get install -y --no-install-recommends \
    tzdata \
    git \
    ca-certificates \
    curl \
    build-essential \
    libssl-dev \
    pkg-config \
    libclang-dev \
    cmake

```
# Git

```bash
git clone https://github.com/<GITHUB_USER>/sui.git
```

Set up your fork of the Sui repository:
Go to the Sui repository on GitHub and click the Fork button in the top right-hand corner of the screen.
Clone your personal fork of the Sui repository to your local machine (ensure that you insert your GitHub username into the URL):

```bash
git clone https://github.com/<GITHUB_USER>/sui.git
```

cd into your sui repository:

```bash
cd sui
```

Set up the Sui repository as a git remote:

```bash
git remote add upstream https://github.com/MystenLabs/sui
```

Sync your fork:

```bash
git fetch upstream
```

Check out the devnet branch:

```bash
git checkout --track upstream/devnet
```

# Get Chain states

- Make a copy of the fullnode configuration template:
```bash
cp crates/sui-config/data/fullnode-template.yaml fullnode.yaml
```

Configure public views and Open Ports
```bash
sed -i.bak "s/127.0.0.1/0.0.0.0/" fullnode.yaml
```

Download the latest genesis state for Devnet by clicking that link or by running the following in your terminal:
```bash
curl -fLJO https://github.com/MystenLabs/sui-genesis/raw/main/devnet/genesis.blob
```

# Optional: You can skip this set of steps if you are willing to accept the default paths to resources. If you need custom paths, edit your fullnode.yaml file to reflect the paths you employ:
Update the db-path field with the path to where the fullnode's database will be located. By default this will create the database in a directory ./suidb relative to your current directory:
```bash
db-path: "/path/to/suidb"
```
Update the genesis-file-location with the path to the genesis file. By default, the config looks for the file genesis.blob in your current directory:
genesis:
```bash
genesis-file-location: "/path/to/genesis.blob"
```
# Start your Sui fullnode:
```bash
cargo run --release --bin sui-node -- --config-path fullnode.yaml
```

Post build, receive the success confirmation message, SuiNode started!
Optional: Publish / subscribe to notifications using JSON-RPC via websocket.

Your fullnode will now be serving the read endpoints of the Sui JSON-RPC API at: `http://127.0.0.1:9000`
# Setup Systemd
```bash
sudo nano /etc/systemd/system/suiFullNode.service
```
OR 

```bash
cat<<-EOF > /etc/systemd/system/suiFullNode.service
[Unit]
Description=SuiFullNode daemon
After=network-online.target

[Service]
Type=simple
Restart=always
RestartSec=1
User=root
WorkingDirectory=/root/sui
ExecStart=/root/.cargo/bin/cargo run --release --bin sui-node -- --config-path fullnode.yaml
SyslogIdentifier=suiFullNode
StartLimitInterval=0
LimitNOFILE=65536
LimitNPROC=65536

[Install]
WantedBy=multi-user.target
EOF
```

```bash
sudo systemctl daemon-reload
sudo chmod 755 /etc/systemd/system/suiFullNode.service
sudo systemctl enable suiFullNode.service
sudo service suiFullNode start
sudo service suiFullNode status

sudo service suiFullNode stop
sudo service suiFullNode restart

```
# Check Logs
```bash
sudo apt-get install grc
sudo grc tail -f /var/log/syslog
```


# ufw

```bash
apt-get install ufw

ufw allow 9184

ufw allow 9000

ufw allow 8080

ufw allow 22

ufw enable

ufw status

ufw status verbose
```

```bash

cd /lib/systemd/system/
nano ufw.service
```
OR

```bash
cat<<-EOF > /lib/systemd/system/ufw.service
[Unit]
Description=Uncomplicated firewall
Documentation=man:ufw(8)
DefaultDependencies=no
After=network.target
Before=suiFullNode.service

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=ufw enable
ExecStop=ufw disable

[Install]
WantedBy=multi-user.target
EOF

```

# Update systemctl 

```bash
sudo systemctl daemon-reload

sudo chmod 755 /lib/systemd/system/ufw.service

sudo systemctl enable ufw.service

sudo service ufw start

sudo service ufw status

netstat -tulpn | grep LISTEN
```

You can check the status of your node here:
`https://node.sui.zvalid.com/`

# ufw

cd /mnt/sda3/lib/systemd/system/

cd /lib/systemd/system/
nano ufw.service

OR

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


apt-get install ufw
ufw allow 9184
ufw allow 9000
ufw allow 8080
ufw allow 2225
ufw enable
ufw status
ufw status verbose

sudo systemctl daemon-reload
sudo chmod 755 /lib/systemd/system/ufw.service
sudo systemctl enable ufw.service
sudo service ufw start
sudo service ufw status
netstat -tulpn | grep LISTEN


# Info
If you do ufw enable, systemctl disable ufw and then reboot the system, what is the ufw status verbose output after the reboot?

I'm guessing that it will be inactive.

If that's true, then the explanation is as follows:

ufw enable = enable firewall rules right now, and make a record that the desired state is to have the firewall enabled from now on. (If a firewall management daemon is needed, this will also start it automatically.)

ufw disable = disable firewall rules right now, and make a record that the desired state is to have the firewall disabled until commanded otherwise.

systemctl start ufw = restore the previously-recorded desired state of the firewall (if the desired state is to have the firewall disabled, there will be nothing to do). Also, start any firewall management daemon if needed, in such a way that the management process will be recognized by systemd as a background process that does not belong to any user session. If you want to have the firewall enabled persistently, you'll want this to happen automatically at boot time, and also have ufw enable set.

systemctl stop ufw = stop the firewall management daemon; may or may not also disable any existing firewall rules (use iptables -vnL or nft list tables to check the actual rules in effect within the kernel, independently from ufw).

systemctl enable ufw = at any subsequent reboots, run systemctl start ufw automatically as part of the boot process.

systemctl disable ufw = at any subsequent reboots, don't do anything to restore the firewall state and don't automatically start the firewall management daemon: go with the kernel default of no firewall rules at all.

For example, if you need to set up new firewall rules remotely and must ensure you won't lock yourself out, you might set systemctl disable ufw, set up an automatic reboot in 15 minutes or so, then add your rules and use ufw enable. If you can still connect to the system, the rules are correct as far as the remote access is concerned; you can set systemctl enable ufw (so the rules will be effective also after a reboot) and remove the timed reboot job.

But if you made a mistake that disables your access, just wait for the reboot job to trigger, and the system will come up with no firewall rules (because of systemctl disable ufw) and you will be able to log back in to fix the rule configuration.
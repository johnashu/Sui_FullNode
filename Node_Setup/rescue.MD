# Rescue Contabo

# Mount disk

```bash

sudo fdisk -l
sudo mkdir /mnt/sda3
sudo mount /dev/sda3 /mnt/sda3

cd /mnt/sda3/etc/systemd/system/multi-user.target.wants/
sudo rm ufw.service

sudo reboot

```

```bash
adduser maffaz

usermod -aG sudo maffaz

su - maffaz 

sudo adduser admin

sudo usermod -aG ssh admin

sudo mkdir -p "/home/admin/.ssh"
sudo chmod 0700 "/home/admin/.ssh"
sudo chown "admin:admin" "/home/admin/.ssh"

```

Add the SSH public key to your admin. This next command will open up a blank text editor. Here you will copy/paste the key starting with “ssh-rsa….”

```bash
sudo nano "/home/admin/.ssh/authorized_keys"
```

> Paste Public Key
```bash
ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAilecANtfLlX2bjpSaUYh4DEh/Rv1a3rwPUNtZAWA1eMLbOS+2pcOh8NG/5GyTXYFbQSX4eVhjyHv3pNxl2GyTB87c2YTW8ylhKDPbvK1fGqqb8hlX8KdCfY+PEanzGJiYCFYSy3gDr/wwm6M/80CR9qCG/VGFTDTIB1ktfoo3KOmBXAno6bTtHHXHSV7BwoFSpS1qHGdvmJgLZYeGlvs3WkCCrcnvm16rxHfnL8DHFx11xTWsV1CyiL5JBwn/mC7055aOJkDIwZFze7BCZsNibOsUk93VAw0CvMhmCWwhN1VU4fwedCPKirU6T047qDf2hP8bEkVIPy15BEH31+URw== rsa-key-20220913
```

# Set permissions
```bash
sudo ls "/home/admin/.ssh" -l
sudo chown "admin:admin" "/home/admin/.ssh/authorized_keys"
sudo chmod 0600 "/home/admin/.ssh/authorized_keys"
```

# Edit the SSH settings.

```bash
sudo nano /etc/pam.d/sshd
```


# Comment the following line out by adding a # in front of it.
```bash
#@include common-auth
```
# Next is to edit the sshd_config file.
```bash
sudo nano /etc/ssh/sshd_config
```
# Set UsePAM to yes.
```bash
UsePAM yes
```

# Disable the password authentication by removing # in front of it.
```bash
PasswordAuthentication no
```
# Add a new line at the end of the file that sets the Authentication Methods to require first the public key to be valid.
```bash
AuthenticationMethods publickey
```
# OPTIONAL BUT RECOMMENDED: Disable root authentication this will add extra layer of security to your VPS. Find the line and remove the # in front of it and set the value to no.
```bash
PermitRootLogin no
```
# OPTIONAL BUT RECOMMEND: Change your SSH port from 22 to another one, for example 2225. Check this list to help you pick a port to use. WARNING: If you do change your port to something other than 22 remember to change your ufw settings.
```bash
Port 2225
```
Then

```bash
sudo ufw allow 2225
sudo ufw deny 22
```

# Finally restart the sshd service to update the settings.
```bash
sudo service sshd restart
```

# **DONT CLOSE YOUR SESSION YET. Test it first by opening a new session.**

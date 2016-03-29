SSH

https://help.ubuntu.com/14.04/serverguide/openssh-server.html

OpenSSH provides tools for control and transfer of data between remote, networked computers.

OpenSSH is a version of Secure Shell (SSH) protocols. The server component sshd listens for client connections. 

## Install

    sudo apt-get install openssh-client
    sudo apt-get install openssh-server

## Configure

Confiration file lives in /etc/ssh/sshd_config

    man sshd_config

To restart after making changes.

    sudo services ssh restart

## SSH Keys

SSH keys allow authentication between two hosts without the need of a password. SH key authentication uses two keys, a private key and a public key. To generate the keys. To generate the key:

    ssh-keygen -t rsa

This will generate the keys using the RSA algorithm. During the process you will be prompted for a password. 

Hit enter when prompted.

The public key is saved in file ~/.ssh/id_rsa.pub. This can now be copied to the remote host.

Append it to authorised keys by entering:

    ssh-copy-id username@remotehost

Check the permissions on the authorised_keys file. Only the authorised user shoudl have read and write permissions.

    chmod 600 .ssh/authorised_keys

## Bluehost

To set up SSH with bluehost, the guidance reads.

    ssh hoovervi@hooverville.biz

This means I can log in after entering a password. Still not figured out how to upload a key???


## SHH to Host


## 

### 라즈베리파이 SAMBA접속

`sudo apt-get install samba samba-common-bin` 

`sudo nano /etc/samba/smb.conf`

```
[global]
wins support = yes
security = user
[raspberrypi]
comment = pi Folder
path=/pi
browseable=Yes
valid users = @users
force group = users
writable=Yes
only guest=no
guest ok = no
create mask=0777
directory mask=0777
public=no
```

`sudo smbpasswd -a pi`

`sudo /etc/init.d/samba restart`

​	

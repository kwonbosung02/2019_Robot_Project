### 라즈베리파이 고정IP

`/etc/dhcpcd.conf` 파일 수정해서 고정 IP 할당



gateway 주소 확인

`netstat -nr` : gateway 주소 확인 가능



dhcpcd.conf 파일 수정

```
# Example static IP configuration
#interface eth0
#static ip_address=192.168.0.10/24
#static ip6 address=fd51:42f8:caae:d92e::ff/64
#static routers=192.168.0.1
#static domain_name_servers=192.168.0.1 8.8.8.8 fd51:42f8:caae:d92e::1
```

```
# Example static IP configuration
#interface eth0
static ip_address=192.168.0.10/24
#static ip6 address=fd51:42f8:caae:d92e::ff/64
static routers=192.168.0.1
static domain_name_servers=192.168.0.1 8.8.8.8 fd51:42f8:caae:d92e::1
```

*static ip_address* -> 바꾸고 싶은 ip 주소 입력

*static router* -> 라우터 주소 입력

*static domain_name_servers* -> 바꾸고 싶은 ip 주소 입력



`sudo reboot`






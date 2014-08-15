# Các tập lệnh hay dùng
### Đổi tên máy chủ
- Trong CENTOS
```sh
echo "HOSTNAME=cen65-srv01" >> /etc/sysconfig/network
hostname "cen65-srv01"
```
- Trong Ubuntu
```sh
echo "u12-monitor.testcong.vn" > /etc/hostname
hostname -F /etc/hostname
```

### Cài đặt lệnh setuptools
- Cài đặt lệnh setup cho Centos 6.5 minimal
```sh
yum -y update && yum -y install setup && \
yum -y install setuptool && \
yum -y install setuptool system-config-network-tui system-config-firewall
```

### Đặt lại thời gian cho CENTOS
```sh
rm -rf /etc/localtime
ln -s  /usr/share/zoneinfo/Asia/ /etc/localtime
```

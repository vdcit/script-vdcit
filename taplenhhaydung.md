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

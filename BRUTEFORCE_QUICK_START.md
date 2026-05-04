# Brute-Force Attack Testing - Quick Reference

## 🚀 Start Testing NOW

### Command để chạy test SSH Brute-Force

```bash
# Test 1: SSH Brute-Force (độ trễ 1 giây)
python3 bruteforce_ssh_attack.py \
  --host 192.168.1.100 \
  --port 22 \
  --user admin \
  --wordlist passwords.txt \
  --delay 1

# Test 2: SSH Brute-Force (nhanh - 10 attempts/sec)
python3 bruteforce_ssh_attack.py \
  --host 192.168.1.100 \
  --port 22 \
  --user admin \
  --rapid \
  --attempts 10
```

### Command để chạy test RDP Brute-Force

```bash
# Test 3: RDP Brute-Force (độ trễ 0.5 giây)
python3 bruteforce_rdp_attack.py \
  --host 192.168.1.100 \
  --port 3389 \
  --user admin \
  --wordlist passwords.txt \
  --delay 0.5

# Test 4: RDP Brute-Force (nhanh - 50 attempts)
python3 bruteforce_rdp_attack.py \
  --host 192.168.1.100 \
  --port 3389 \
  --user admin \
  --rapid \
  --attempts 50
```

### Command để chạy Port Scanning

```bash
# Test 5: Port Scan (các port phổ biến)
python3 port_scanner.py \
  --host 192.168.1.100 \
  --common

# Test 6: Port Scan (các port 1-100)
python3 port_scanner.py \
  --host 192.168.1.100 \
  --range 1 100

# Test 7: Port Scan (nhanh - 1-1000)
python3 port_scanner.py \
  --host 192.168.1.100 \
  --ports 1-1000 \
  --rapid
```

### Chạy tất cả test với menu

```bash
# Interactive mode
python3 run_all_tests.py --host 192.168.1.100 --interactive

# Chạy tất cả test tự động
python3 run_all_tests.py --host 192.168.1.100 --all --monitor
```

---

## 📊 Các dòng báo động Snort kỳ vọng

### SSH Brute-Force Alert

```
[**] [1:3000002:1] SSH BRUTE-FORCE Possible Brute Force Attack Detected [**]
192.168.1.100:54321 -> 192.168.1.1:22
Message: SSH BRUTE-FORCE Possible Brute Force Attack Detected
```

### RDP Brute-Force Alert

```
[**] [1:3000006:1] RDP BRUTE-FORCE Multiple Connections Detected [**]
192.168.1.100:60000 -> 192.168.1.1:3389
Message: RDP BRUTE-FORCE Multiple Connections Detected
```

### Port Scan Alert

```
[**] [1:3000012:1] RECONNAISSANCE Port Scanning Activity Detected [**]
192.168.1.100:various -> 192.168.1.1:[various ports]
Message: RECONNAISSANCE Port Scanning Activity Detected
```

---

## 📁 File được tạo

| File | Mô tả |
|------|-------|
| `bruteforce_ssh_attack.py` | Script tấn công SSH |
| `bruteforce_rdp_attack.py` | Script tấn công RDP |
| `port_scanner.py` | Script quét port |
| `run_all_tests.py` | Chương trình chạy tất cả test |
| `passwords.txt` | Danh sách mật khẩu |
| `snort_custom_rules.conf` | Snort rules để phát hiện |
| `ATTACK_TESTING_GUIDE.md` | Hướng dẫn chi tiết |

---

## ✅ Checklist trước khi test

- [ ] Cài đặt Paramiko: `pip3 install paramiko`
- [ ] Snort đang chạy
- [ ] Npcap đang capture packet
- [ ] Firewall config đúng
- [ ] SSH/RDP service đang chạy trên target
- [ ] Network connectivity OK: `ping <target-ip>`

---

## 🎯 Các bước thực hiện

### Bước 1: Chuẩn bị môi trường

```bash
# Cài đặt dependencies
pip3 install paramiko

# Kiểm tra Snort
ps aux | grep snort

# Kiểm tra network
ping 192.168.1.100
```

### Bước 2: Khởi động Snort

```bash
# Terminal 1: Chạy Snort
sudo snort -A full -l /var/log/snort -c snort_custom_rules.conf -i eth0
```

### Bước 3: Chạy Attack Test

```bash
# Terminal 2: Chạy test
python3 bruteforce_ssh_attack.py --host 192.168.1.100 --user admin --wordlist passwords.txt
```

### Bước 4: Xem kết quả

```bash
# Terminal 3: Theo dõi alert
tail -f /var/log/snort/alert
```

---

## 📋 Cấu hình tùy chỉnh

### SSH với port khác

```bash
python3 bruteforce_ssh_attack.py \
  --host 192.168.1.100 \
  --port 2222 \
  --user root \
  --wordlist passwords.txt
```

### RDP với độ trễ tùy chỉnh

```bash
python3 bruteforce_rdp_attack.py \
  --host 192.168.1.100 \
  --port 3389 \
  --delay 2
```

### Port scan các port cụ thể

```bash
python3 port_scanner.py \
  --host 192.168.1.100 \
  --ports 22,80,443,3389
```

---

## 🔍 Dữ liệu cần thu thập

Để phân tích kết quả, ghi lại:

| Thông tin | Giá trị |
|-----------|--------|
| Ngày/Giờ test | YYYY-MM-DD HH:MM:SS |
| Loại tấn công | SSH/RDP/Port Scan |
| Target | IP:PORT |
| Thời gian tấn công | X seconds |
| Tổng số attempt | N |
| Số lần phát hiện | M |
| Thời gian phát hiện | X seconds |
| CPU usage | X% |
| Memory usage | Y% |

---

## ⚠️ Lưu ý bảo mật

✓ Chỉ test trên hệ thống của bạn hoặc có permission  
✓ Không test trên production systems  
✓ Cô lập lab environment khỏi internet  
✓ Ghi lại toàn bộ quá trình test  
✓ Không chia sẻ real IP addresses  

---

**Sẵn sàng test! Ready to go!** ✅

#/bin/bash
echo "[+] Install requirements"
apt-get update
apt-get install git -y
apt-get install python3 -y
apt-get install fping -y
pip3 install pychromecast
echo "[*] Done"

echo "[+] Getting files"
git clone
echo "[*] Done"

echo "[+] Installing"
mkdir /opt/notifier
mkdir /etc/notifier
cd /tmp
cp /tmp/notifier/notifier.py /opt/notifier/notifier.py
cp /tmp/notifier/config.txt /etc/notifier/config.txt
cp /tmp/notifier/data.txt /etc/notifier/data.txt

cp /tmp/notifier/notifier.service /etc/systemd/system/notifier.service
systemctl enable notifier
systemctl start notifier
echo "[*] Done"

echo "[+] Clean up"
rm -r /tmp/notifier
echo "[*] Done"

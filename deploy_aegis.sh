#!/bin/bash
# deploy_aegis.sh

echo "🚀 بدء نشر نظام AEGIS المتكامل"

# 1. تثبيت المتطلبات الأساسية
sudo apt-get update
sudo apt-get install -y \
    python3.10 \
    python3-pip \
    docker.io \
    docker-compose \
    git \
    nmap \
    tcpdump

# 2. إنشاء البيئة الافتراضية
python3 -m venv /opt/aegis/venv
source /opt/aegis/venv/bin/activate

# 3. تثبيت حزم Python
pip install --upgrade pip
pip install -r requirements.txt

# 4. تنزيل كود النظام
# Note: Assuming we are running this script from the repo or downloading it. 
# If running from repo, we might skip cloning or clone to specific location.
# The user script clones into /opt/aegis/core
if [ ! -d "/opt/aegis/core" ]; then
    git clone https://github.com/aegis-system/core.git /opt/aegis/core
fi
cd /opt/aegis/core

# 5. تكوين قاعدة البيانات
python3 setup_database.py

# 6. بدء الخدمات الأساسية
docker-compose up -d

# 7. بدء خدمة AEGIS
sudo cp aegis.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable aegis
sudo systemctl start aegis

# 8. تكوين الجدار الناري
sudo ufw allow 8000/tcp  # واجهة API
sudo ufw allow 9000/tcp  # واجهة الويب
sudo ufw allow 22/tcp    # SSH
sudo ufw enable

echo "✅ تم نشر نظام AEGIS بنجاح!"
echo "🌐 واجهة الويب: http://$(hostname -I | awk '{print $1}'):9000"
echo "🔌 واجهة API: http://$(hostname -I | awk '{print $1}'):8000/docs"

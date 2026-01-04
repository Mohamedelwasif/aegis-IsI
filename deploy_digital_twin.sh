#!/bin/bash
# deploy_digital_twin.sh

echo "🚀 بدء نشر Cyber Digital Twin..."

# 1. تثبيت المتطلبات
pip install -r src/backend/requirements.txt

# 2. تكوين Elasticsearch للتحليل الجنائي
# Note: Ensure Docker is running
if command -v docker &> /dev/null; then
    sudo docker run -d \
      --name elasticsearch \
      -p 9200:9200 \
      -p 9300:9300 \
      -e "discovery.type=single-node" \
      docker.elastic.co/elasticsearch/elasticsearch:8.10.0

    # 3. تكوين Redis للتخزين المؤقت
    sudo docker run -d \
      --name redis \
      -p 6379:6379 \
      redis:alpine
else
    echo "⚠️ Docker not found. Skipping container deployment."
fi

# 4. بدء خدمات الشبكة
# sudo systemctl start network-monitoring.service
echo "ℹ️ Network monitoring service start skipped (systemd not available)."

# 5. تشغيل النظام (Backend)
# Assumes running from root
cd src/backend
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!

# 6. تشغيل واجهة الويب (Frontend)
# Assumes compiled build or dev server
# python -m http.server 8050 & 
# Using npm run dev for development
cd ../../aegis-frontend
npm run dev &

echo "✅ Cyber Digital Twin جاهز!"
echo "🌐 الوصول عبر: http://localhost:5173 (Frontend) or http://localhost:8050 (Static)"
echo "📊 Dashboard: http://localhost:8000/dash/"

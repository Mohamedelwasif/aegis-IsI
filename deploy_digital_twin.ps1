# PowerShell Deployment Script for Cyber Digital Twin
Write-Host "🚀 بدء نشر Cyber Digital Twin..." -ForegroundColor Cyan

# 1. تثبيت المتطلبات
Write-Host "📦 Installing Python requirements..."
pip install -r src/backend/requirements.txt

# 2. تكوين Elasticsearch للتحليل الجنائي
if (Get-Command docker -ErrorAction SilentlyContinue) {
    Write-Host "🐳 Starting Elasticsearch..."
    docker run -d `
      --name elasticsearch `
      -p 9200:9200 `
      -p 9300:9300 `
      -e "discovery.type=single-node" `
      docker.elastic.co/elasticsearch/elasticsearch:8.10.0

    # 3. تكوين Redis للتخزين المؤقت
    Write-Host "🐳 Starting Redis..."
    docker run -d `
      --name redis `
      -p 6379:6379 `
      redis:alpine
} else {
    Write-Host "⚠️ Docker not found. Skipping container deployment." -ForegroundColor Yellow
}

# 4. بدء خدمات الشبكة (Simulation)
Write-Host "🔌 Starting Network Services (Simulated)..."

# 5. تشغيل النظام
Write-Host "🔥 Starting Backend (Uvicorn)..."
Start-Process -FilePath "python" -ArgumentList "-m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000" -WorkingDirectory "src/backend" -NoNewWindow

# 6. تشغيل واجهة الويب
Write-Host "🎨 Starting Frontend (Vite)..."
Set-Location "aegis-frontend"
Start-Process -FilePath "npm" -ArgumentList "run dev" -NoNewWindow

Write-Host "✅ Cyber Digital Twin جاهز!" -ForegroundColor Green
Write-Host "🌐 Frontend: http://localhost:5173"
Write-Host "📊 Dashboard: http://localhost:8000/dash/"

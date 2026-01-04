# AEGIS - Comprehensive Cyber Security System
# نظام إيجيس للأمن السيبراني الشامل

## نظرة عامة (Overview)
هذا هو الهيكل المعماري لنظام AEGIS القائم على الخدمات المصغرة (Microservices Architecture). يهدف النظام إلى توفير حلول أمنية شاملة للهيئات الحكومية والشركات والمنازل الذكية.

## الهيكلية (Architecture)

يتكون النظام من الخدمات التالية:

1.  **API Gateway (`/api-gateway`)**:
    - نقطة الدخول الرئيسية (Entry Point).
    - توجه الطلبات إلى الخدمات المناسبة.
    - تعمل على المنفذ `3000`.

2.  **Network Security Service (`/network-service`)**:
    - إدارة أجهزة Cisco، الجدران النارية (Firewalls)، وأنظمة كشف التسلل (IDS).
    - مبنية باستخدام Python (Flask).
    - تعمل على المنفذ `5000`.

3.  **Physical Security Service (`/physical-service`)**:
    - إدارة كاميرات المراقبة، وأنظمة التحكم في الدخول.
    - مبنية باستخدام Node.js.
    - تعمل على المنفذ `3001`.

4.  **IoT Security Service (`/iot-service`)**:
    - إدارة أجهزة المنازل الذكية وإنترنت الأشياء الصناعي.
    - مبنية باستخدام Node.js.
    - تعمل على المنفذ `3002`.

## طريقة التشغيل (How to Run)

### المتطلبات
- Docker & Docker Compose

### التشغيل باستخدام Docker
قم بتشغيل الأمر التالي في المجلد الرئيسي:
```bash
docker-compose up --build
```

### نقاط الوصول (Endpoints)
- **الحالة العامة للنظام**: `http://localhost:3000/`
- **أجهزة الشبكة (Cisco)**: `http://localhost:3000/api/network/cisco/devices`
- **سجلات الجدار الناري**: `http://localhost:3000/api/network/firewall/logs`
- **كاميرات المراقبة**: `http://localhost:3000/api/physical/cameras`
- **أجهزة المنزل الذكي**: `http://localhost:3000/api/iot/smart-home/devices`

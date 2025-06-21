# Docker Compose Practice

### ✅ 專案概述

架設三個container分別負責SQL、Python、Javascript的作業流程。最終將Titanic資料以表格方式呈現置網頁上。

### ✅ 專案目錄結構

```sh
project/
├── backend/
│   ├── app.py
│   ├── import_csv.py
│   ├── titanic_full_data.csv 
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── index.html
│   ├── script.js
│   ├── niginx.conf
│   └── Dockerfile
├── db/
│   └── init.sql
├── docker-compose.yml
└── README.md
```

### ✅ 專案部署方式

```sh
docker compose down -v
docker compose up --build
```

### ✅ 專案使用方式

在Browser上輸入
```sh
IP:8081
```

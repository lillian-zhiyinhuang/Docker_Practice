FROM nginx:alpine

# 複製靜態頁面
COPY index.html /usr/share/nginx/html/
COPY script.js /usr/share/nginx/html/

# 複製 Nginx 配置
COPY nginx.conf /etc/nginx/nginx.conf

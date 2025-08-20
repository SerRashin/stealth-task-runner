FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# System deps for Chrome
RUN apt-get update && apt-get install -y wget gnupg unzip curl     libnss3 libgconf-2-4 libxi6 libxcursor1 libxdamage1 libxcomposite1     libasound2 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 libxkbcommon0     libxrandr2 libgbm1 libgtk-3-0 libxshmfence1 fonts-liberation libappindicator3-1 xdg-utils  && rm -rf /var/lib/apt/lists/*

# Google Chrome stable
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor > /usr/share/keyrings/google.gpg &&     echo "deb [signed-by=/usr/share/keyrings/google.gpg arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list &&     apt-get update && apt-get install -y google-chrome-stable &&     rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV UC_DOWNLOAD_DIR=/tmp/uc_downloads
RUN mkdir -p /tmp/uc_downloads

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

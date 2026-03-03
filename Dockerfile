FROM python:3.12-slim

WORKDIR /jobstriker
COPY requirements.txt .
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*
RUN echo "pwd is: $(pwd)"
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN chmod +x ./start_local.sh
ENTRYPOINT ["sh", "./start_local.sh"]

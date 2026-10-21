FROM mcr.microsoft.com/playwright/python:1.63.0-noble
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PLAYWRIGHT_BROWSERS_PATH=/ms-playwright
COPY backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY backend/app ./app
COPY backend/tests ./tests
COPY frontend ./frontend
RUN useradd --create-home --uid 10001 --shell /usr/sbin/nologin firewatch \
    && mkdir -p /data/reports \
    && chown -R 10001:10001 /data \
    && chmod 0750 /data /data/reports
USER 10001:10001
ENV HOME=/home/firewatch
EXPOSE 8000
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]

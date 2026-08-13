FROM python:3.14-slim

RUN useradd -m -r appuser && \
   mkdir /app && \
   chown -R appuser /app

WORKDIR /app

COPY requirements.txt .
USER appuser
ENV PATH="/home/appuser/.local/bin:$PATH"

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=appuser:appuser . .

#RUN python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["gunicorn", "--bind=0.0.0.0:8000", "--workers=3", "gestor.wsgi:application"]
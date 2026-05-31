FROM python:3.13-alpine

WORKDIR /app

RUN python -m pip install --no-cache-dir --upgrade pip setuptools wheel \
 && addgroup -S app && adduser -S app -G app

COPY --chown=app:app Python/ /app/

USER app

ENV PYTHONUNBUFFERED=1

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD python -c "import sys; sys.exit(0)"

CMD ["python", "calculator.py"]

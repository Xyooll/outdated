FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
WORKDIR /app
COPY operation-dna /app/operation-dna
RUN mkdir -p /app/data

# The runtime is intentionally dependency-light. Add adapters as explicit packages.
CMD ["python", "-c", "print('Operation DNA runtime image ready')"]

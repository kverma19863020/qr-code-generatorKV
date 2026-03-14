# Base image
FROM python:3.12-slim-bullseye

# Set working directory
WORKDIR /app

# Copy dependency file
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create non-root user and folders
RUN useradd -m myuser && mkdir logs qr_codes && chown myuser:myuser logs qr_codes

# Copy project files
COPY --chown=myuser:myuser . .
# Switch user
USER myuser
# Run application
ENTRYPOINT ["python", "main.py"]
CMD ["--url", "http://github.com"]
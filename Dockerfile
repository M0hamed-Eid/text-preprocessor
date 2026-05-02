# Base image
FROM python:3.10-slim

# Prevent Python buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# We are removing the apt-get section to bypass the 403 Forbidden error
# If a library later complains about a missing 'gcc', we can revisit this.

# Copy requirements first for caching
COPY requirements.txt .

# Upgrade pip and install Python packages
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Download NLTK models (adding punkt_tab for your specific project)
RUN python -m nltk.downloader punkt punkt_tab stopwords wordnet omw-1.4

# Copy project files
COPY . .

# Make startup script executable
RUN chmod +x start.sh

# Expose app port
EXPOSE 8000

# Start app
CMD ["./start.sh"]
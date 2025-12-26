# Use lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirement.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Copy entire project
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Disable Streamlit telemetry
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Run Streamlit app
CMD ["streamlit", "run", "frontend/app.py", "--server.port=8501", "--server.address=0.0.0.0"]

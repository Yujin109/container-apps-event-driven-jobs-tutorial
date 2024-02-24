FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the rest of the application code
COPY . .

RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -U poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

# Expose the port the app runs on
EXPOSE 8080

# Start the application
CMD ["poetry", "run", "python", "main.py"]
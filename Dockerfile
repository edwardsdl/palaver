FROM python:3.6-stretch

# Install System Dependencies
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    tesseract-ocr

# Create User Account
RUN useradd  --create-home --system palaver
USER palaver

WORKDIR /srv/palaver

# Install Dependencies
COPY --chown=palaver requirements.txt requirements.txt
RUN pip install --user --no-warn-script-location --requirement requirements.txt

# Copy Application
COPY --chown=palaver app.py palaver ./

# Run Application
ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]

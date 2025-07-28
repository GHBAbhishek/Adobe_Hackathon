FROM --platform=linux/amd64 python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir PyPDF2
ENTRYPOINT ["python", "process_pdfs.py"]

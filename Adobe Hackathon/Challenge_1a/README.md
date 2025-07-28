# Adobe India Hackathon - Round 1A

This project extracts structured outlines (title, headings H1-H3) from PDFs and outputs them as JSON.

## 🧠 Approach
We use PyPDF2 to extract text from each page and apply heuristics to detect heading levels based on capitalization and assumed font size.

## 📁 Input/Output
- **Input:** PDF files in `/app/input`
- **Output:** JSON files in `/app/output`

## 📦 Docker Build & Run
```bash
docker build --platform=linux/amd64 -t mysolution:abc123 .
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none mysolution:abc123
```

## 📌 Constraints Met
- ✅ Model-free, fast execution (<10 sec)
- ✅ CPU-only, offline
- ✅ Docker compatible (amd64)

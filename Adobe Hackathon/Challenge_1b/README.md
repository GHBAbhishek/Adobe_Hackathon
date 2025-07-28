# Adobe India Hackathon - Round 1B

This system identifies and ranks relevant sections from multiple PDFs based on a persona's job.

## 👤 Persona Example
- PhD Researcher in Computational Biology
- Job: Literature review on "Graph Neural Networks for Drug Discovery"

## 🧠 Keywords Used
- "method", "dataset", "benchmark"

## 📁 Input/Output
- Input PDFs → `/app/input`
- Output JSON → `/app/output/challenge1b_output.json`

## 📦 Docker Usage
```bash
docker build --platform=linux/amd64 -t mysolution1b:abc456 .
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none mysolution1b:abc456
```

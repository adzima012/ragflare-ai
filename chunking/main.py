import os
import json
from utils import split_text

SOURCE_FILE = "../docs/contoh_dokumen.txt"
OUTPUT_FILE = "../outputs/chunks.jsonl"

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def save_chunks(chunks, output_path, source_name):
    with open(output_path, 'w', encoding='utf-8') as f:
        for i, chunk in enumerate(chunks):
            item = {
                "id": f"{source_name}-{i}",
                "text": chunk,
                "metadata": {
                    "source": source_name,
                    "chunk_index": i
                }
            }
            f.write(json.dumps(item) + "\n")

if __name__ == "__main__":
    # Step 1: Load text
    text = read_file(SOURCE_FILE)
    source_name = os.path.basename(SOURCE_FILE)

    # Step 2: Split into chunks
    chunks = split_text(text)

    # Step 3: Save to JSONL
    save_chunks(chunks, OUTPUT_FILE, source_name)

    print(f"✅ Saved {len(chunks)} chunks to {OUTPUT_FILE}")
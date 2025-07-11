from rag_services import generate_embedding
from db import insert_document

def chunk_text(text, chunk_size=200, overlap=20):
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        if chunk.strip():  # ensure non-empty chunks only
            chunks.append(chunk)
        start += chunk_size - overlap
    print(f"✅ Prepared {len(chunks)} non-empty chunks for ingestion.")
    return chunks

one = ['Check your offer letter. Paid/Unpaid: Unpaid, but offers valuable real-world AI project experience. Commitment: 10 hours/week minimum. Tech Stack: Any stack is acceptable; Python is commonly used. GitHub Submissions: Public repositories preferred for assessment. APIs: Allowed and encouraged. Project Examples: AI-powered home renovation, inventory forecasting, price prediction, productivity tools. Coding Requirements: Demonstrated skills required for selection. Post-Internship Opportunities: Certification, LinkedIn listing, and potential job referrals for top performers. OPT/CPT: Align start/end dates with the cohort timeline, consult your school, and follow E-Verify steps if applicable. Paid Services: API/cloud costs covered by PMA or PMs; hardware not covered. Kajabi Access: Interns do not receive Kajabi course access but receive separate recorded training and documents. Useful Links: Intern Recorded Training Intern Onboarding, AI Course, and Guide']


def main():
    with open("./files/Training.txt", "r") as f:
        content = f.read()
        print(repr(content[-200:]))  # show last 200 characters including \n

    chunks = chunk_text(content, chunk_size=200, overlap=20)
    print(chunks)
    print(len(chunks))
    for idx, chunk in enumerate(chunks):
        try:
            embedding = generate_embedding(chunk)
            insert_document({
                "document": chunk,
                "embedding": embedding,
                "chunk_index": idx,
                "source": "AI_Bootcamp_Journey"
            })
            print(f"✅ Chunk {idx+1}/{len(chunks)} ingested successfully.")
        except Exception as e:
            print(f"❌ Error ingesting chunk {idx+1}: {e}")

if __name__ == "__main__":
    main()



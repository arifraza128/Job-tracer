import sys
from pathlib import Path
import json
import httpx

# Add project root to python path to resolve crawler.* imports
project_root = Path(__file__).resolve().parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from crawler.utils.normalize import normalize
from crawler.utils.deduplicate import generate_hash
from crawler.utils.models import Job

def fetch_remoteok_jobs():
    print("Fetching jobs from RemoteOK...")
    response = httpx.get(
        "https://remoteok.com/api",
        headers={"User-Agent": "Mozilla/5.0"}
    )
    
    print(response.status_code)
    if response.status_code != 200:
        print("Failed to fetch jobs from RemoteOK.")
        return []
        
    raw_data = response.json()
    
    # RemoteOK API returns legal terms/metadata as the first element in the JSON array
    # Let's filter elements that represent a job listing (contains "position")
    jobs_list = []
    for item in raw_data:
        if isinstance(item, dict) and "position" in item:
            jobs_list.append(item)
            
    print(f"Jobs found: {len(jobs_list)}")
    return jobs_list

if __name__ == "__main__":
    # Test deduplication hash function as specified in Step 5
    test_hash = generate_hash("Python Dev", "Google", "Remote")
    print(f"Test generate_hash output: {test_hash}")
    
    # Fetch jobs
    jobs = fetch_remoteok_jobs()
    
    normalized_jobs = []
    job_objects = []
    
    if jobs:
        # Step 4 test on first job
        test_job = jobs[0]
        print("Original job sample:")
        print(test_job)
        print("Normalized job sample:")
        print(normalize(test_job))
        
        for job_data in jobs:
            # Step 4: Normalize
            norm = normalize(job_data)
            
            # Step 5: Deduplication Hash
            job_hash = generate_hash(
                norm.get("title") or "",
                norm.get("company") or "",
                norm.get("location") or ""
            )
            norm["hash"] = job_hash
            
            # Step 6: Create Job Schema Instance
            job_obj = Job(
                title=norm.get("title"),
                company=norm.get("company"),
                location=norm.get("location"),
                source=norm.get("source")
            )
            
            normalized_jobs.append(norm)
            job_objects.append(job_obj)
            
        # Step 7: Save Sample Jobs as JSON
        output_path = project_root / "jobs.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(normalized_jobs, f, indent=4)
        print(f"Saved jobs list to {output_path}")

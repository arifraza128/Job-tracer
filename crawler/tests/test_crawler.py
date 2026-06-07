import sys
from pathlib import Path

# Add project root to python path
project_root = Path(__file__).resolve().parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from crawler.utils.normalize import normalize
from crawler.utils.deduplicate import generate_hash
from crawler.utils.models import Job

def test_normalize():
    raw_job = {
        "position": "Python Developer",
        "company": "Google",
        "location": "Remote",
        "salary": "$120,000",
        "extra_info": "ignored"
    }
    normalized = normalize(raw_job)
    assert normalized["title"] == "Python Developer"
    assert normalized["company"] == "Google"
    assert normalized["location"] == "Remote"
    assert normalized["salary"] == "$120,000"
    assert normalized["source"] == "remoteok"
    print("test_normalize passed!")

def test_generate_hash():
    h1 = generate_hash("Python Dev", "Google", "Remote")
    h2 = generate_hash("python dev", "google", "remote")
    assert h1 == h2
    assert len(h1) == 32
    print("test_generate_hash passed!")

def test_job_model():
    job = Job("Python Dev", "Google", "Remote", "remoteok")
    assert job.title == "Python Dev"
    assert job.company == "Google"
    assert job.location == "Remote"
    assert job.source == "remoteok"
    print("test_job_model passed!")

if __name__ == "__main__":
    test_normalize()
    test_generate_hash()
    test_job_model()
    print("All tests passed successfully!")

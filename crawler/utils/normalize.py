def normalize(job):
    return {
        "title": job.get("position"),
        "company": job.get("company"),
        "location": job.get("location"),
        "salary": job.get("salary"),
        "source": "remoteok"
    }

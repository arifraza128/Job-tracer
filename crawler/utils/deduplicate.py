import hashlib

def generate_hash(title, company, location):
    t = (title or "").lower()
    c = (company or "").lower()
    l = (location or "").lower()
    text = t + c + l
    return hashlib.md5(text.encode("utf-8")).hexdigest()

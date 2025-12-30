print("APP STARTED")

# Resume and JD (already loaded from files)
with open("data/resume.txt", "r", encoding="utf-8") as f:
    resume = f.read().lower()

with open("data/job_description.txt", "r", encoding="utf-8") as f:
    jd = f.read().lower()

# Simple skill list (expand later)
skills_list = [
    "python", "sql", "pandas", "machine learning",
    "power bi", "data visualization", "communication"
]

def extract_skills(text):
    return {skill for skill in skills_list if skill in text}

def match_resume(resume, jd):
    resume_skills = extract_skills(resume)
    jd_skills = extract_skills(jd)

    matching = resume_skills & jd_skills
    missing = jd_skills - resume_skills

    score = int((len(matching) / len(jd_skills)) * 100)

    print("\nRESULT:\n")
    print(f"Match Score (0-100): {score}")
    print(f"Matching Skills: {', '.join(matching)}")
    print(f"Missing Skills: {', '.join(missing)}")
    print("Suggestions: Improve missing skills and add examples")
    print("Recruiter Summary: Candidate matches most technical requirements")

def main():
    match_resume(resume, jd)

if __name__ == "__main__":
    main()

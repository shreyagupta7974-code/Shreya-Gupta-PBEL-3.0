import fitz

from utils import (
    extract_name,
    extract_email,
    extract_phone,
    extract_linkedin,
    extract_github,
    extract_skills,
    clean_text
)

from ats_score import calculate_ats_score


def read_pdf(pdf_path):

    text = ""

    document = fitz.open(pdf_path)

    for page in document:
        text += page.get_text()

    document.close()

    return clean_text(text)

def extract_education(text):

    education_keywords = [

        "b.tech",
        "btech",
        "b.e",
        "be",
        "m.tech",
        "mca",
        "bca",
        "bsc",
        "msc",
        "engineering",
        "computer science",
        "information technology",
        "diploma"

    ]

    found = []

    lower = text.lower()

    for item in education_keywords:

        if item in lower:
            found.append(item.title())

    return list(set(found))



def extract_projects(text):

    keywords = [

        "project",
        "projects",
        "developed",
        "created",
        "built"

    ]

    lower = text.lower()

    return any(word in lower for word in keywords)

def extract_experience(text):

    keywords = [

        "experience",
        "internship",
        "worked",
        "company",
        "developer"

    ]

    lower = text.lower()

    return any(word in lower for word in keywords)


def extract_certifications(text):

    keywords = [

        "certificate",
        "certification",
        "coursera",
        "udemy",
        "nptel",
        "infosys",
        "aws"

    ]

    lower = text.lower()

    return any(word in lower for word in keywords)


def extract_achievements(text):

    keywords = [

        "achievement",
        "award",
        "winner",
        "hackathon",
        "competition",
        "rank"

    ]

    lower = text.lower()

    return any(word in lower for word in keywords)



def analyze_resume(pdf_path, job_description=""):

    text = read_pdf(pdf_path)

    name = extract_name(text)

    email = extract_email(text)

    phone = extract_phone(text)

    linkedin = extract_linkedin(text)

    github = extract_github(text)

    skills = extract_skills(text)

    education = extract_education(text)

    projects = extract_projects(text)

    experience = extract_experience(text)

    certifications = extract_certifications(text)

    achievements = extract_achievements(text)


    resume_data = {

        "name": name,

        "email": email,

        "phone": phone,

        "linkedin": linkedin,

        "github": github,

        "skills": skills,

        "education": education,

        "projects": projects,

        "experience": experience,

        "certifications": certifications,

        "achievements": achievements

    }


    ats_result = calculate_ats_score(

        resume_data,

        job_description

    )


    result = {

        "name": name,

        "email": email,

        "phone": phone,

        "linkedin": linkedin,

        "github": github,

        "skills": skills,

        "education": education,

        "projects": projects,

        "experience": experience,

        "certifications": certifications,

        "achievements": achievements,

        "ats_score": ats_result.get("ats_score", 0),

        "match_score": ats_result.get("match_score", 0),

        "quality": ats_result.get("quality", "Average"),

        "strengths": ats_result.get("strengths", []),

        "weaknesses": ats_result.get("weaknesses", []),

        "suggestions": ats_result.get("suggestions", []),

        "resume_text": text

    }

    return result
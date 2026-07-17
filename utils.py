import re

def extract_email(text):

    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


def extract_phone(text):

    pattern = r"(\+91[-\s]?)?[6-9]\d{9}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"



def extract_linkedin(text):

    pattern = r"(https?:\/\/)?(www\.)?linkedin\.com\/[^\s]+"

    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        return match.group()

    return "Not Found"



def extract_github(text):

    pattern = r"(https?:\/\/)?(www\.)?github\.com\/[^\s]+"

    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        return match.group()

    return "Not Found"


def extract_name(text):

    lines = text.split("\n")

    ignore_words = [

        "resume",
        "curriculum",
        "vitae",
        "email",
        "phone",
        "mobile",
        "address",
        "github",
        "linkedin"

    ]

    for line in lines:

        line = line.strip()

        if len(line) < 3:

            continue

        if len(line) > 35:

            continue

        if any(char.isdigit() for char in line):

            continue

        lower = line.lower()

        if any(word in lower for word in ignore_words):

            continue

        if len(line.split()) >= 2:

            return line

    return "Not Found"




def extract_skills(text):

    skills_database = [

        "Python",
        "Java",
        "C",
        "C++",
        "HTML",
        "CSS",
        "JavaScript",
        "Flask",
        "Django",
        "MySQL",
        "SQL",
        "MongoDB",
        "Machine Learning",
        "Deep Learning",
        "Artificial Intelligence",
        "Data Analysis",
        "Pandas",
        "NumPy",
        "Power BI",
        "Excel",
        "Git",
        "GitHub",
        "AWS",
        "Docker",
        "Linux",
        "React",
        "Node.js",
        "Bootstrap",
        "Tailwind CSS"

    ]

    found = []

    lower_text = text.lower()

    for skill in skills_database:

        if skill.lower() in lower_text:

            found.append(skill)

    return sorted(list(set(found)))



def clean_text(text):

    text = text.replace("\t", " ")
    text = text.replace("\r", " ")
    text = re.sub(r"\n+", "\n", text)
    text = re.sub(r"[ ]+", " ", text)

    return text.strip()

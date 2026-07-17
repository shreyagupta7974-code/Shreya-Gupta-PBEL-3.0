

def calculate_ats_score(resume_data, job_description=""):

    score = 0

    strengths = []
    weaknesses = []
    suggestions = []

   

    if resume_data["name"] != "Not Found":

        score += 5
        strengths.append("Name detected successfully.")

    else:

        weaknesses.append("Name not found.")
        suggestions.append("Add your full name at the top of your resume.")


    if resume_data["email"] != "Not Found":

        score += 10
        strengths.append("Professional email available.")

    else:

        weaknesses.append("Email missing.")
        suggestions.append("Add a professional email address.")

    

    if resume_data["phone"] != "Not Found":

        score += 10
        strengths.append("Phone number available.")

    else:

        weaknesses.append("Phone number missing.")
        suggestions.append("Add your contact number.")

 

    skill_count = len(resume_data["skills"])

    if skill_count >= 8:

        score += 20
        strengths.append("Excellent technical skills.")

    elif skill_count >= 5:

        score += 15
        strengths.append("Good technical skills.")

    elif skill_count >= 3:

        score += 10
        weaknesses.append("Moderate technical skills.")
        suggestions.append("Add more relevant technical skills.")

    else:

        weaknesses.append("Very few technical skills.")
        suggestions.append("Mention your technical skills clearly.")

  

    if resume_data["education"]:

        score += 10
        strengths.append("Education section found.")

    else:

        weaknesses.append("Education section missing.")
        suggestions.append("Add your education details.")

  

    if resume_data["projects"]:

        score += 15
        strengths.append("Projects section available.")

    else:

        weaknesses.append("Projects missing.")
        suggestions.append("Add academic or personal projects.")

    if resume_data["experience"]:

        score += 10
        strengths.append("Experience section found.")

    else:

        weaknesses.append("Experience not found.")
        suggestions.append("Add internship or work experience.")


    if resume_data["certifications"]:

        score += 10
        strengths.append("Certifications available.")

    else:

        weaknesses.append("No certifications.")
        suggestions.append("Complete certifications from Coursera, NPTEL or similar platforms.")

  
    if resume_data["github"] != "Not Found":

        score += 5
        strengths.append("GitHub profile available.")

    else:

        weaknesses.append("GitHub profile missing.")
        suggestions.append("Add your GitHub profile.")

   

    if resume_data["linkedin"] != "Not Found":

        score += 5
        strengths.append("LinkedIn profile available.")

    else:

        weaknesses.append("LinkedIn profile missing.")
        suggestions.append("Add your LinkedIn profile.")


    if score > 100:
        score = 100

    match_score = score


    if score >= 90:

        quality = "Excellent"

    elif score >= 75:

        quality = "Good"

    elif score >= 60:

        quality = "Average"

    else:

        quality = "Needs Improvement"


    return {

        "ats_score": score,

        "match_score": match_score,

        "quality": quality,

        "strengths": strengths,

        "weaknesses": weaknesses,

        "suggestions": suggestions

    }
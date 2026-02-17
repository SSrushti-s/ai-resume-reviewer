from app.pdf_loader import extract_text_from_pdf
from app.agent import get_resume_review
import json

if __name__ == "__main__":
    # 1. Load the Resume
    resume_content = extract_text_from_pdf("data\Srushti S - Computer Science and Engineering Student Resume (2).pdf")

    # 2. Define the Job Description (In a real app, this comes from a MERN input)
    job_desc = """
    Looking for a Front-End Developer proficient in React, Node.js, and MongoDB. 
    Experience with AI integration and Python is a plus.
    """

    # 3. Get the Review
    print("Analyzing Resume... please wait.")
    try:
        result = get_resume_review(resume_content, job_desc)

        print("\n===== AI RESUME REVIEW (JSON) =====")
        pretty_result = json.dumps(result, indent=4)
        
        print(pretty_result)
        
        # Example of accessing specific data
        print(f"\nMatch Score: {result['match_percentage']}%")
        
    except Exception as e:
        print(f"An error occurred: {e}")
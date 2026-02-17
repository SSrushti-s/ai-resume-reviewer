import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from app.prompts import RESUME_REVIEWER_PROMPT
from langchain_groq import ChatGroq

load_dotenv()

def get_resume_review(resume_text, job_description):
    # 1. Initialize Gemini Model
    llm = ChatGroq(
        model_name="llama-3.3-70b-versatile", 
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

    # 2. Create the Parser
    parser = JsonOutputParser()

    # 3. Format the Prompt (The Right Way)
    prompt = ChatPromptTemplate.from_messages([
        ("system", RESUME_REVIEWER_PROMPT),
        ("user", "Job Description:\n{jd}\n\nResume Content:\n{resume}")
    ])

    # 4. Create the Chain (Prompt -> Model -> Parser)
    chain = prompt | llm | parser

    # 5. Execute
    response = chain.invoke({
        "resume": resume_text,
        "jd": job_description
    })
    
    return response
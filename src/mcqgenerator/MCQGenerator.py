from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableLambda
from langchain_core.output_parsers import JsonOutputParser 
import PyPDF2
import json

from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

def extract_content(ai_message, subject=None):
    return {"quiz": ai_message.content, "subject": subject}


llm = ChatGroq(model="openai/gpt-oss-20b")

TEMPLATE = """
Text:{text}
You are an expert MCQ maker. Given the above text, it is your job to create a quiz of {number} 
multiple choice questions for {subject} students in {tone} tone. Make sure the questions are 
not repeated and check all the questions to be conforming the text as well. Make sure to format 
your response like RESPONSE_JSON below and use it as a guide. Ensure to make {number} MCQs
### RESPONSE_JSON {response_json}
"""

TEMPLATE2 = """
You are an expert english grammarian and writer. Given a Multiple Choice Quiz for {subject} students.
You need to evaluate the complexity of the question and give a complete analysis of the quiz. 
Only use at max 50 words for complexity. If the quiz is not as per with the congnitive and analytical 
abilities of the students, updata the quiz questions which needs to be changed the tone such that it 
perfectly fits the student abilities.
Quiz_MCQs: {quiz} 
"""

# tone means complexity of quiz like, easy, moderate, hard
prompt1 = PromptTemplate(
    template=TEMPLATE,
    input_variables=["text", "number", "tone", "response_json", "subject"]
)

prompt2 = PromptTemplate(
    template=TEMPLATE2,
    input_variables=["quiz", "subject"]
)

prompt3 = RunnableLambda(extract_content)

parser = JsonOutputParser()

quiz_chain = prompt1 | llm
review_chain = prompt2 | llm
final_chain = quiz_chain | prompt3 | review_chain | parser
import os
import PyPDF2
import json
import traceback

def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader = PyPDF2.PdfFileReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        
        except Exception as e:
            raise Exception("error reading the PDF file")
        
    elif file.name.endswith(".txt"):
        return file.read().decode('utf-8')
    
    else:
        raise Exception("Unsupported file format only pdf and text file supported")
    
def get_table_data(quiz):
    
    try:
        quiz_table_data = []
        for i in quiz:
            question = quiz[i]['mcq']
            options = quiz[i]["options"]
            option_str = ""
            for j, k in options.items():
                option_str = option_str + f" {j}: {k} |"
            corect_answer = quiz[i]["correct"]
            
            quiz_table_data.append({"MCQ": question, "Choices": option_str[:-1], "Correct": corect_answer})
        
        return quiz_table_data
    
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)  
        return False   
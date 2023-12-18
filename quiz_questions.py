from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Set your OpenAI API key
API_KEY = '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'

def parse_result(result):
    q_start = result.find("Question:") + len("Question:")
    q_end = result.find("A.", q_start, len(result))
    question = result[q_start : q_end]
    
    a_end = result.find("B.", q_end, len(result))
    option_a = result[q_end + 2, a_end]

    b_end = result.find("C.", a_end, len(result))
    option_b = result[a_end + 2, b_end]

    c_end = result.find("D.", b_end, len(result))
    option_c = result[b_end + 2, c_end]

    d_end = result.find("Answer:", c_end, len(result))
    option_d = result[c_end + 2, d_end]

    ans_end = result.find("Answer:", d_end, len(result))
    answer = result[d_end + 7, ans_end]

    if 'A.' in answer:
        ans_op = 'A'
    elif 'B.' in answer:
        ans_op = 'B'
    elif 'C.' in answer:
        ans_op = 'C'
    else:
        ans_op = 'D'

    res = {'question' : question,
           'option_a' : option_a,
           'option_b' : option_b,
           'option_c' : option_c,
           'option_d' : option_d,
          'answer' : answer,
          'correct_option' : ans_op}
    return res
        

# Function to generate quiz questions and answers using Langchain and OpenAI's Chat Completion API
def generate_quiz(topic, num_questions):
    # Generate questions based on the topic using Langchain
    template = "Question: {question}"
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm = OpenAI(openai_api_key=API_KEY)

    llm_chain = LLMChain(prompt=prompt, llm=llm)
    question = f'''Assume you are a professor at a top university. Make an MCQ-type question and answer on  the topic "{topic}" and give me the result in the format 
                    Question: {question}
                    A. {option 1}
                    B. {option 2}
                    C. {option 3}
                    D. {option 4}
                    
                    Answer: {correct option letter}'''
    # results = [parse_result(llm_chain.run(question)) for i in range(num_questions)]

    response = """
            Certainly, here's an example of an MCQ type question on the topic of world politics in the requested format:
            
            Question:
            What is the term used to describe the situation where a country’s government is run by a single individual who holds absolute power and often suppresses opposition?
            
            A. Autocracy
            B. Oligarchy
            C. Democracy
            D. Theocracy
            
            Answer:
            A. Autocracy"""

    results = [parse_result(response) for i in range(num_questions)]

    return results

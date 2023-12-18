import langchain
import openai
import os
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Set your OpenAI API key
openai.api_key = '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'
os.environ["OPENAI_API_KEY"] = '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'

# Function to generate quiz questions and answers using Langchain and OpenAI's Chat Completion API
def generate_quiz(topic, num_questions):
    # Generate questions based on the topic using Langchain
    template = "Question: {question}"
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm = OpenAI()

    llm_chain = LLMChain(prompt=prompt, llm=llm)
    question = f"Create a multiple-choice quiz about {topic}."
    results = [llm_chain.run(question) for i in range(num_questions)]

    return results

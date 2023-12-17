#import openai

#openai.api_key = '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'

#def generate_quiz(topic):
    prompt = f"Create a multiple-choice quiz about {topic}. Questions:\n1."
    response = openai.ChatCompletion.create(
        model="text-davinci-003",
        messages=[
            {"role": "system", "content": prompt}
        ],
        max_tokens=150
    )
    # Extracting generated quiz questions from the OpenAI response
    quiz_questions = response['choices'][0]['message']['content']
    return quiz_questions

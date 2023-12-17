import streamlit as st
import openai

# Set up OpenAI API credentials
openai.api_key = "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"

def generate_quiz(topic: str):
    """
    Generates an AI-powered multiple choice quiz using langchain and streamlit.

    Parameters:
    - topic: str
        The topic for which the quiz is generated.

    Returns:
    - None
        The function displays the generated quiz and the user's score.

    Raises:
    - ValueError:
        Raises an error if the topic is not provided.
    """

    # Validate the topic
    if not topic:
        raise ValueError("Please provide a topic for the quiz.")

    # Generate quiz using OpenAI Chat Completion API
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Generate a multiple choice quiz on {topic}.",
        max_tokens=100,
        n=5,
        stop=None,
        temperature=0.7
    )

    # Extract quiz questions from the API response
    questions = response.choices[0].text.strip().split("\n")

    # Display the quiz using Streamlit
    st.title("AI-powered Multiple Choice Quiz")
    st.write(f"Topic: {topic}")
    st.write("Instructions: Select the correct option for each question.")
    st.write("")

    # Initialize score
    score = 0

    # Display each question and get user's answer
    for i, question in enumerate(questions):
        st.write(f"Question {i+1}: {question}")
        options = ["Option A", "Option B", "Option C", "Option D"]
        user_answer = st.radio("Select your answer:", options)
        correct_answer = "Option A"  # Assuming Option A is always the correct answer

        # Check if user's answer is correct
        if user_answer == correct_answer:
            score += 1

    # Display the user's score
    st.write("")
    st.write(f"Your score: {score}/{len(questions)}")

# Example usage
generate_quiz("Python Programming")

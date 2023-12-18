import streamlit as st
from quiz_questions import generate_quiz
# Function to display the quiz questions
def display_quiz(quiz_data):
    for i, question_data in enumerate(quiz_data):
        st.markdown(f"### Question {i + 1}: {question_data['question']}\")
        st.markdown(f"A. {question_data['option_a']}\")
        '''
        st.radio(f"A_{i}", question_data['option_a'])
        st.radio(f"B_{i}", question_data['option_b'])
        st.radio(f"C_{i}", question_data['option_c'])
        st.radio(f"D_{i}", question_data['option_d'])
        '''

        st.markdown("\\")

def main():
    st.title("MCQ Quiz Application")

    # User inputs for topic and number of questions
    topic = st.text_input("Enter the topic for the quiz:")
    num_questions = st.number_input("Number of questions:", min_value=1, max_value=10, value=5, step=1)

    if st.button("Start Quiz"):
        if topic:
            # Generate quiz questions and answers
            quiz_data = generate_quiz(topic, num_questions)
            # Display the quiz questions
            display_quiz(quiz_data)
            st.button("Submit Quiz")  # Add functionality to submit the quiz
        else:
            st.warning("Please enter a topic to start the quiz.")

if __name__ == "__main__":
    main()

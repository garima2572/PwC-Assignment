import streamlit as st
from quiz_questions import generate_quiz


def main():
    st.title("MCQ Quiz Application")

    # User inputs for topic and number of questions
    topic = st.text_input("Enter the topic for the quiz:")
    num_questions = st.number_input("Number of questions:", min_value=1, max_value=10, value=5, step=1)

    # Generate quiz questions and answers
    quiz_data = generate_quiz(topic, num_questions)

    question_options = []
    for i, question_data in enumerate(quiz_data):
        st.markdown(f"### Question {i + 1}: {question_data['question']}")
        radio = st.radio(
                    "Select the most appropriate option",
                    ["A.", "B.", "C.", "D."],
                    captions = [question_data['option_a'], question_data['option_b'],
                               question_data['option_c'], question_data['option_d']], key = f'ques_{i}')
        question_options.append(radio)

        if radio == question_data["correct_option"]:
            st.write('Correct option.')
        else:
            st.write('Incorrect option.')


if __name__ == "__main__":
    main()

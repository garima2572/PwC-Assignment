import streamlit as st
from quiz_questions import generate_quiz


def main():
    st.title("MCQ Quiz Application")

    with st.form('Prompt'):
        # User inputs for topic and number of questions
        topic = st.text_input("Enter the topic for the quiz:")
        num_questions = st.number_input("Number of questions:", min_value=1, max_value=10, value=5, step=1)
    
        # Generate quiz questions and answers
        quiz_data = generate_quiz(topic, num_questions)
    
        submit_prompt = st.form_submit_button('Generate questions')

    question_options = []
    with st.form('Questions'):
        if submit_prompt:
            question_options.clear()
            for i, question_data in enumerate(quiz_data):
                st.write(f"Question {i + 1}: {question_data['question']}")
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

            submit_ans = st.form_submit_button('Submit Answers')
            
            if submit_ans:
                n_correct = 0
                for i, question_data in enumerate(quiz_data):
                    radio = question_options[i]
                    if radio == question_data["correct_option"]:
                        st.write(f"For question {i + 1}: ")
                        st.write(f'\t Correct ans = {question_data["correct_option"]} ')
                        st.write(f'\t Selected ans = {radio} ')
                        n_correct += 1
                st.write(f"You scored {n_correct} / {len(quiz_data)}")
                st.write(f"Percentage {n_correct * 100 / len(quiz_data)}")

if __name__ == "__main__":
    main()

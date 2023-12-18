import streamlit as st
from quiz_questions import generate_quiz

if 'stage' not in st.session_state:
    print("Reset", flush=True)
    st.session_state.stage = 0
    
def set_stage(stage):
    st.session_state.stage = stage

def get_stage():
    return st.session_state.stage

def render_result(question_options, quiz_data):
    set_stage(2)
    n_correct = 0
    print("Ques ops : ", question_options, flush = True)
    for i, question_data in enumerate(quiz_data):
        radio = question_options[i]
        if radio == question_data["correct_option"]:
            st.markdown(f"# For question {i + 1}: ")
            st.write(f'Correct ans = {question_data["correct_option"]}')
            st.write(f'\t Selected ans = {radio} ')
            n_correct += 1
    st.write("# Overall Results:")
    st.write(f"You scored {n_correct} / {len(quiz_data)}")
    st.write(f"Percentage {n_correct * 100 / len(quiz_data)}")

question_options = []
def main():
    global question_options
    st.title("MCQ Quiz Application")

    
    # User inputs for topic and number of questions
    topic = st.text_input("Enter the topic for the quiz:")
    num_questions = st.number_input("Number of questions:", min_value=1, max_value=10, value=5, step=1)

    # Generate quiz questions and answers
    quiz_data = generate_quiz(topic, num_questions)

    st.button('Generate questions', on_click=set_stage, args=(1,))

    
    if get_stage() == 1:
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
        print("Ques ops : ", question_options, flush = True)
        selected_ans = question_options.copy()
        st.button('Submit Answers', on_click=render_result, args=(question_options, quiz_data))


if __name__ == "__main__":
    main()

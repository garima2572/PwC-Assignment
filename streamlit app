import streamlit as st

# Function to display the generated quiz questions
def display_quiz(questions):
    st.markdown(f"## Quiz Questions\n{questions}")

def main():
    st.title("MCQ Quiz Generator")

    # User input for topic
    topic = st.text_input("Enter the topic for the quiz:")

    if st.button("Generate Quiz"):
        if topic:
            quiz_questions = generate_quiz(topic)
            display_quiz(quiz_questions)
        else:
            st.warning("Please enter a topic.")

if __name__ == "__main__":
    main()

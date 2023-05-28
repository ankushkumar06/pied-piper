import streamlit as st
import openai
# Set up OpenAI API credentials
openai.api_key = 'OPEN_AI_KEY'

# Define Streamlit app layout
def app():
    st.title("Job Description Generator")
    st.write("Automatically generate job descriptions using AI")

    # Job description input
    job_title = st.text_input("Job Title")
    job_summary = st.text_area("Job Summary")

    # Generate job description on button click
    if st.button("Generate"):
        if job_title and job_summary:
            prompt = f"Give me the job description for {job_title} in the markdown format."
            max_tokens = 200  # Adjust the desired length of the generated job description
            response = openai.Completion.create(
                engine='text-davinci-003',  # Choose the OpenAI language model
                prompt=prompt,
                max_tokens=max_tokens,
                n=1,
                stop=None,
                temperature=0.7  # Adjust the temperature for more conservative or creative outputs
            )
            generated_description = response.choices[0].text.strip()
            st.markdown(generated_description)
            # Now creating interview questions
            prompt = f"Give me ten interview questions for {job_title} in the markdown format."
            st.subheader("Generated Interview questions")
            response = oa.Completion.create(
                engine='text-davinci-003',  # Choose the oa language model
                prompt=prompt,
                max_tokens=max_tokens,
                n=1,
                stop=None,
                temperature=0.7  # Adjust the temperature for more conservative or creative outputs
            )
            generated_description = response.choices[0].text
            st.markdown(generated_description)
        else:
            st.write("Please enter the job title and summary.")

# Run the Streamlit app

app()

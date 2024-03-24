import streamlit as st
import base64
from ml_backend import ml_backend

# Set the title and introductory text of the app
st.title("AI TUTOR V0.0")
st.text("Welcome to AI TUTOR")
# Provide some instructions or description about the app
st.markdown(""" 
# Ask text or upload visual query""")

# Initialize ML backend
backend = ml_backend()

# Create a form for user input
with st.form(key="form"):
    # Input field for user query
    prompt = st.text_input("Describe your query")

    # Upload image option
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    # Submit button to trigger message generation
    submit_button = st.form_submit_button(label='Generate Message')

    # Check if the submit button is clicked
    if submit_button:
        # Generate message based on user query and uploaded image
        with st.spinner("Generating message..."):
            if uploaded_image is not None:
                # Convert the uploaded image to base64
                image_data = base64.b64encode(uploaded_image.read()).decode("utf-8")
                output = backend.generate_message(prompt, image_data)
            else:
                output = backend.generate_message(prompt)
        
        # Display the generated message
        st.markdown("# Message Output:")
        st.subheader(output)
        st.markdown("____")
        st.subheader("You can press the Generate Message Button again if you're unhappy with the model's output")

        # Provide option to send the generated message via email
        st.markdown("# Send Your message")
        st.text(output)  # Display the message text
        url = "https://mail.google.com/mail/?view=cm&fs=1&to=&su=&body=" + backend.replace_spaces_with_pluses(output)
        #st.markdown("[Click here to send the email]({})".format(url))

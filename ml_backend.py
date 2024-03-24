import openai

class ml_backend:
        
    openai.api_key = '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'

    def generate_message(self, user_prompt="Ask Question", image_data=None):
        """Generate a message based on user prompt and optional image data"""
        prompt = user_prompt + "\n\nPlease respond"
        if image_data:
            prompt += "\n\n![Image](data:image/jpeg;base64," + image_data + ")"
        
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=prompt,
            temperature=0.71,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.36,
            presence_penalty=0.75
        )
        return response.choices[0].text.strip()

    def replace_spaces_with_pluses(self, sample):
        """Replace spaces with pluses"""
        return sample.replace(" ", "+")

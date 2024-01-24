import streamlit as st
import base64
import requests
import os

# from openai_api import extract_food_from_image, chatgpt  # Uncomment if these functions are available in your environment


def encode_image(uploaded_file):
    # Read the uploaded file and encode it to base64
    return base64.b64encode(uploaded_file.getvalue()).decode("utf-8")


def analyze_image_with_openai(base64_image):
    api_key = os.environ.get("OPENAI_API_KEY")
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What food are in the refrigerator? Do NOT generate any openings other than the list of foods in the image. ONLY GIVE ME THE INGREDIENTS in bullet points",
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                ],
            }
        ],
        "max_tokens": 300,
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions", headers=headers, json=payload
    )
    return response


def analyze_image_with_openai(base64_image, api_key):
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What’s in this image?"},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                ],
            }
        ],
        "max_tokens": 300,
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions", headers=headers, json=payload
    )
    return response


def main():
    st.title("Food Preference Finder")

    # User input via Streamlit widgets
    cuisine = st.selectbox(
        "Are you in the mood for any particular cuisine today?",
        ["Italian", "Mexican", "Asian", "Other"],
        index=0,
    )
    diet = st.selectbox(
        "Do you have any dietary restrictions or preferences?",
        ["None", "Vegetarian", "Vegan", "Gluten-Free", "Low-Carb"],
        index=0,
    )
    flavor = st.selectbox(
        "What kind of flavors are you craving today?",
        ["Spicy", "Sweet", "Savory", "Mix"],
        index=2,
    )
    meal_type = st.selectbox(
        "Are you looking for something light or hearty?",
        ["Light (Salad, Sandwich)", "Hearty (Pasta, Steak)"],
        index=1,
    )

    preferences = (
        f"\nYour Food Preferences:\n"
        f"Cuisine Preference: {cuisine}\n"
        f"Dietary Restrictions: {diet}\n"
        f"Flavor Profile: {flavor}\n"
        f"Meal Type: {meal_type}"
    )

    # Image upload
    uploaded_file = st.file_uploader(
        "Upload an image of the contents of your fridge", type=["png", "jpg", "jpeg"]
    )

    if uploaded_file is not None:
        # Encode the uploaded image to base64
        base64_image = encode_image(uploaded_file)

        # Display the uploaded image (optional)
        st.image(uploaded_file, caption="Uploaded Fridge Image.", use_column_width=True)
        

    if st.button("Find Recipe"):
        response = analyze_image_with_openai(base64_image)
        print(response)
        # Uncomment and use the appropriate function calls if these are actual functions in your environment
        # main_prompt = """
        # Given my food preferences and ingredients I have in my fridge, what should I cook for dinner tonight? Make me a full recipe.
        #
        # My food preferences:
        # {preferences}
        #
        # Ingredients I have in my fridge:
        # {ingredients}
        # """.format(preferences=preferences, ingredients=ingredients)
        #
        # response = chatgpt(main_prompt.strip())
        # st.text(response)

        # Placeholder response
        st.text("This is where the recipe response would appear.")


if __name__ == "__main__":
    main()

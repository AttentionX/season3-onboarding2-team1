import streamlit as st
from openai_api import extract_food_from_image, chatgpt


def main():
    st.title("Refrigerator Chef 🧑‍🍳🍽️")

    st.markdown("## Let's find the perfect meal for you today! 🍜")
    st.markdown("Tell us about your preferences and what's in your fridge.")

    with st.expander("Set Your Food Preferences"):
        cuisine = st.selectbox(
            "Cuisine Preference:",
            ["Italian", "Mexican", "Asian", "Other"],
            index=0,
        )
        diet = st.selectbox(
            "Dietary Restrictions:",
            ["None", "Vegetarian", "Vegan", "Gluten-Free", "Low-Carb"],
            index=0,
        )
        flavor = st.selectbox(
            "Flavor Profile:",
            ["Spicy", "Sweet", "Savory", "Mix"],
            index=2,
        )
        meal_type = st.selectbox(
            "Meal Type:",
            ["Light (Salad, Sandwich)", "Hearty (Pasta, Steak)"],
            index=1,
        )

    preferences = (
        f"Cuisine Preference: {cuisine}\n"
        f"Dietary Restrictions: {diet}\n"
        f"Flavor Profile: {flavor}\n"
        f"Meal Type: {meal_type}"
    )

    st.markdown("## Now, show us what's in your fridge! 📸")
    image_link = st.text_input(
        "Enter the link to an image of the contents of your fridge:",
        "https://healsview.com/wp-content/uploads/2023/10/open-fridge-or-1024x683.jpg",
    )

    if st.button("Find Recipe"):
        ingredients = extract_food_from_image(image_link)
        
        col1, col2 = st.columns(2)
        with col1:
            st.image(image_link, caption="Image from URL", use_column_width=True)
        with col2:
            st.markdown(f"**Ingredients in your fridge:**\n{ingredients}")

        main_prompt = """
        Given my food preferences and ingredients I have in my fridge, what should I cook for dinner tonight? DO NOT use any additional ingredients. Make me a full recipe. Write your response in markdown.
        
        My food preferences:
        {preferences}
        
        Ingredients I have in my fridge:
        {ingredients}
        """.format(
            preferences=preferences, ingredients=ingredients
        )

        response = chatgpt(main_prompt.strip())

        st.markdown("## Your Custom Recipe 📖")
        st.markdown(response)


if __name__ == "__main__":
    main()

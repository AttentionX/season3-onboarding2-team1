import streamlit as st
from openai_api import extract_food_from_image, chatgpt

def main():
    st.title("냉장고 속 재료로 레시피 추천해주는 AI")

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

    # Image link input
    image_link = st.text_input(
        "Enter the link to an image of the contents of your fridge:",
        "https://healsview.com/wp-content/uploads/2023/10/open-fridge-or-1024x683.jpg",
    )

    if st.button("Find Recipe"):
        # Uncomment and use the appropriate function calls if these are actual functions in your environment
        ingredients = extract_food_from_image(image_link)
        
        print(ingredients)
        main_prompt = """
        Given my food preferences and ingredients I have in my fridge, what should I cook for dinner tonight? Make me a full recipe.
        
        My food preferences:
        {preferences}
        
        Ingredients I have in my fridge:
        {ingredients}
        """.format(preferences=preferences, ingredients=ingredients)
        
        response = chatgpt(main_prompt.strip())
        
        print(response)
        st.text(response)

        # Placeholder response
        # st.text("This is where the recipe response would appear.")


if __name__ == "__main__":
    main()

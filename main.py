import click


@click.command()
@click.option(
    "--cuisine",
    default="Italian",
    prompt="Are you in the mood for any particular cuisine today, like Italian, Mexican, Asian, or something else?",
    help="Your preferred cuisine.",
)
@click.option(
    "--diet",
    default="None",
    prompt="Do you have any dietary restrictions or preferences I should be aware of, like vegetarian, vegan, gluten-free, or low-carb?",
    help="Your dietary restrictions, if any.",
)
@click.option(
    "--flavor",
    default="Savory",
    prompt="What kind of flavors are you craving today? Something spicy, sweet, savory, or maybe a mix?",
    help="Your preferred flavor profile.",
)
@click.option(
    "--meal_type",
    default="Hearty",
    prompt="Are you looking for something light like a salad or sandwich, or something more hearty like a pasta dish or a steak?",
    help="Your preferred meal type.",
)
def main(cuisine, diet, flavor, meal_type):
    """
    A CLI application to find out your food preferences for today.
    """
    click.echo("\nYour Food Preferences:")
    click.echo(f"Cuisine Preference: {cuisine}")
    click.echo(f"Dietary Restrictions: {diet}")
    click.echo(f"Flavor Profile: {flavor}")
    click.echo(f"Meal Type: {meal_type}")


if __name__ == "__main__":
    main()

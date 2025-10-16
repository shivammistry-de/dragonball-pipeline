import requests

# This API fetches Dragon Ball characters.
# We are specifically filtering for Saiyans who are also Z Fighters.
API_URL = "https://dragonball-api.com/api/characters?race=Saiyan&affiliation=Z fighter"

def fetch_character_data():
    """Fetches data for Dragon Ball characters from the API."""
    print("Fetching character data from Dragon Ball API...")
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Check for any HTTP errors
        data = response.json()
        print("Successfully fetched character data.")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def save_data(characters):
    """Saves the relevant character data to a file."""
    if not characters:
        print("No character data to save.")
        return

    # Create a string to hold our output
    output_content = "SAIYAN Z FIGHTERS:\n"
    output_content += "-------------------\n"

    # The response is a direct list of characters, so we loop through it
    for char in characters:
        name = char.get('name', 'Unknown Name')
        ki = char.get('ki', 'Unknown Ki')
        output_content += f"- Name: {name}, Ki: {ki}\n"
    
    try:
        with open("z_fighters.txt", "w", encoding="utf-8") as f:
            f.write(output_content)
        print("Data successfully saved to z_fighters.txt")
    except IOError as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    character_data = fetch_character_data()
    save_data(character_data)


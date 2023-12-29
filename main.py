from PIL import Image, ImageDraw, ImageFont
import os

def create_card(number, suit):
    # Define ASCII symbols
    symbols = {
        "H": "♥",
        "D": "♦",
        "C": "♣",
        "S": "♠",
    }

    # Create a blank image with white background
    card_width, card_height = 150, 200
    card_image = Image.new("RGB", (card_width, card_height), "white")
    draw = ImageDraw.Draw(card_image)

    # Draw card outline
    outline_width = 2
    draw.rectangle([(0, 0), (card_width, card_height)], outline="black", width=2)

    # Load font for text
    font_size = 20

    # Draw top-left symbol
    paste_position = (outline_width, outline_width)
    symbol_image = draw_symbol(symbols, font_size, suit)
    card_image.paste(symbol_image, paste_position)

    # Draw bottom-right symbol
    paste_position = (card_width - font_size - outline_width, card_height - (2 * font_size) - outline_width)
    symbol_image = draw_symbol(symbols, font_size, suit, 180)
    card_image.paste(symbol_image, paste_position)

    # Draw front image
    font_size = 80
    paste_position = (int(((card_width) / 2) - (font_size / 2)) , int(((card_height) / 2) - (font_size / 2)))
    symbol_image = draw_front(symbols, font_size, suit)
    card_image.paste(symbol_image, paste_position)

    return card_image

def draw_front(symbols, font_size, suit):
    font = ImageFont.truetype("arial.ttf", font_size)
    
    symbol_width = font_size
    symbol_height = font_size

    symbol_image = Image.new("RGB", (symbol_width, symbol_height), "white")
    draw = ImageDraw.Draw(symbol_image)

    if suit == "H" or suit == "D":
        fill_color = 'red'
    else:
        fill_color = 'black'

    # Calculate the center position
    symbol_position = (symbol_width / 2, symbol_height / 2)

    draw.text(symbol_position, symbols[suit], font=font, fill=fill_color, anchor='mm')    
    
    return symbol_image    
    

def draw_symbol(symbols, font_size, suit, rotate = None):

    font = ImageFont.truetype("arial.ttf", font_size)
    
    symbol_width = font_size
    symbol_height = 2 * font_size

    symbol_image = Image.new("RGB", (symbol_width, symbol_height), "white")
    draw = ImageDraw.Draw(symbol_image)

    if suit == "H" or suit == "D":
        fill_color = 'red'
    else:
        fill_color = 'black'

    height_offset = 15
    width_offset = 2
    symbol_position = ((symbol_width / 2) + width_offset, height_offset + font_size)
    text_position = ((symbol_width / 2) + width_offset, height_offset)

    draw.text(symbol_position, symbols[suit], font=font, fill=fill_color, anchor='mm')    
    draw.text(text_position, f"{number[0]}", font=font, fill=fill_color, anchor='mm')
    
    if rotate == None:
        return symbol_image    
    else:
        return symbol_image.rotate(rotate)
        
if __name__ == "__main__":
 
    # List of card numbers and suits
    numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["H", "D", "C", "S"]

    # Create a deck of cards
    deck = [(number, suit) for number in numbers for suit in suits]

    # Output directory
    output_directory = "deck_of_cards"

    if os.path.exists(output_directory) == False:
        os.makedirs(output_directory)

    # Create card images and save them
    for card in deck:
        number, suit = card
        card_image = create_card(number, suit)
        
        # Save the card image
        filename = f"{output_directory}/{number}{suit}.png"
        card_image.save(filename)

    print("Card images generated and saved.")
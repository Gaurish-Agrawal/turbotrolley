import cv2
from PIL import Image
import PIL.ImageOps  

import pytesseract
import numpy as np
import paddleocr
from paddleocr import PaddleOCR

# Callback function to display the coordinates of the points clicked on the image
def show_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        print(f"Mouse Coordinates: ({x}, {y})")

def play(path):
	# Read the image file
	image_path = path
	image = cv2.imread(image_path)
	# Display the image in a window
	cv2.imshow('Image', image)
	# Set the callback function for mouse events
	cv2.setMouseCallback('Image', show_coordinates)
	# Wait for a key press and close the image window
	cv2.waitKey(0)
	cv2.destroyAllWindows()





from transformers import pipeline

# Initialize a text classification pipeline with a pre-trained model
classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')

# Example list of items
items = [
    "almond milk", "banana chips", "blueberries", "tablet", "sweatshirt", "soundbar",
    "gouda cheese", "margarine", "fabric softener", "paper towels", "baby formula", "pacifiers",
    "bagels", "organic eggs", "turkey breast", "bell peppers", "granola", "basmati rice", "spaghetti",
    "tortilla chips", "espresso", "diet soda", "mineral water", "ice cream", "disinfectant spray", "compostable trash bags",
    "scouring pads", "antibacterial soap", "body wash", "facial moisturizer", "fitness tracker", "blouses", "sneakers", "windshield washer fluid",
    "synthetic motor oil", "LED bulbs", "wireless chargers", "lipstick", "greek yogurt", "protein bars", "gum", "action camera", "gaming laptop", "winter coat"
]

# Example user-provided categories
categories = [
    "dairy products", "snack items", "fruits and vegetables", "electronic devices", "clothing items",
    "cleaning supplies", "baby care products", "bakery items", "meat and seafood", "grains and cereals",
    "beverages", "frozen foods", "health and beauty products", "fitness and sports", "home essentials",
    "automotive products"
]

# Function to enhance descriptions for better context
def enhance_description(item):
    return f"The item '{item}' is commonly found in Walmart."

# Classify items
sorted_items = {category: [] for category in categories}

for item in items:
    # Enhance context of each item
    text = enhance_description(item)
    result = classifier(text, categories)
    
    # Get the most likely category
    category = result['labels'][0]
    
    sorted_items[category].append(item)


s = """
'hammer': 'Hardware',
    'screwdriver set': 'Hardware',
    'nails': 'Hardware',
    'screws': 'Hardware',
    'wrenches': 'Hardware',
    'drill': 'Hardware',
    'saw': 'Hardware',
    'tape measure': 'Hardware',
    'level': 'Hardware',
    'paint': 'Hardware',
    'paint brushes': 'Hardware',
    'TV': 'Electronics',
    'laptop': 'Electronics',
    'smartphone': 'Electronics',
    'tablet': 'Electronics',
    'headphones': 'Electronics',
    'bluetooth speaker': 'Electronics',
    'camera': 'Electronics',
    'printer': 'Electronics',
    'router': 'Electronics',
    'video game console': 'Electronics',
    'running shoes': 'Shoes',
    'sneakers': 'Shoes',
    'sandals': 'Shoes',
    'boots': 'Shoes',
    'dress shoes': 'Shoes',
    'slippers': 'Shoes',
    'high heels': 'Shoes',
    'dog food': 'Pets',
    'cat food': 'Pets',
    'bird seed': 'Pets',
    'aquarium': 'Pets',
    'dog leash': 'Pets',
    'cat litter': 'Pets',
    'pet toys': 'Pets',
    'fish food': 'Pets',
    'pet shampoo': 'Pets',
    'pet bed': 'Pets',
    'detergent': 'Chemicals',
    'bleach': 'Chemicals',
    'disinfectant': 'Chemicals',
    'cleaner': 'Chemicals',
    'air freshener': 'Chemicals',
    'milk': 'Grocery',
    'bread': 'Grocery',
    'eggs': 'Grocery',
    'cheese': 'Grocery',
    'butter': 'Grocery',
    'yogurt': 'Grocery',
    'vegetables': 'Grocery',
    'fruits': 'Grocery',
    'meat': 'Grocery',
    'pasta': 'Grocery',
    'rice': 'Grocery',
    'cereal': 'Grocery',
    'soda': 'Grocery',
    'coffee': 'Grocery',
    'tea': 'Grocery',
    'spices': 'Grocery',
    'onions': 'Grocery',
    'eggs': 'Grocery',
    'cheese': 'Grocery',
    'tomatoes': 'Grocery',
    'car battery': 'Automotive',
    'motor oil': 'Automotive',
    'car tires': 'Automotive',
    'windshield wipers': 'Automotive',
    'car wax': 'Automotive',
    'air freshener': 'Automotive',
    'car tools': 'Automotive',
    'notebooks': 'Stationery',
    'pens': 'Stationery',
    'pencils': 'Stationery',
    'markers': 'Stationery',
    'highlighters': 'Stationery',
    'binders': 'Stationery',
    'folders': 'Stationery',
    'paper': 'Stationery',
    'scissors': 'Stationery',
    'glue': 'Stationery',
    'diapers': 'Infants',
    'baby formula': 'Infants',
    'baby wipes': 'Infants',
    'baby clothes': 'Infants',
    'baby toys': 'Infants',
    'baby shampoo': 'Infants',
    'baby lotion': 'Infants',
    'basketball': 'Sports',
    'soccer ball': 'Sports',
    'tennis racket': 'Sports',
    'baseball bat': 'Sports',
    'yoga mat': 'Sports',
    'dumbbells': 'Sports',
    'treadmill': 'Sports',
    'acrylic paint': 'Crafts',
    'brushes': 'Crafts',
    'canvases': 'Crafts',
    'glue gun': 'Crafts',
    'yarn': 'Crafts',
    'knitting needles': 'Crafts',
    'fabric': 'Crafts',
    'scissors': 'Crafts',
    'microwave': 'Appliance',
    'blender': 'Appliance',
    'toaster': 'Appliance',
    'coffee maker': 'Appliance',
    'refrigerator': 'Appliance',
    'washing machine': 'Appliance',
    'dryer': 'Appliance',
    'dresses': 'Girl Cloth',
    'skirts': 'Girl Cloth',
    'tops': 'Girl Cloth',
    'pants': 'Girl Cloth',
    'shoes': 'Girl Cloth',
    't-shirts': 'Boy Cloth',
    'jeans': 'Boy Cloth',
    'shorts': 'Boy Cloth',
    'jackets': 'Boy Cloth',
    'shoes': 'Boy Cloth',
    'makeup': 'Beauty',
    'skincare': 'Beauty',
    'haircare': 'Beauty',
    'perfume': 'Beauty',
    'nail polish': 'Beauty',
    'action figures': 'Toys',
    'dolls': 'Toys',
    'board games': 'Toys',
    'puzzles': 'Toys',
    'lego sets': 'Toys',
    'remote control cars': 'Toys',
    'stuffed animals': 'Toys',
    'shirts': 'Men Cloth',
    'pants': 'Men Cloth',
    'suits': 'Men Cloth',
    'jackets': 'Men Cloth',
    'shoes': 'Men Cloth',
    'blouses': 'Lady Cloth',
    'skirts': 'Lady Cloth',
    'dresses': 'Lady Cloth',
    'pants': 'Lady Cloth',
    'shoes': 'Lady Cloth',
    'sofa': 'Furniture',
    'dining table': 'Furniture',
    'chairs': 'Furniture',
    'beds': 'Furniture',
    'wardrobes': 'Furniture',
    'coffee table': 'Furniture',
    'sheets': 'Bed/Bath',
    'blankets': 'Bed/Bath',
    'pillows': 'Bed/Bath',
    'towels': 'Bed/Bath',
    'bath mats': 'Bed/Bath',
    'shower curtains': 'Bed/Bath',
    'greeting cards': 'Hallmark',
    'gift wrap': 'Hallmark',
    'gift bags': 'Hallmark',
    'ribbons': 'Hallmark',
    'party supplies': 'Hallmark',
    'foundation': 'Cosmetics',
    'lipstick': 'Cosmetics',
    'mascara': 'Cosmetics',
    'eyeshadow': 'Cosmetics',
    'blush': 'Cosmetics',
    'christmas decorations': 'Seasonal',
    'halloween costumes': 'Seasonal',
    'easter eggs': 'Seasonal',
    'valentine cards': 'Seasonal',
    'fourth of July flags': 'Seasonal',
    'customer service': 'Service Desk',
    'returns': 'Service Desk',
    'exchanges': 'Service Desk',
    'photo printing': 'Photo Dept',
    'passport photos': 'Photo Dept',
    'photo books': 'Photo Dept',
    'canvas prints': 'Photo Dept',
    'eyeglasses': 'Vision Center',
    'contact lenses': 'Vision Center',
    'eye exams': 'Vision Center',
    'sunglasses': 'Vision Center',
    """

print(s.replace("'",'"'))
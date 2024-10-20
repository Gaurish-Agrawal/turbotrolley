import difflib
import cv2
import re
from paddleocr import PaddleOCR

from transformers import pipeline

def extract_text_from_image(img_path):
    
    ocr = PaddleOCR(use_angle_cls=True, lang='en')  # Need to run only once to download and load model into memory
    
    # Extract text
    result = ocr.ocr(img_path, cls=True)

    # Combine the extracted text into a single string
    extracted_text = [line[1][0].lower() for line in result[0]]
    return extracted_text




def find_closest_word(word, word_list):
    closest_matches = difflib.get_close_matches(word, word_list, n=1, cutoff=0.6)
    if closest_matches:
        return closest_matches[0]
    else:
        return False

def imageFunction(url, items):

    text = extract_text_from_image("static/uploads/"+url)
    print("\n\n\n",text)

    itemsToReturn = []

    for item in text:

        item = re.sub(r'[^a-zA-Z0-9]', ' ', item)
        
        word = find_closest_word(item, items)
        if word!=False:
            itemsToReturn.append(word)
        else:
            itemsToReturn.append(item)

    

    return itemsToReturn

def split_words(word_list):
    processed_list = []
    for item in word_list:
        # Use regex to check for a lowercase letter followed by an uppercase letter
        match = re.search(r'([a-z])([A-Z])', item)
        if match:
            # Split the item at the match position
            index = match.start(1) + 1
            processed_list.append(item[:index])
            processed_list.append('')
            processed_list.append(item[index:])
        else:
            processed_list.append(item)
    return processed_list

def cleanString(input_string):

    cleaned_string = re.sub(r'<.*?>', '', input_string)

    # Split the string by sections and items
    sections = re.split(r'\s*(\d+\.\s)', cleaned_string)

    # Recombine sections and items into a list
    result = []
    current_section = ""
    for part in sections:
        if not part.strip():
            continue
        if re.match(r'\d+\.\s', part):
            if current_section:
                result.append(current_section.strip())
                result.append("")  # Add a blank item after the category name
            current_section = part
        else:
            current_section += part

    if current_section:
        result.append(current_section.strip())

    result = split_words(result)

    return result

RE_D = re.compile('\d')

def has_digits(string):
    res = RE_D.search(string)
    return res is not None

def copyText(string):
    string = cleanString(string)
    for i in range(len(string)):
        if string[i] == "":
            string[i] = "\n"
        if not (has_digits(string[i])) and string[i]!="\n":
            string[i] = "\n"+string[i].lstrip()

    return " ".join(string)







# Function to load image from local path
def load_image(image_path):
    image = cv2.imread(image_path)
    return image

# Function to preprocess the image to improve OCR results
def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 3)
    return gray

# Function to get text and coordinates from image using PaddleOCR
def get_text_coordinates(image_path):
    ocr = PaddleOCR(use_angle_cls=True, lang='en')
    result = ocr.ocr(image_path, cls=True)

    text_coordinates = {}
    for line in result:
        for word_info in line:
            word = word_info[1][0]
            bbox = word_info[0]
            mid_x = (bbox[0][0] + bbox[2][0]) // 2
            mid_y = (bbox[0][1] + bbox[2][1]) // 2
            text_coordinates[word] = (int(mid_x), int(mid_y))

    return text_coordinates

# Main function
def sendCoords(image_path):
    image = load_image(image_path)
    preprocessed_image = preprocess_image(image)
    
    # Save the preprocessed image temporarily
    preprocessed_image_path = 'preprocessed_image.png'
    cv2.imwrite(preprocessed_image_path, preprocessed_image)
    
    # Get coordinates for text using PaddleOCR
    text_coordinates = get_text_coordinates(preprocessed_image_path)
    
    return text_coordinates

def enhance_description(item):
    return f"The item '{item}' is found in stores."

def categorizeItems_Initially(categories, items):

    # Initialize a text classification pipeline with a pre-trained model
    classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')

    # Predict categories for new items
    sorted_items = {category: [] for category in categories}

    for item in items:
        # Enhance context of each item
        text = enhance_description(item)
        result = classifier(text, categories)
        
        # Get the most likely category
        category = result['labels'][0]
        
        sorted_items[category].append(item)

    return sorted_items
from flask import Flask, render_template, request, jsonify, redirect, url_for, send_from_directory, flash
from optimized_path import get_optimized_path
from draw_path import draw
import os
import json
from store_layout import find_store, find_storeItemDirectory
from werkzeug.utils import secure_filename
from imagefunctions import imageFunction, cleanString, copyText, sendCoords, categorizeItems_Initially
from PIL import Image

app = Flask(__name__)
app.secret_key = 'your_secret_key'

global notFounds
global address
global name


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


#Client Side

@app.route('/grocery_list_alt', methods=['GET', 'POST'])
def grocery_list_alt():
    global address
    global name

    data = request.args.get('data', '')
    data = json.loads(data)

    items = find_storeItemDirectory(address).keys()

    return render_template('grocery_list.html', name=name, 
                           address=address.replace(" ","").replace(",",""),
                           address_yes_space = address,
                           items=items, itemstoadd=data)


@app.route('/grocery_list', methods=['GET', 'POST'])
def grocery_list():
    global address
    global name

    name, address = request.args.get('name', '').split(";")
    name.strip();
    address = address.strip();
    items = find_storeItemDirectory(address).keys()

    if (address[0]==" "):
        address = address[1:]

    return render_template('grocery_list.html', name=name, 
                           address=address.replace(" ","").replace(",",""),
                           address_yes_space = address,
                           items=items, itemstoadd=[])

global label

@app.route('/submit_items', methods=['POST'])
def submit_items():
    global label
    items = request.json.get('items', [])
    global notFounds


    _ = categorize_items(items)

    copy = copyText(label)
    
    return jsonify(success=True, text=label, copy=copy, notFounds=json.dumps(notFounds), image_url=url_for('static', filename='newimage.png'))

def categorize_items(items):
    
    global notFounds
    global address

    notFounds = []
    category_mapping = find_storeItemDirectory(address)

  
    print("KKKKKK", category_mapping)

    categorized_items = {}
    for item in items:

        item_name = item['item'].lower()
        category = category_mapping.get(item_name, 'Miscellaneous')
        
        if category=="Miscellaneous":
            notFounds.append(item)
        else:
            if category not in categorized_items:
                categorized_items[category] = []

            categorized_items[category].append(item)

   
    path, distance = get_optimized_path(categorized_items,address)


    global label
    label = ""
    for cat in path:
        if cat!="Entrance" and cat!="Checkout":
            label+="<u/>"+cat+"</u/>"+"<br/><br/>"
            lst = categorized_items[cat]
            c=0
            for i in lst:
                c+=1
                label+= str(c)+". "+ i['item']+"<br/>"
            
            label+="<br/>" #local label
    

    image_path = "static/stores/"+address.replace(" ","").replace(",","")+".png" #reuse

    new_path = "static/newimage.png"

    draw(path, image_path, new_path, address)
    return label[:-5]


UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'heic'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/u', methods=['POST'])
def upload_image():
    global address
    global notFounds
    global label

    if 'file' not in request.files:
        print('nope')
        return jsonify(success=False)
    
    file = request.files['file']

    if file.filename == '':
        print('nope2')
        return jsonify(success=False)
    
    if file:
        
        print("\n\n\n\n\n\nhere")

        filename = "imagefortext.png"
        file_path = "static/uploads/" + filename

        file.save(file_path)


        if os.path.isfile(file_path):

            items = find_storeItemDirectory(address).keys()

            result = imageFunction(filename, items)
        
            itemsToReturn = [{'item': i} for i in result]

            _ = categorize_items(itemsToReturn)

            copy = copyText(label)

            label = cleanString(label)

            nf = ", ".join([i['item'] for i in notFounds])
        
    
    return render_template('grocery_list_image.html',
                           notFounds=nf,
                           label=label, items=itemsToReturn, items2=items, copy=copy)
 
@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


#Server Side

global data_dict
global threeInfoStack

@app.route('/updatecats')
def updatecats():
    global data_dict
    return render_template('updatecats.html', data=data_dict)

@app.route('/add', methods=['POST'])
def addcat():
    global data_dict
    new_key = request.form.get('new_key')
    new_value = request.form.get('new_value')
    if new_key and new_value:
        data_dict[new_key] = new_value
    return redirect(url_for('updatecats'))


@app.route('/createastore')
def createastore():
    return render_template('store_creation.html')

@app.route('/submit-store', methods=['POST'])
def submit_store():
    global data_dict
    global threeInfoStack

    store_name = request.form['store_name']
    store_address = request.form['store_address']
    file = request.files['store_image']

    file_path = "static/stores/" + store_address.replace(" ","").replace(",","")+".png" #reuse

    threeInfoStack = [store_name, store_address, file_path]


    file.save(file_path)


    if file:
        print("here")
        data_dict = sendCoords(file_path)
        
        return render_template('updatecats.html', data=data_dict)
    else:
        return "Not yet"

def updateAll(items_dict, data_dict):
    global threeInfoStack
    
    store_name, store_address, file_path = threeInfoStack

    with open('jsonfiles/supermarkets.json', 'r') as file:
        data = json.load(file)
    new_entry = { "name": store_name.lower().title(), "location": store_address}
    data.append(new_entry)
    with open('jsonfiles/supermarkets.json', 'w') as file:
        json.dump(data, file, indent=4)

    with open('jsonfiles/storeItemDirectory.json', 'r') as file:
        data = json.load(file)
    
    temp_dict = {}

    for i in items_dict:
        lst = items_dict[i]
        for k in lst:
            temp_dict[k.lower()] = i

    data[store_address] = temp_dict
    with open('jsonfiles/storeItemDirectory.json', 'w') as file:
        json.dump(data, file, indent=4)

    with open('jsonfiles/store_layout.json', 'r') as file:
        data = json.load(file)
    data[store_address] = data_dict
    with open('jsonfiles/store_layout.json', 'w') as file:
        json.dump(data, file, indent=4)

    print("******* ALL UPDATED *******")



@app.route('/update', methods=['POST'])
def update():
    global data_dict
    updated_data = request.form.to_dict()
    new_data_dict = {}

    items_dict = {}


    for key, value in data_dict.items():
        new_key = updated_data.get(f'key_{key}', key)
        if not updated_data.get(f'delete_{key}'):
            new_data_dict[new_key] = value

            items = updated_data.get(f'items_{key}', '')
            items_list = [item.strip() for item in items.split(',') if item.strip()]
            items_dict[new_key] = items_list

    data_dict = new_data_dict
    keys = list(data_dict.keys())

    items = request.form['text_input'].split(",")

    if len(items)>1:
        items_dict = categorizeItems_Initially(keys, items) #reassign
    else:
        print("Manual chosen", items_dict)

    updateAll(items_dict, data_dict)



    return "All Done"

if __name__ == "__main__":
    app.run(debug=True) 
import json


stores = {
    "6067 N Ridge Rd, Madison, OH":
    {
    'Entrance': (800,600),
    'Checkout': (600, 480),
    'Auto': (250, 160),
    'Sporting Goods': (375, 160),
    'Toys': (400, 160),
    'Electronics': (550, 160),
    'Household Paper': (650, 160),
    'Cleaning': (700, 160),
    'Pets': (750, 160),
    'Snacks': (800, 160),
    'Dairy': (950, 100),
    'Adult Beverages': (950, 120),
    'Deli': (1050, 160),
    'Meat': (1010, 260),
    'Grocery': (925, 260),
    'Frozen': (925, 360),
    'Bakery': (1050, 400),
    'Fresh Produce': (925, 440),
    'Boys': (525, 260),
    'Girls': (615, 260),
    'Baby': (950, 260),
    'Shoes': (550, 340),
    'Mens': (550, 400),
    'Ladies': (650, 420),
    'Jewelry': (825, 340),
    'Intimates': (750, 360),  # Combined Sleepwear & Panties
    'Home Office': (450, 260),
    'Crafts': (450, 300),
    'Celebrate': (450, 360),
    'Cosmetics': (450, 410),
    'Home Decor': (325, 240),  # Combined Home
    'Furniture': (325, 280),
    'Bedding': (325, 290),
    'Bath': (325, 340),
    'Storage & Laundry': (325,370),
    'Kitchen': (325, 360),  # Combined Kitchen & Dining
    'Health & Wellness': (250, 500),
    'Seasonal': (225, 400),
    'Garden': (150, 440),
    'Paint': (225, 260),
    'Hardware': (225, 300),
    'Clearance': (225, 330),
    'Pharmacy': (250, 500),
    'Travel':  (375, 160),
},
    "1750 Story Rd, San Jose, CA": 
    {
    'Entrance': (185,811),
    'Checkout': (305,691),
    'Auto': (200,320),  # Using coordinates from Hardware
    'Sporting Goods': (200,320),
    'Toys': (677,127),
    'Electronics': (550, 160),
    'Household Paper': (1040,700),
    'Cleaning': (1028,346),  # Using coordinates from Grocery
    'Pets': (895,241),
    'Snacks': (800, 160),
    'Dairy': (1028,346),  # Using coordinates from Grocery
    'Adult Beverages': (1031,422),
    'Deli': (1020,624),
    'Meat': (1028,346),  # Using coordinates from Grocery
    'Grocery': (1028,346),
    'Frozen': (1028,346),  # Using coordinates from Grocery
    'Bakery': (1028,346),  # Using coordinates from Grocery
    'Fresh Produce': (1028,346),  # Using coordinates from Grocery
    'Boys': (400,460),
    'Girls': (375,560),
    'Baby': (341,255),
    'Shoes': (290,123),  # Using coordinates from Mens
    'Mens': (290,123),
    'Ladies': (86,477),  
    'Jewelry': (86,477),   # Using coordinates from Ladies
    'Intimates': (98,250),
    'Home Office': (817,346),  # Using coordinates from Home Decor
    'Crafts': (817,346),  # Using coordinates from Home Decor
    'Celebrate': (817,346),  # Using coordinates from Home Decor
    'Cosmetics': (817,346),  # Using coordinates from Home Decor
    'Home Decor': (817,346),
    'Furniture': (817,346),  # Using coordinates from Home Decor
    'Bedding': (817,346),  # Using coordinates from Home Decor
    'Bath': (395,350),
    'Storage & Laundry': (817,346),  # Using coordinates from Home Decor
    'Kitchen': (840,560),
    'Health & Wellness': (685,677),
    'Seasonal': (225, 400),
    'Garden': (225,400),  # Using coordinates from Seasonal
    'Paint': (200,320),  # Using coordinates from Sporting Goods
    'Hardware': (200,320),  # Using coordinates from Sporting Goods
    'Clearance': (200,320),  # Using coordinates from Sporting Goods
    'Pharmacy': (660,770),
    'Travel': (800,461),
},

'777 Story Road, San Jose, CA': {
   'Hardware': (92, 52),
    'Electronics': (233, 51),
    'Shoes': (312, 52),
    'Pets': (383, 51),
    'Chemicals': (489, 50),
    'Grocery': (673, 51),
    'Action Alley': (361, 69),
    'Automotive': (129, 128),
    'Stationery': (239, 127),
    'Infants': (488, 128),
    'Sports': (132, 171),
    'Crafts': (247, 171),
    'Appliance': (409, 169),
    'Girl Cloth': (493, 170),
    'Boy Cloth': (572, 168),
    'Beauty': (674, 225),
    'Grocery': (778, 218),
    'Toys': (133, 244),
    'Men Cloth': (494, 230),
    'Lady Cloth': (573, 230),
    'Furniture': (400, 244),
    'Bed/Bath': (503, 282),
    'Hallmark': (236, 301),
    'Cosmetics': (677, 302),
    'Seasonal': (135, 360),
    'Action Alley': (413, 381),
    'Registers': (412, 422),
    'Service Desk': (250, 471),
    'Photo Dept': (331, 471),
    'Vision Center': (497, 471),
    'Checkout': (408,406),
    'Entrance': (766, 491),
},

'2850 Quimby Rd, San Jose, CA':  {
    'Frozen': (203, 30), 
    'Dairy': (30, 534),
    'Fresh Produce': (608, 30), 
    'Sweets': (954, 184), 
    'Tea Essentials': (503, 153), 
    'Spice & Mixes': (547, 216), 
    'Pantry Staples': (508, 341), 
    'Snacks': (511, 534), 
    'Lentils & Flour': (554, 730), 
    'Condiments & Preserves': (589, 792), 
    'Rice': (541, 925),
    "Checkout": (1150, 386),
    "Entrance": (1165,93),
    "Delights": (1150, 230),
},


"3155 Silver Creek Rd, San Jose, CA": {
    "Household Paper": (69, 111),
    "Seasonal": (222, 111),
    "Household": (86, 286),
    "Pets": (383, 288),
    "Sporting Goods": (554, 291),
    "Tech": (855, 304),
    "Travel": (677, 315),
    "Home Improvement": (1063, 306),
    "Kitchen": (1272, 344),
    "Kids Room Bedding": (900, 411),
    "Bath": (1171, 411),
    "Snacks": (87, 430),
    "Toys Games": (673, 457),
    "Baby": (346, 475),
    "Fitting Rooms": (700, 824),
    "Infant Toddler": (331, 600),
    "Boys": (706, 602),
    "Mens": (1128, 593),
    "Maternity": (835, 616),
    "Grocery": (101, 642),
    "Furniture": (1284, 705),
    "Shoes": (1067, 738),
    "School Office": (227, 751),
    "Hosiery": (1149, 748),
    "Girls": (687, 754),
    "Activewear": (971, 774),
    "Intimates": (403, 799),
    "Kids": (561, 791),
    "Fitting Room": (1077, 826),
    "Home Decor": (1281, 835),
    "Womens": (1096, 857),
    "Accessories": (703, 887),
    "Meat Seafood": (111, 918),
    "Bakery": (139, 1022),
    "Deli": (83, 1029),
    "Personal Care": (388, 1041),
    "Health Beauty": (569, 1039),
    "Beauty": (782, 1055),
    "Guest Service": (1309, 1118),
    "Wine And Spirits": (102, 1160),
    "Optical": (489, 1173),
    "Pharmacy": (626, 1172),
    "Cafe": (986, 1165),
    "Starbucks": (1090, 1181),
    "Entrance": (220, 1199),
    "Checkout": (1038, 1052),
}

}

def find_store(address):
    print("new find store function")
    with open('jsonfiles/store_layout.json', 'r') as file:
        stores = json.load(file)
    
    return stores.get(address, "Store address not found")

def find_storeItemDirectory(address):
    print("HERE AT THE STORE DIRECTORY")
    with open('jsonfiles/storeItemDirectory.json', 'r') as file:
        storeItemDirectory = json.load(file)
    
    return storeItemDirectory.get(address, "Store address not found")

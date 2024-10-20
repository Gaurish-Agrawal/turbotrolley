document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('add-item').addEventListener('click', addItem);
    document.getElementById('submit-items').addEventListener('click', submitItems);
});

function addItem() {

    const itemInput = document.getElementById('item-input');

    const item = itemInput.value.trim();


    if (item) {
        const table = document.getElementById('grocery-table').getElementsByTagName('tbody')[0];
        const row = table.insertRow();
        const cell1 = row.insertCell(0);
        
        const cell3 = row.insertCell(1); //2->1

        cell1.textContent = item;
        
        cell3.innerHTML =
        `<button onclick="deleteRow(this)" style="border: none; background-color: white;">
        <span style="font-size: 20px; color: darkgreen;font-weight: bold;">&#10005;</span>
        </button>`;

        itemInput.value = '';
        
    } else {
        alert('Please enter an item.');
    }
}

function deleteRow(button) {
    const row = button.parentElement.parentElement;
    row.parentElement.removeChild(row);
}

function submitItems() {

    const table = document.getElementById('grocery-table').getElementsByTagName('tbody')[0];
    const rows = table.getElementsByTagName('tr');
    const items = [];

    for (let i = 0; i < rows.length; i++) {
        const item = rows[i].cells[0].textContent;
        items.push({ item }); //q
    }

    fetch('/submit_items', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ items }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Items submitted:', data); // Debugging: Log the server response
    })
    .catch((error) => {
        console.error('Error:', error); // Debugging: Log any errors
    });
}



function updateImage() {
    fetch('/submit_items', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({})
        })
            .then(response => response.json()
        )
            .then(data => {
                reloadImage(data.image_url, data.notFounds, data.text, data.copy);
        })
            .catch(error => console.error('Error:', error));
}


function reloadImageForImage() {
    const img = document.getElementById('store-diagram');
    img.src = 'static/newimage.png';

    const q = document.getElementById('item-order-label_image');
    q.innerHTML = "<h3>${q.innerHTML}</h3>"
}


function reloadImage(imageUrl, notFounds,text, copy) {

    var c = "";
    notFounds = JSON.parse(notFounds);

    for (let i = 0; i < notFounds.length; i++) {
        c += notFounds[i].item + ", ";
    }

    const p = document.getElementById('notFounds');
    const q = document.getElementById('item-order-label');
    const ca = document.getElementById('item-order-label-copy');
    
    if (c){
        p.innerHTML = "Not at this store: "+c.substring(0, c.length - 2);
    }

    q.innerHTML = text;
    ca.innerHTML = copy;

    const img = document.getElementById('store-diagram');
    img.src = imageUrl + '?' + new Date().getTime();
}
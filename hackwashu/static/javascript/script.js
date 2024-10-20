//var supermarkets = [];

var c = 0;


const supermarkets = [
    { name: "Target", location: "1750 Story Rd, San Jose, CA" },
    { name: "Target", location: "3155 Silver Creek Rd, San Jose, CA" },
    { name: "Walmart", location: "6067 N Ridge Rd, Madison, OH" },
    { name: "Walmart", location: "777 Story Road, San Jose, CA" },
    { name: "New India Bazaar", location: "2850 Quimby Rd, San Jose, CA"},
    { name: "Paws And Go", location: "101 South 40, Saint Louis, MO"},
];

function filterResults() {
    
    /*
    c++;


    if (c == 1) {  // Ensure strict equality check
        fetch('jsonfiles/supermarkets.json')
            .then(response => {
                if (!response.ok) {  // Check if the response is OK
                    throw new Error('Network response was not ok');
                }
                return response.json();  // Parse the response as JSON
            })
            .then(data => {
                alert("Data found!");  // Notify that data is found
                supermarkets = data;  // Assign the data to the supermarkets variable
            })
            .catch(error => {
                alert('Error fetching the data:', error);  // Log any errors
            });
    }
    */
    

    const input = document.getElementById('search-bar');
    const filter = input.value.toUpperCase();
    const resultsList = document.getElementById("results-list");
    resultsList.innerHTML = ''; // Clear previous results

    if (filter.length === 0) {
        resultsList.style.display = "none";
        return;
    }

    resultsList.style.display = "block";

    supermarkets.forEach(supermarket => {
        if (supermarket.name.toUpperCase().indexOf(filter) > -1) {
            const div = document.createElement('div');
            div.className = 'result-item';
            div.innerHTML = `
                <div class="result-title">${supermarket.name}</div>
                <div class="result-details">${supermarket.location}</div>
            `;
            div.addEventListener('click', () => {
                window.location.href = `/grocery_list?name=${encodeURIComponent(supermarket.name)}+;+${encodeURIComponent(supermarket.location)}`;
            });
            resultsList.appendChild(div);
        }
    });
}
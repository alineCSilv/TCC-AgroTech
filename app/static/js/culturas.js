// Function to handle form submission
document.querySelector('form').addEventListener('submit', function (event) {
    event.preventDefault();

    var cultura = {
        nome: document.getElementById('nome').value,
        phSolo: document.getElementById('phSolo').value,
        p: document.getElementById('p').value,
        k: document.getElementById('k').value,
        mg: document.getElementById('mg').value,
        ca: document.getElementById('ca').value,
        h_al: document.getElementById('h_al').value,
        sb: document.getElementById('sb').value,
        ctc: document.getElementById('ctc').value,
        v: document.getElementById('v').value,
        m: document.getElementById('m').value,
        al: document.getElementById('al').value,
        mo: document.getElementById('mo').value
    };

    // Here you can send the 'cultura' object to the server
    // For example, using fetch API to make a POST request
    // fetch('/api/cultura', { method: 'POST', body: JSON.stringify(cultura) });
});

// Function to fill the form with test data
function preencherComDadosDeTeste() {
    document.getElementById('nome').value = 'Teste';
    document.getElementById('phSolo').value = (Math.random() * (7.5 - 5.0) + 5.0).toFixed(2);
    document.getElementById('p').value = (Math.random() * (30 - 10) + 10).toFixed(2);
    document.getElementById('k').value = (Math.random() * (50 - 20) + 20).toFixed(2);
    document.getElementById('mg').value = (Math.random() * (5.0 - 1.0) + 1.0).toFixed(2);
    document.getElementById('ca').value = (Math.random() * (10.0 - 2.0) + 2.0).toFixed(2);
    document.getElementById('h_al').value = (Math.random() * (3.0 - 1.0) + 1.0).toFixed(2);
    document.getElementById('sb').value = (Math.random() * (8.0 - 3.0) + 3.0).toFixed(2);
    document.getElementById('ctc').value = (Math.random() * (10.0 - 5.0) + 5.0).toFixed(2);
    document.getElementById('v').value = (Math.random() * (80 - 50) + 50).toFixed(2);
    document.getElementById('m').value = (Math.random() * (20 - 5) + 5).toFixed(2);
    document.getElementById('al').value = (Math.random() * (5.0 - 1.0) + 1.0).toFixed(2);
    document.getElementById('mo').value = (Math.random() * (5.0 - 1.0) + 1.0).toFixed(2);
}

// Call the function to fill the form with test data
preencherComDadosDeTeste();
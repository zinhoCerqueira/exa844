// Chamar a função assim que o DOM for carregado
document.addEventListener('DOMContentLoaded', addElementsInSelect);
document.addEventListener('DOMContentLoaded', time_Spinner);

function time_Spinner() {
    var spinner = document.getElementById('spinner');
    setTimeout(function () {
        spinner.style.display = 'none';
    }, 3000);
}

async function addElementsInSelect() {
    // Lógica da função
    const apiUrl = 'https://api-bus.onrender.com/origens';
    fazerRequisicaoAPI(apiUrl)
        .then(data => {
            // Manipular os dados da API
            // console.log(data);

            const select = document.getElementById('my_id');

            for (const key in data) {
                const option = document.createElement('option');
                option.value = data[key];
                option.text = data[key];
                select.appendChild(option);
            }
        });
}

async function fazerRequisicaoAPI(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error('Erro na requisição API');
        }
        const data = await response.json();
        console.log(data);
        return data;
    } catch (error) {
        console.error(error);
    }
}

function searchCity() {
    const data = { origem: document.getElementById("my_id").value };
    const url = 'https://api-bus.onrender.com/destino_origens';
    console.log(document.getElementById("my_id").value);
    time_Spinner();
    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    };

    fetch(url, options)
    .then(response => response.json())
    .then(data => {
      // Processar a resposta JSON retornada pela API
      console.log(data);
    })
    .catch(error => {
      // Lidar com erros de requisição
      console.error('Erro:', error);
    });



}
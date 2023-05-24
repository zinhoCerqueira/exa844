// Chamar a função assim que o DOM for carregado
document.addEventListener('DOMContentLoaded', addElementsInSelect);
document.addEventListener('DOMContentLoaded', time_Spinner);

function time_Spinner() {
    var spinner = document.getElementById('spinner');
    setTimeout(function () {
        spinner.style.display = 'none';
    }, 000);
}

async function addElementsInSelect() {
    // Lógica da função
    const apiUrl = 'https://api-bus.onrender.com/origens';
    fazerRequisicaoAPI(apiUrl)
        .then(data => {
            // Manipular os dados da API

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

            console.log(data);

            const select = document.getElementById('id_destino');

            for (const key in data) {
                const option = document.createElement('option');
                option.value = data[key];
                option.text = data[key];
                select.appendChild(option);
            }
        })
        .catch(error => {
            // Lidar com erros de requisição
            console.error('Erro:', error);
        });


    const botao1 = document.getElementById('botao-1');
    botao1.classList.add('bg-gradient-to-r');
    botao1.classList.add('from-tertiary');
    botao1.classList.add('to-quaternary');
    botao1.disabled = false;

    const border_select = document.getElementById('id_destino');
    border_select.classList.add('border-tertiary');
    border_select.classList.add('border-gradient-to-r');
    border_select.disabled = false;

}

function searchRota() {
    const data = {
        local_saida: document.getElementById("my_id").value,
        local_chegada: document.getElementById("id_destino").value
    };

    time_Spinner();

    var dadosJSON = JSON.stringify(data);
    sessionStorage.setItem('local_data', dadosJSON);
    window.location.href = 'rotas.html';

}

function rotaImg1() {

    document.getElementById("my_id").value = "Feira De Santana, BA";
    document.getElementById("id_destino").value = "Salvador, BA";

    const data = {
        local_saida: "Feira De Santana, BA",
        local_chegada: "Salvador, BA"
    };


    time_Spinner();

    var dadosJSON = JSON.stringify(data);
    sessionStorage.setItem('local_data', dadosJSON);
    window.location.href = 'rotas.html';

}

function rotaImg1() {
    const data = {
        local_saida: "Feira De Santana, BA",
        local_chegada: "Salvador, BA"
    };


    time_Spinner();

    var dadosJSON = JSON.stringify(data);
    sessionStorage.setItem('local_data', dadosJSON);
    window.location.href = 'rotas.html';

}

function rotaImg2() {

    const data = {
        local_saida: "Salvador, BA",
        local_chegada: "Lencois, BA"
    };


    time_Spinner();

    var dadosJSON = JSON.stringify(data);
    sessionStorage.setItem('local_data', dadosJSON);
    window.location.href = 'rotas.html';

}

function rotaImg3() {

    document.getElementById("my_id").value = "Feira De Santana, BA";
    document.getElementById("id_destino").value = "Salvador, BA";

    const data = {
        local_saida: "Euclides Da Cunha, BA",
        local_chegada: "Juazeiro, BA"
    };


    time_Spinner();

    var dadosJSON = JSON.stringify(data);
    sessionStorage.setItem('local_data', dadosJSON);
    window.location.href = 'rotas.html';

}


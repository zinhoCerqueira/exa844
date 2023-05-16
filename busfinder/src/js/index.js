

async function minhaFuncao() {
    // Lógica da função
    const apiUrl = 'https://api-bus.onrender.com/origens';
    fazerRequisicaoAPI(apiUrl)
        .then(data => {
            // Manipular os dados da API
            // console.log(data);
            console.log("oi");
            
            const select = document.getElementById('my_id');

            for (const key in data) {
                const option = document.createElement('option');
                option.value = key;
                option.text = data[key];
                select.appendChild(option);
            }
        });
}

// Chamar a função assim que o DOM for carregado
document.addEventListener('DOMContentLoaded', minhaFuncao);

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

function myFunction() {
    console.log(document.getElementById("my_id").value);
}
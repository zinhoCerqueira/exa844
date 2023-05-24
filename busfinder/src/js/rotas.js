document.addEventListener('DOMContentLoaded', search_rotas());

function search_rotas() {
    var dadosJSON = sessionStorage.getItem('local_data');
    var dados = JSON.parse(dadosJSON);

    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(dados),
    };

    const url = 'https://api-bus.onrender.com/rotacompleta_origemdestino';

    fetch(url, options)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            for (const key in data) {

                console.log(data[key]['chegada']);

                // Criação do elemento <div> com as classes "mt-4" e "flex"
                var divElement = document.createElement("div");
                divElement.classList.add("m-4", "bg-cover", "overflow-hidden",
                    "border", "rounded-md", "shadow-lx");

                // Criação do primeiro <div> interno
                var div1 = document.createElement("div");
                div1.classList.add("w-2/3", "m-4", "border-r", "border-gray-300");

                // Criação dos parágrafos e dos elementos <span> dentro do primeiro <div>
                var p1 = document.createElement("p");
                var span1 = document.createElement("span");
                span1.classList.add("font-bold");
                span1.textContent = "Origem: ";
                p1.appendChild(span1);
                p1.innerHTML += "<span id='origem'>" + data[key]['origem'] + "</span>";

                var p2 = document.createElement("p");
                var span2 = document.createElement("span");
                span2.classList.add("font-bold");
                span2.textContent = "Destino: ";
                p2.appendChild(span2);
                p2.innerHTML += "<span id='destino'>" + data[key]['destino'] + "</span>";

                var p3 = document.createElement("p");
                var span3 = document.createElement("span");
                span3.classList.add("font-bold");
                span3.textContent = "Empresa: ";
                p3.appendChild(span3);
                p3.innerHTML += "<span id='empresa'>" + data[key]['empresa'] + "</span>";

                var p4 = document.createElement("p");
                var span4 = document.createElement("span");
                span4.classList.add("font-bold");
                span4.textContent = "Tipo: ";
                p4.appendChild(span4);
                p4.innerHTML += "<span id='tipo'>" + data[key]['tipo'] + "</span>";

                div1.appendChild(p1);
                div1.appendChild(p2);
                div1.appendChild(p3);
                div1.appendChild(p4);

                // Criação do segundo <div> interno
                var div2 = document.createElement("div");
                div2.classList.add("w-1/3", "m-4");

                // Criação dos parágrafos e dos elementos <span> dentro do segundo <div>
                var p5 = document.createElement("p");
                var span5 = document.createElement("span");
                span5.classList.add("font-bold");
                span5.textContent = "Saída: ";
                p5.appendChild(span5);
                p5.innerHTML += "<span id='saida'>" + data[key]['saida'] + "</span>";

                var p6 = document.createElement("p");
                var span6 = document.createElement("span");
                span6.classList.add("font-bold");
                span6.textContent = "Chegada: ";
                p6.appendChild(span6);
                p6.innerHTML += "<span id='chegada'>" + data[key]['chegada'] + "</span>";

                var p7 = document.createElement("p");
                var span7 = document.createElement("span");
                span7.classList.add("font-bold");
                span7.textContent = "Duração: ";
                p7.appendChild(span7);
                p7.innerHTML += "<span id='tempo_de_viagem'>" + data[key]['tempo_de_viagem'] + "</span>";

                var p8 = document.createElement("p");
                var span8 = document.createElement("span");
                span8.classList.add("font-bold");
                span8.textContent = "Preço: ";
                p8.appendChild(span8);
                p8.innerHTML += "<span id='preco'>" + data[key]['preco'] + " R$" + "</span>";

                div2.appendChild(p5);
                div2.appendChild(p6);
                div2.appendChild(p7);
                div2.appendChild(p8);

                var divInfo = document.createElement("div");
                divInfo.classList.add("flex");

                divInfo.appendChild(div1);
                divInfo.appendChild(div2);

                // Adiciona os dois <div> internos ao elemento principal <div>
                divElement.appendChild(divInfo);

                //Botão
                var divButton = document.createElement("div");
                var button = document.createElement("button");
                button.classList.add("w-full", "block", "text-secondary", "px-4", "py-2",
                    "bg-gradient-to-r", "from-tertiary", "to-quaternary"
                );
                button.textContent = "Selecione";
                divButton.appendChild(button);
                divElement.appendChild(divButton);

                // Insere o elemento principal <div> no documento HTML
                var ambiente = document.getElementById('ambiente');
                ambiente.appendChild(divElement);
            }
        })
        .catch(error => {
            // Lidar com erros de requisição
            console.error('Erro:', error);
        });

}

function rotaImg(){
    window.location.href = 'index.html';
}
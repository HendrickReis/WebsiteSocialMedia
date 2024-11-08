document.addEventListener('DOMContentLoaded', function() {
    // Seleciona o botão e a div
    const botaoAdicionar = document.getElementById('enviar');
    const conteudoDiv = document.getElementById('mensagens');

    // Função para adicionar a tag quando o botão for clicado
    botaoAdicionar.addEventListener('click', function() {
        // Faz a requisição GET para o servidor Flask usando fetch
        fetch('/adicionar_mensagem')
            .then(response => response.json())  // Espera a resposta no formato JSON
            .then(data => {
                // Adiciona a nova tag HTML dentro da div #conteudo
                conteudoDiv.innerHTML += data.tag;
            })
            .catch(error => {
                console.error('Erro ao adicionar a tag:', error);
            });
    });
});

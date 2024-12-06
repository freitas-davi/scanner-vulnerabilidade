document.addEventListener("DOMContentLoaded", function(){
    const resultadoDiv = document.getElementById("resultado");

    if (resultadoDiv && resultadoDiv.innerHTML.trim() !== ""){
        resultadoDiv.style.display = "block";
    }
});

// MODAL
document.addEventListener("DOMContentLoaded", function(){
    const modal = document.getElementById("myModal");
    const openModalButton = document.getElementById("open-modal");
    const closeModalButton = document.querySelector(".close");

    // Abrir o modal
    openModalButton.addEventListener("click", function(){
        modal.style.display = "flex"; //Exibe o modal
    });

    // Fecha o modal ao clicar no btn fechar
    closeModalButton.addEventListener("click", function(){
        modal.style.display = "none"; //Oculta model
    });

     // Fecha a modal ao clicar fora do conteúdo
     window.addEventListener("click", function(event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
});

// Editar portas
function editarPorta(id, numero, descricao) {
    // Preenche os inputs com os valores da porta selecionada
    document.getElementById('porta-id').value = id;
    document.getElementById('numero-porta').value = numero;
    document.getElementById('descricao').value = descricao;

    // Altere o texto do botão para indicar que é uma edição
    const botaoSalvar = document.querySelector('.btn-addport');
    botaoSalvar.textContent = 'Editar';
}

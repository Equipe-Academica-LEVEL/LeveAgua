document.addEventListener("DOMContentLoaded", function(){
    // Obtém todos os elementos de navegação
    const navItems = document.querySelectorAll('.nav-item');

    // Obtém as seções de navegação
    const sectionUsuario = document.querySelector('.section-usuario');
    const sectionEndereco = document.querySelector('.section-endereco');
    const sectionConfiguracoes = document.querySelector('.section-configuracoes');

    // Função para lidar com a seleção de navegação
    function handleNavClick(selectedItem) {
        // Remove a classe 'is-selected' de todos os itens
        navItems.forEach(function(nav) {
            nav.classList.remove('is-selected');
        });

        // Adiciona a classe 'is-selected' ao item clicado
        selectedItem.classList.add('is-selected');

        // Oculta todas as seções de navegação
        sectionUsuario.classList.add('is_desactive');
        sectionEndereco.classList.add('is_desactive');
        sectionConfiguracoes.classList.add('is_desactive');

        // Mostra a seção correspondente ao item clicado
        if (selectedItem.id === 'usuario') {
            sectionUsuario.classList.remove('is_desactive');
        } else if (selectedItem.id === 'endereco') {
            sectionEndereco.classList.remove('is_desactive');
        } else if (selectedItem.id === 'configuracoes') {
            sectionConfiguracoes.classList.remove('is_desactive');
        }
    }

    // Adiciona o evento de clique a cada item de navegação
    navItems.forEach(function(item) {
        item.addEventListener('click', function() {
            handleNavClick(this);
        });
    });

    // -------------------------------------------------------------------------------------------
    // SEÇÃO DE USUÁRIOS

    // Obtém as seções específicas de usuário
    const sectionDadosUsuario = document.querySelector('.mostra-de-dados_content');
    const sectionEditarUsuario = document.querySelector('.atualizar_usuario_content');
    const sectionExcluirUsuario = document.querySelector('.excluir_usuario_content');

    // Seleciona os botões
    const btnExcluirConta = document.querySelector('.excluir-usuario'); // Botão "Excluir Conta"
    const btnEditarUsuario = document.querySelector('.atualizar-informacoes'); // Botão "Atualizar Informações"
    const btnVoltarUsuario = document.querySelectorAll('.voltar-usuario'); // Botões "Voltar"

    // Função para esconder apenas as seções relacionadas a Usuarios
    function esconderSecoesUsuario() {
        sectionDadosUsuario.classList.add('is_desactive');
        sectionEditarUsuario.classList.add('is_desactive');
        sectionExcluirUsuario.classList.add('is_desactive');
    }

    function mostrarDadosUsuario(){
        esconderSecoesUsuario();
        sectionDadosUsuario.classList.remove('is_desactive');
    }

    function mostrarEditarUsuario(){
        esconderSecoesUsuario();
        sectionEditarUsuario.classList.remove('is_desactive');
    }

    function mostrarExcluirUsuario(){
        esconderSecoesUsuario();
        sectionExcluirUsuario.classList.remove('is_desactive');
    }

    // Adiciona o evento de clique aos botões "Voltar" de usuario
    btnVoltarUsuario.forEach(function(botao) {
        botao.addEventListener('click', function(event) {
            event.preventDefault();  // Evita o comportamento padrão do link
            mostrarDadosUsuario();
        });
    });

    // Adiciona o evento de clique ao botão "Atualizar Informações"
    if (btnEditarUsuario) {
        btnEditarUsuario.addEventListener('click', function(event) {
            event.preventDefault();  // Evita o comportamento padrão do link
            mostrarEditarUsuario();
        });
    }

    // Adiciona o evento de clique ao botão "Excluir Conta"
    if (btnExcluirConta) {
        btnExcluirConta.addEventListener('click', function(event) {
            event.preventDefault();  // Evita o comportamento padrão do link
            mostrarExcluirUsuario();
        });
    }

    // -------------------------------------------------------------------------------------------
    // SEÇÃO DE ENDEREÇO

    // Obtém as seções específicas de endereço
    const sectionEnderecoPrincipal = document.querySelector('.endereco');
    const sectionAdicionarEndereco = document.querySelector('.adicionar-endereco-content');
    const sectionVisualizarEndereco = document.querySelector('.visualizar-endereco-content');
    const sectionEditarEndereco = document.querySelector('.editar-endereco-content');
    
    // Seleciona os botões
    const btnAdicionarEndereco = document.querySelector('.adicionar-endereco'); // Botão "+ Endereço"
    const btnVoltar = document.querySelectorAll('.voltar-endereco'); // Botões "Voltar"
    const btnEditarEndereco = document.querySelectorAll('.editar-endereco'); // Botões "Editar Informações"


    // Função para exibir o formulário de adicionar endereço
    function mostrarAdicionarEndereco() {
        esconderSecoesEndereco();
        sectionAdicionarEndereco.classList.remove('is_desactive');
    }

    // Função para voltar à lista de endereços
    function voltarParaEndereco() {
        esconderSecoesEndereco();
        sectionEnderecoPrincipal.classList.remove('is_desactive');
    }

    // Função para carregar o endereço via AJAX usando Fetch API
    function carregarEndereco(url) {
        fetch(url)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Erro ao buscar o endereço');
                }
                return response.json();
            })
            .then(data => {
                mostrarVisualizarEndereco(data);
            })
            .catch(error => {
                console.error('Erro:', error);
                alert('Erro ao carregar os dados do endereço.');
            });
    }

    // Função para exibir a seção de edição de endereço com os dados
    function mostrarEditarEndereco(endereco){
        esconderSecoesEndereco();
        sectionEditarEndereco.classList.remove('is_desactive');

        document.querySelector('#endereco_id').value = endereco.id;
        document.querySelector('.editar_nome_da_propriedade').value = endereco.nome_da_propriedade;

        document.querySelector('.editar_complemento').value = endereco.complemento;
        
    }

    // Função para exibir a seção de visualizar endereço com os dados
    function mostrarVisualizarEndereco(endereco) {
        esconderSecoesEndereco();

        // Preencher a seção de visualização com os dados do endereço
        document.querySelector('#visualizarEnderecoID').textContent = endereco.id;
        document.querySelector('#endereco_id').value = endereco.id;
        document.querySelector('#form-excluir-endereco').action = "delete/" + endereco.id + "/";
        document.querySelector('#visualizarEnderecoNome').textContent = endereco.nome_da_propriedade;
        document.querySelector('.visualizarEnderecoNome').textContent = endereco.nome_da_propriedade;
        document.querySelector('#visualizarEnderecoEstado').textContent = endereco.estado;
        document.querySelector('#visualizarEnderecoMunicipio').textContent = endereco.municipio;
        document.querySelector('#visualizarEnderecoDistrito').textContent = endereco.distrito;
        document.querySelector('#visualizarEnderecoCep').textContent = endereco.cep;
        document.querySelector('#visualizarEnderecoComplemento').textContent = endereco.complemento;

        sectionVisualizarEndereco.classList.remove('is_desactive');

        // Adiciona o evento de clique aos botões "Editar informações"
        btnEditarEndereco.forEach(function(botao) {
            botao.addEventListener('click', function(event) {
                event.preventDefault();  // Evita o comportamento padrão do link
                mostrarEditarEndereco(endereco);
            });
        });
    }

    // Função para esconder apenas as seções relacionadas a endereços
    function esconderSecoesEndereco() {
        sectionAdicionarEndereco.classList.add('is_desactive');
        sectionVisualizarEndereco.classList.add('is_desactive');
        sectionEnderecoPrincipal.classList.add('is_desactive');
        sectionEditarEndereco.classList.add('is_desactive');
    }

    // Adiciona o evento de clique ao botão "+ Endereço"
    if (btnAdicionarEndereco) {
        btnAdicionarEndereco.addEventListener('click', function(event) {
            event.preventDefault();  // Evita o comportamento padrão do link
            mostrarAdicionarEndereco();
        });
    }

    // Adiciona o evento de clique aos botões "Voltar"
    btnVoltar.forEach(function(botao) {
        botao.addEventListener('click', function(event) {
            event.preventDefault();  // Evita o comportamento padrão do link
            voltarParaEndereco();
        });
    });

    

    // Adiciona o evento de clique aos botões "Visualizar" na tabela de endereços
    const visualizarBotoes = document.querySelectorAll('.read-endereco');

    visualizarBotoes.forEach(function (botao) {
        botao.addEventListener('click', function (event) {
            event.preventDefault();
            const url = this.getAttribute('data-url');
            carregarEndereco(url);
        });
    });
});

// DELETAR ENDEREÇO

document.addEventListener("DOMContentLoaded", function() {
    // Seleciona todos os botões de exclusão
    const deleteButtons = document.querySelectorAll('.delete-endereco');

    // Seleciona o pop-up de deletar endereço
    const deletePopup = document.querySelector('.deletar-endereco-pop_up');

    // Seleciona o botão de cancelar no pop-up
    const cancelDeleteButton = document.querySelector('#cancelar-excluir');

    // Função para mostrar o pop-up de exclusão
    function mostrarPopupExclusao() {
        deletePopup.classList.add('is_displayflex');
    }

    // Função para ocultar o pop-up de exclusão
    function ocultarPopupExclusao() {
        deletePopup.classList.remove('is_displayflex');
    }

    // Adiciona o evento de clique a todos os botões de exclusão
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault(); // Evita o comportamento padrão do link
            mostrarPopupExclusao();
        });
    });

    // Adiciona o evento de clique ao botão de cancelar no pop-up
    cancelDeleteButton.addEventListener('click', function(event) {
        event.preventDefault(); // Evita o comportamento padrão do link
        ocultarPopupExclusao();
    });
});
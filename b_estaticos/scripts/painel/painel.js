document.addEventListener('DOMContentLoaded', function() {
    const sections = {
        painel: document.querySelector('#painel'),
        relatorios: document.querySelector('#relatorios'),
        configuracoes: document.querySelector('#configuracoes')
    };

    const contentSections = {
        painel: document.querySelector('.section-painel-inicio'),
        relatorios: document.querySelector('.section-relatorios'),
        configuracoes: document.querySelector('.section-configurações')
    };

    function handleSectionClick(selectedSection) {
        // Gerencia a classe 'is-selected' nos botões do menu
        Object.keys(sections).forEach(section => {
            if (section === selectedSection) {
                sections[section].classList.add('is-selected');
            } else {
                sections[section].classList.remove('is-selected');
            }
        });

        // Gerencia a classe 'is_desactive' nas seções de conteúdo
        Object.keys(contentSections).forEach(section => {
            if (section === selectedSection) {
                contentSections[section].classList.remove('is_desactive');
            } else {
                contentSections[section].classList.add('is_desactive');
            }
        });
    }

    sections.painel.addEventListener('click', function() {
        handleSectionClick('painel');
    });

    sections.relatorios.addEventListener('click', function() {
        handleSectionClick('relatorios');
    });

    sections.configuracoes.addEventListener('click', function() {
        handleSectionClick('configuracoes');
    });
});

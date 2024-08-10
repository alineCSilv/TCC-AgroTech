
/*Script para manipulação de dados de análises de solo*/

//Função para enviar os dados do formulário para o servidor
document.getElementById('analiseForm').addEventListener('submit', function (event) {
    event.preventDefault();
    var formData = new FormData(this);
    var isEditing = !!document.getElementById('cod_analise').value;
    var acao = isEditing ? '/edit' : '/exc';
    fetch('/analises', {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                updateTableRow(data.analise, isEditing, acao);

                document.getElementById('analiseForm').reset();
                $('#analiseModal').modal('hide');
            } else {
                alert('Erro ao cadastrar a análise.');
            }
        })
        .catch(error => console.error('Erro:', error));
});

//Função para atualizar a tabela de análises
function updateTableRow(analise, isEditing, acao) {
    //console.log(analise);
    var rowHTML = `
            <tr>
                <td>${analise.cod_analise}</td>
                <td>${analise.proprietario}</td>
                <td>${analise.data_cadastro}</td>
                <td>${analise.vl_ph}</td>
                <td>${analise.vl_fosforo}</td>
                <td>${analise.vl_potassio}</td>
                <td>${analise.vl_magnesio}</td>
                <td>${analise.vl_calcio}</td>
                <td>${analise.vl_al}</td>
                <td>${analise.vl_h_al}</td>
                <td>${analise.vl_sb}</td>
                <td>${analise.vl_ctc}</td>
                <td>${analise.vl_saturacao}</td>
                <td>${analise.vl_im}</td>
                <td>${analise.vl_mo}</td>
                <td>
                    <button class="btn btn-sm btn-primary" onclick="editAnalise(this)">Editar</button>
                </td>
            </tr>
        `;

    if (isEditing) {
        var existingRows = document.querySelectorAll('#analisesTableBody tr');
        var updated = false;
        if (acao == '/exc') {
            existingRows.forEach(function (row) {
                var cell = row.querySelector('td:first-child');
                if (cell && cell.innerText == analise.cod_analise) {
                    row.remove();
                    updated = true;
                }
            });
        }
        else {
            existingRows.forEach(function (row) {
                var cell = row.querySelector('td:first-child');
                if (cell && cell.innerText == analise.cod_analise) {
                    row.innerHTML = rowHTML;
                    updated = true;
                }
            });
        }

        if (!updated) {
            console.error('Error: Existing row not found');
        }
    } else {
        document.getElementById('analisesTableBody').insertAdjacentHTML('beforeend', rowHTML);
    }
}


function editAnalise(button) {
    var row = button.parentElement.parentElement;
    var cells = row.getElementsByTagName('td');

    // Preenche o formulário com os valores da linha selecionada
    document.getElementById('cod_analise').value = cells[0].innerText;
    document.getElementById('proprietario').value = cells[1].innerText;
    document.getElementById('dataAnalise').value = cells[2].innerText;
    document.getElementById('ph').value = cells[3].innerText;
    document.getElementById('fosforo').value = cells[4].innerText;
    document.getElementById('potassio').value = cells[5].innerText;
    document.getElementById('magnesio').value = cells[6].innerText;
    document.getElementById('calcio').value = cells[7].innerText;
    document.getElementById('al').value = cells[8].innerText;
    document.getElementById('h_al').value = cells[9].innerText;
    document.getElementById('sb').value = cells[10].innerText;
    document.getElementById('ctc').value = cells[11].innerText;
    document.getElementById('saturacao').value = cells[12].innerText;
    document.getElementById('im').value = cells[13].innerText;
    document.getElementById('mo').value = cells[14].innerText;

    // Remove a linha antiga
    //row.remove();

    // Mostra o formulário para edição
    $('#analiseModal').modal('show');

    //Altera o botão da modal para editar
    var button = document.querySelector('#analiseModal button[type="submit"]');
    button.innerText = 'Salvar';

}

//Função para excluir a análise
document.getElementById('btn_excluir').addEventListener('click', function (event) {
    event.preventDefault();

    var formData = new FormData(document.getElementById('analiseForm'));
    var isEditing = !!document.getElementById('cod_analise').value;
    var acao = '/exc';

    fetch('/delete-analise', {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                updateTableRow(data.analise, isEditing, acao);

                document.getElementById('analiseForm').reset();
                $('#analiseModal').modal('hide');
            } else {
                alert('Erro ao excluir a análise.');
            }
        })
        .catch(error => console.error('Erro:', error));
});

function preencherComDadosDeTeste() {
    const nomes = ['João Silva', 'Maria Souza', 'Carlos Oliveira', 'Ana Lima', 'Pedro Santos', 'Paula Fernandes', 'José Ferreira', 'Clara Pereira'];
    const nomeProprietario = nomes[Math.floor(Math.random() * nomes.length)];

    const dataAnalise = new Date();
    dataAnalise.setDate(dataAnalise.getDate() - Math.floor(Math.random() * 365)); // Data aleatória no último ano
    const dataAnaliseFormatada = dataAnalise.toISOString().split('T')[0];

    const ph = (Math.random() * (7.5 - 5.0) + 5.0).toFixed(2);
    const fosforo = (Math.random() * (30 - 10) + 10).toFixed(2);
    const potassio = (Math.random() * (50 - 20) + 20).toFixed(2);
    const magnesio = (Math.random() * (5.0 - 1.0) + 1.0).toFixed(2);
    const calcio = (Math.random() * (10.0 - 2.0) + 2.0).toFixed(2);
    const al = (Math.random() * (1.0 - 0.5) + 0.5).toFixed(2);
    const h_al = (Math.random() * (3.0 - 1.0) + 1.0).toFixed(2);
    const sb = (Math.random() * (8.0 - 3.0) + 3.0).toFixed(2);
    const ctc = (Math.random() * (10.0 - 5.0) + 5.0).toFixed(2);
    const saturacao = (Math.random() * (80 - 50) + 50).toFixed(2);
    const im = (Math.random() * (20 - 5) + 5).toFixed(2);
    const mo = (Math.random() * (5.0 - 1.0) + 1.0).toFixed(2);

    document.getElementById('proprietario').value = nomeProprietario;
    document.getElementById('dataAnalise').value = dataAnaliseFormatada;
    document.getElementById('ph').value = ph;
    document.getElementById('fosforo').value = fosforo;
    document.getElementById('potassio').value = potassio;
    document.getElementById('magnesio').value = magnesio;
    document.getElementById('calcio').value = calcio;
    document.getElementById('al').value = al;
    document.getElementById('h_al').value = h_al;
    document.getElementById('sb').value = sb;
    document.getElementById('ctc').value = ctc;
    document.getElementById('saturacao').value = saturacao;
    document.getElementById('im').value = im;
    document.getElementById('mo').value = mo;
}

// Função para preencher o formulário e a tabela na inicialização
function inicializarDados() {
    fetch('/listar-analises')
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success')
                data.analises.forEach(analise => updateTableRow(analise, false, null));
            else
                alert('Erro ao carregar as análises.');
        })
        .catch(error => console.error('Erro:', error));

    var tbody = document.getElementById('analisesTableBody');

    
}


// Chamar a função para preencher os inputs com dados ao carregar a página
window.onload = function () {
    inicializarDados();
    preencherComDadosDeTeste();
};

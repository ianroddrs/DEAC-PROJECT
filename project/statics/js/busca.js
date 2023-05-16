// mudar tipo de input de acordo com select
function mudarTipoInput() {
    var select = document.getElementById("tipo-input");
    var input = document.getElementById("meu-input");
    var novoTipo = select.value;
    input.type = novoTipo;
  }


  

// adicionar e remover selects

document.addEventListener('DOMContentLoaded', function() {
    const btnAdicionarselect = document.getElementById('btn-adicionar-select');
    const selectsContainer = document.getElementById('selects');
    let contador = 2;

    btnAdicionarselect.addEventListener('click', function() {
      const novoselect = document.createElement('div');
      novoselect.classList.add('select');

      const selectHTML = `
        <label for="select_coluna_${contador}">Select:</label>
        <select id="select_coluna_${contador}" name="select_coluna_${contador}" >
          <option value="">Selecione uma coluna</option>
          {% for coluna in colunas %}
          <option value="{{ coluna }}">{{ coluna }}</option>
          {% endfor %}
        </select>
        <input type="text" id="select_valor_${contador}" name="select_valor_${contador}"  placeholder="Valor">
        <button type="button" class="btn-apagar-select">Apagar</button>
      `;

      novoselect.innerHTML = selectHTML;
      selectsContainer.appendChild(novoselect);
      contador++;
    });

    selectsContainer.addEventListener('click', function(event) {
      if (event.target.classList.contains('btn-apagar-select')) {
        const select = event.target.closest('.select');
        if (selectsContainer.children.length > 1) {
          select.remove();
        } else {
          const select = select.querySelector('select');
          const input = select.querySelector('input');
          select.value = '';
          input.value = '';
        }
      }
    });
  });
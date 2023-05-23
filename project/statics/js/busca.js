// adicionar selects
function adicionar_select(){

  const selectsContainer = document.getElementById('selects');
  let contador = 2;

  const novoselect = document.createElement('div');
  novoselect.classList.add('select');

  const selectHTML = `
  <label for="select_coluna_1">Select:</label>
    <select id="select_coluna_1" name="select_coluna_1" onchange="mudarTipoInput()">
      <option value="">Selecione uma coluna</option>
      {% for coluna in colunas %}
      <option value="{{ coluna }}">{{ coluna }}</option>
      {% endfor %}
    </select>
    <input type="search" id="select_valor_1" name=""  placeholder="Buscar por...">
    <button type="button" class="btn-apagar-select" onclick="remover_select(this)"><i class="bi bi-trash"></i></button>
  `;

  novoselect.innerHTML = selectHTML;
  selectsContainer.appendChild(novoselect);
  contador++;
}

// remover selects
function remover_select(button){
  const selectsContainer = document.getElementById('selects');
  var busca = button.parentNode;
  var selectElement = busca.querySelector("select");
  var inputElement = busca.querySelector("input");
  if (selectsContainer.children.length > 1) {
    busca.remove();
  } else {
    selectElement.value = '';
    inputElement.value = '';
  }
}



/////////////////////////////////////////////////////////

function select_name(select){

  var busca = select.parentNode;
  var inputElement = busca.querySelector("input");
  inputElement.name = select.value
}
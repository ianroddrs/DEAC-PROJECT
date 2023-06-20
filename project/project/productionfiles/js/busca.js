document.addEventListener("DOMContentLoaded", function() {
  const dropdownItems = document.querySelectorAll(".dropdown-item");
  const btnApagar = document.querySelectorAll(".btn-apagar");
  const inputs = document.querySelectorAll(".input_lista");
  const btnAdd = document.querySelectorAll(".btn-add");

  // Função para adicionar um elemento à lista
  function adicionarElemento(divLista, inputTexto, inputLista) {
    const lista = inputTexto.value.split(",");

    for (let i = lista.length - 1; i >= 0; i--) {
      let elemento = lista[i].trim();
    
      if (elemento === "") {
        lista.splice(i, 1);
      } else {
        lista[i] = elemento;
      }
    }

    lista.forEach(function(elemento) {
      if (elemento.trim() !== "") {
        const novoBadge = document.createElement("span");
        novoBadge.classList.add('align-items-center','mx-1', 'border', 'rounded-pill', 'px-1')
        novoBadge.textContent = elemento.trim();
        
        const divisor = document.createElement("span");
        divisor.classList.add('vr', 'mx-2')



        // <span class="badge d-flex align-items-center p-1 pe-2 text-secondary-emphasis bg-secondary-subtle border border-secondary-subtle rounded-pill">
        //   <img class="rounded-circle me-1" width="24" height="24" src="https://github.com/mdo.png" alt="">
        //   Secondary
        //   <span class="vr mx-2"></span>
        //   <a href="#"><i class="bi bi-x-circle-fill"></i></a>
        // </span>

        
        const botaoDiv = document.createElement("a");
        botaoDiv.innerHTML = '<i class="bi bi-x-circle-fill"></i>'
        
        botaoDiv.onclick = function() {
          divLista.removeChild(novoBadge);
          
          let valorParaRemover = novoBadge.textContent;
          let index = lista.indexOf(valorParaRemover);
          if (index !== -1) {
            lista.splice(index, 1);
          }

          inputLista.value = lista.join()
        };
        novoBadge.appendChild(divisor)
        novoBadge.appendChild(botaoDiv);
        divLista.appendChild(novoBadge);
      }
    });
  }

  // Função para atualizar o estado do dropdown
  function atualizarDropdown(targetItem, targetDiv, inputValue) {
    targetItem.classList.toggle("selected");
    targetDiv.style.display = targetItem.classList.contains("selected") ? "block" : "none";
    inputValue = targetItem.classList.contains("selected") ? "" : inputValue;
  }

  // Função para limpar os campos
  function limparCampos(targetDiv, inputLista) {
    const divLista = targetDiv
    while (divLista.firstChild) {
      divLista.removeChild(divLista.firstChild);
    }
    inputLista.value = "";
  }

  // Loop para mostrar inputs com valores ao carregar a página
  inputs.forEach(function(input) {
    if (input.value !== "") {
      const targetData = input.getAttribute("name");
      const divLista = document.getElementById(`block-lista-${targetData}`);
      const inputLista = document.getElementById(`lista-${targetData}`);
      const dropdownItem = document.querySelector(`.dropdown-item[data-target="${targetData}"]`);
      adicionarElemento(divLista, inputLista, inputLista);

      dropdownItem.classList.add("selected");

      const targetDiv = document.getElementById(`select-${targetData}`);
      targetDiv.style.display = "block";
    }
  });

  // Loop para adicionar inputs pelo botão
  btnAdd.forEach(function(item) {
    item.addEventListener("click", function() {
      const targetData = item.getAttribute("data-target");
      const input = document.getElementById(targetData);
      const divLista = document.getElementById(`block-lista-${targetData}`);
      const inputLista = document.getElementById(`lista-${targetData}`);
      if (input.value != "") {
        if (input.value.trim() !== "") {
          adicionarElemento(divLista, input, inputLista);
        }
        inputLista.value += input.value + ",";
        input.value = "";
      }
    });
  });

  // Loop para adicionar e remover inputs pelo dropdown
  dropdownItems.forEach(function(item) {
    item.addEventListener("click", function() {
      const targetId = item.getAttribute("data-target");
      const targetDiv = document.getElementById(`select-${targetId}`);
      const input = targetDiv.querySelector("input");

      atualizarDropdown(item, targetDiv, input.value);
    });
  });

  // Loop para remover inputs pelo botão
  btnApagar.forEach(function(item) {
    item.addEventListener("click", function() {
      const targetData = item.getAttribute("data-target");
      const targetDiv = document.getElementById(`select-${targetData}`);
      const inputLista = document.getElementById(`lista-${targetData}`);
      const blockLista = document.getElementById(`block-lista-${targetData}`);

      const dropdownItem = document.querySelector(`.dropdown-item[data-target="${targetData}"]`);
      dropdownItem.classList.remove("selected");

      const inputElement = targetDiv.querySelector("input");
      targetDiv.style.display = "none";
      inputLista.value = "";
      inputElement.value = "";

      limparCampos(blockLista, inputLista);
    });
  });
});

document.addEventListener("DOMContentLoaded", function() {
  const searchInput = document.getElementById("dropdown-search-input");
  const dropdownItems = document.querySelector(".dropdown-items").children;

  searchInput.addEventListener("input", function() {
    const searchText = searchInput.value.toLowerCase();

    for (let i = 0; i < dropdownItems.length; i++) {
      const dropdownItem = dropdownItems[i];
      const itemText = dropdownItem.textContent.toLowerCase();

      dropdownItem.style.display = itemText.includes(searchText) ? "block" : "none";
    }
  });
});

document.addEventListener("DOMContentLoaded", function() {
  const inputs = document.querySelectorAll(".input_busca");

  function mascara(obj, fun) {
    obj.addEventListener("keyup", function() {
      obj.value = fun(obj.value);
    });
  }

  function mboletim(v) {
    v = v.replace(/\D/g, "");
    v = v.replace(/(\d)(\d{1})$/, "$1-$2");
    v = v.replace(/^(\d{5,9})(\d{6})/g, "$1.$2");
    v = v.replace(/^(\d{1,5})(\d{4})/g, "$1/$2");
    return v;
  }

  function mtext(v) {
    v = v.replace(/[^a-zA-ZÀ-ú0-9\s]/g, "");
    v = v.toUpperCase();
    v = v.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
    v = v.replace(/Ç/g, "C");
    return v;
  }

  inputs.forEach(function(input) {
    const inputType = input.getAttribute("mask");
    const maskFunction = inputType === "bop" ? mboletim : mtext;
    mascara(input, maskFunction);
  });
});

/////////////////////////
// PAGINAÇÃO
////////////////////////

$(document).ready(function(){
  $('#tabela').DataTable({
  language: {
      url: '//cdn.datatables.net/plug-ins/1.13.4/i18n/pt-BR.json',
  },
  responsive: true,
  "aaSorting": [],
});
});
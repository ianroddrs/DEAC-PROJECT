//////////////////////////////////////////////////////////
/////////              DROPDOWN                ///////////
//////////////////////////////////////////////////////////

document.addEventListener("DOMContentLoaded", function() {
  const dropdownItems = document.querySelectorAll(".dropdown-item");
  const btnApagar = document.querySelectorAll(".btn-apagar");
  const inputs = document.querySelectorAll(".input_busca");

  inputs.forEach(function(input) {
    if (input.value !== "") {
      const targetData = input.getAttribute("name");
      const dropdownItem = document.querySelector(`.dropdown-item[data-target="${targetData}"]`);
      dropdownItem.classList.add("selected");

      const targetDiv = document.getElementById(`select-${targetData}`);
      targetDiv.style.display = "block";
    }
  });

  dropdownItems.forEach(function(item) {
    item.addEventListener("click", function() {
      const targetId = item.getAttribute("data-target");
      const targetDiv = document.getElementById(`select-${targetId}`);
      const input = targetDiv.querySelector("input");

      item.classList.toggle("selected");
      targetDiv.style.display = (item.classList.contains("selected")) ? "block" : "none";
      input.value = (item.classList.contains("selected")) ? "" : input.value;
    });
  });

  btnApagar.forEach(function(item) {
    item.addEventListener("click", function() {
      const targetData = item.getAttribute("data-target");
      const targetDiv = document.getElementById(`select-${targetData}`);

      const dropdownItem = document.querySelector(`.dropdown-item[data-target="${targetData}"]`);
      dropdownItem.classList.remove("selected");

      var element = item.parentNode;
      var inputElement = element.querySelector("input");
      targetDiv.style.display = 'none';
      inputElement.value = '';
    });
  });

});

//////////////////////////////////////////////////////////
/////////          PESQUISA NO DROPDOWN        ///////////
//////////////////////////////////////////////////////////

document.addEventListener("DOMContentLoaded", function() {
  const searchInput = document.getElementById("dropdown-search-input");
  const dropdownItems = document.querySelector(".dropdown-items").children;

  searchInput.addEventListener("input", function() {
    const searchText = searchInput.value.toLowerCase();

    for (let i = 0; i < dropdownItems.length; i++) {
      const dropdownItem = dropdownItems[i];
      const itemText = dropdownItem.textContent.toLowerCase();

      if (itemText.includes(searchText)) {
        dropdownItem.style.display = "block";
      } else {
        dropdownItem.style.display = "none";
      }
    }
  });
});

//////////////////////////////////////////////////////////
/////////          MASCARAS DE INPUT           ///////////
//////////////////////////////////////////////////////////

document.addEventListener("DOMContentLoaded", function() {
  var inputs = document.querySelectorAll(".input_busca");

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
    var inputType = input.getAttribute("mask");
    if(inputType == "bop"){
      mascara(input, mboletim);
    } else if(inputType == "text"){
      mascara(input, mtext);
    }
  });
});

//////////////////////////////////////////////////////////
/////////      ADICIONAR PESQUISA INPUT        ///////////
//////////////////////////////////////////////////////////
document.addEventListener("DOMContentLoaded", function() {
  
});


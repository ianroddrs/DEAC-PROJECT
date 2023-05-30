// adicionar / remover inputs na tela
document.addEventListener("DOMContentLoaded", function() {
  const dropdownItems = document.querySelectorAll(".dropdown-item");
  const btnApagar = document.querySelectorAll(".btn-apagar");

  dropdownItems.forEach(function(item) {
    item.addEventListener("click", function() {
      const targetId = item.getAttribute("data-target");
      const targetDiv = document.getElementById(targetId);
      const input = targetDiv.querySelector("input");

      item.classList.toggle("selected");
      targetDiv.style.display = (item.classList.contains("selected")) ? "block" : "none";
      input.value = (item.classList.contains("selected")) ? "" : input.value;
    });
  });

  btnApagar.forEach(function(item){
    item.addEventListener("click", function(){
      const targetData = item.getAttribute("data-target");
      const targetDiv = document.getElementById(targetData);      

      const dropdownItem = document.querySelector(`.dropdown-item[data-target="${targetData}"]`);
      dropdownItem.classList.remove("selected");

      var element = item.parentNode;
      var inputElement = element.querySelector("input");
      targetDiv.style.display = 'none'
      inputElement.value = '';
    });
  });

  document.querySelectorAll("div#selects").forEach(function(selectsDiv) {
    // Selecionar todos os inputs dentro da div
    const inputs = selectsDiv.querySelectorAll("input");
  
    // Verificar se algum dos inputs não está vazio
    let hasValue = false;
    inputs.forEach(function(input) {
      if (input.value !== "") {
        hasValue = true;
      }
    });
  
    // Exibir a div e marcar o dropdown-item relacionado como selecionado
    if (hasValue) {
      selectsDiv.style.display = "block";
      const dropdownItem = document.querySelector(`.dropdown-item[data-target="${selectsDiv.id}"]`);
      dropdownItem.classList.add("selected");
    }
  });
});

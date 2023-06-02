document.addEventListener("DOMContentLoaded", function() {
  const dropdownItems = document.querySelectorAll(".dropdown-item");
  const btnApagar = document.querySelectorAll(".btn-apagar");
  const inputs = document.querySelectorAll(".input_busca");

  inputs.forEach(function(input) {
    if (input.value !== "") {
      const targetData = input.getAttribute("name");
      const dropdownItem = document.querySelector(`.dropdown-item[data-target="${targetData}"]`);
      dropdownItem.classList.add("selected");

      const targetDiv = document.getElementById(targetData);
      targetDiv.style.display = "block";
    }
  });

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

  btnApagar.forEach(function(item) {
    item.addEventListener("click", function() {
      const targetData = item.getAttribute("data-target");
      const targetDiv = document.getElementById(targetData);

      const dropdownItem = document.querySelector(`.dropdown-item[data-target="${targetData}"]`);
      dropdownItem.classList.remove("selected");

      var element = item.parentNode;
      var inputElement = element.querySelector("input");
      targetDiv.style.display = 'none';
      inputElement.value = '';
    });
  });

});

document.addEventListener("DOMContentLoaded", function() {
    const input_nro_bop = document.getElementById("nro_bop");
    const input_nro_tombo = document.getElementById("nro_tombo");
    const selects = document.querySelectorAll(".dd-select");

    input_nro_bop.style.display = "block";
    input_nro_tombo.style.display = "none";

    selects.forEach(function(btn){
        btn.onclick = function(){
            selects.forEach(function(btn){
                btn.classList.remove("selected");
            });
            
            if (btn.textContent == "nro_bop") {
                input_nro_bop.style.display = "block";
                input_nro_tombo.style.display = "none";
            } else if (btn.textContent == "nro_tombo") {
                input_nro_bop.style.display = "none";
                input_nro_tombo.style.display = "block";
            }
            
            btn.classList.add("selected");
        }
    });
});

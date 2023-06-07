function calculate() {
    const v1 = document.getElementById("v1").value;
    const v2 = document.getElementById("v2").value;

    $.get("http://localhost:8080/add", { value1:v1, value2:v2}, (data) => {
        document.getElementById("resultado").innerHTML="Resultado: " + data;
    });      
}

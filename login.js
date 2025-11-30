function login(){

    const email = document.getElementById("email").value;
    const senha = document.getElementById("senha").value;
    
    if (email === "philipea@gmail.com" && senha === "12345") {
        alert("Login Realizado com sucesso");
        window.location.href = "home.html";

    }else if(email === "admin@gmail.com" && senha === "12345"){
        alert("Login Realizado com sucesso");
        window.location.href = "home.html";

    }else if(email === "funcionario@gmail.com" && senha === "12345"){
        alert("Login Realizado com sucesso");
        window.location.href = "home.html";  
    
    }else{
        alert("Dados de login incorretos!!!")
    }
}
function login(){

    const email = document.getElementById("email").value;
    const senha = document.getElementById("senha").value;
    
    if (email === "0336699@gmail.com" && senha === "12345678") {
        alert("Login Realizado com sucesso");
        window.location.href = "home.html";

    }else if(email === "admin@gmail.com" && senha === "12345678"){
        alert("Login Realizado com sucesso");
        window.location.href = "home.html";

    }else if(email === "funcionario@gmail.com" && senha === "12345678"){
        alert("Login Realizado com sucesso");
        window.location.href = "home.html";  
    
    }else{
        alert("Dados de login incorretos!!!")
    }
}
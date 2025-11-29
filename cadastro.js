function cadastro(){
    const nome = document.getElementById('nome')?.value.trim();
    const email = document.getElementById('email')?.value.trim();
    const senha = document.getElementById('senha')?.value || '';
    const senhaConfirm = document.getElementById('senhaConfirm')?.value || '';

    if(!nome){
        alert('Por favor, informe o nome.');
        return;
    }
    if(!email){
        alert('Por favor, informe o email.');
        return;
    }
    if(senha.length <= 6){
        alert('A senha deve ter mais de 6 caracteres.');
        return;
    }
    if(senha !== senhaConfirm){
        alert('As senhas não conferem. Por favor, verifique.');
        return;
    }

    alert('Cadastro realizado com sucesso!');
    window.location.href = 'login.html';
}
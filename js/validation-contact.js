const formulario = document.getElementById('formulario-container');
const inputs = document.querySelectorAll('#formulario-container input');

const expresiones = {
	nombre: /^[a-zA-ZÀ-ÿ]{2,20}$/, // Letras, pueden llevar acentos.
	apellido: /^[a-zA-ZÀ-ÿ]{1,20}$/, // Letras, pueden llevar acentos.
	edad: /^\d{1,2}$/, // 7 a 14 numeros
	email: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/, //nombre.apellido2@gmail.com
	telefono: /^\d{7,15}$/, // 7 a 14 numeros. 
	comentarios: /^[a-zA-Z0-9\s]{10,150}$/ // 2 a 150 caracteres. 
} 
const validarFormulario = (e) => {
    switch(e.target.name){
        case "nombre":
            validarCampo(expresiones.nombre, e.target, 'nombre');
        break;
        case "apellido":
            validarCampo(expresiones.apellido, e.target, 'apellido');
        break;
        case "edad":
            validarCampo(expresiones.edad, e.target, 'edad');
        break;
        case "email":
            validarCampo(expresiones.email, e.target, 'email');
        break;
        case "telefono":
            validarCampo(expresiones.telefono, e.target,'telefono');
        break;
        case "comentario":
            validarCampo(expresiones.comentarios, e.target,'comentarios')
        break;
    }
}

const validarCampo = (expresion, input, campo) => {
    if(expresion.test(input.value)){
        document.getElementById(`grid-container-${campo}`).classList.remove("flex-container-form-incorrecto"); 
        document.getElementById(`grid-container-${campo}`).classList.add("flex-container-form-correcto"); 
        document.getElementById(`grid-container-${campo}`).classList.remove("formulario__input-error")
    }else{
        document.getElementById(`grid-container-${campo}`).classList.add("flex-container-form-incorrecto"); 
        document.getElementById(`grid-container-${campo}`).classList.remove("flex-container-form-correcto"); 
        document.getElementById(`grid-container-${campo}`).classList.add("formulario__input-error")
    }
}
inputs.forEach((input) => {
	input.addEventListener('keyup', validarFormulario);
	input.addEventListener('blur', validarFormulario);
});

document.getElementById('')
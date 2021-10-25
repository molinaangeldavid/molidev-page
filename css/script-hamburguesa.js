let visible = false;

function mostrarMenuVertical (){

    // alert("hola")
    let m = document.getElementById("menu_alternativo");
    if(visible){
        m.style.display='block';

    } else {
        m.style.display='none';

    }
    visible = !visible;

}


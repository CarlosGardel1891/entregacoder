(function(){
    const btnEliminar = document.querySelectorAll(".btnEliminar")

btnEliminar.forEach(btn=> {
    btn.addEventListener('click', (e)=>{
        const confirmar = confirm("seguro que quiere eliminar el curso?");
        if(!confirmar){
            e.preventDefault();
        }
    });
});

})();
campo_editarPratoID  = document.getElementById('field_editPlateID')
campo_editarNome     = document.getElementById('field_editName')
campo_editarCategoria = document.getElementById('field_editCategory')
campo_editarPreco    = document.getElementById('field_editPrice')

function loadModalFieldsEditPanel(component){ 
    cells = component.parentNode.parentNode.cells;
    campo_editarPratoID .value  = cells[0].innerHTML;
    campo_editarNome.value     = cells[1].innerHTML;
    campo_editarCategoria.value = cells[2].innerHTML;
    campo_editarPreco.value    = cells[3].innerHTML;
}
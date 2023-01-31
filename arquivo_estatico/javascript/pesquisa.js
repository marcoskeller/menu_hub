campoPratoId = document.getElementById('campoPratoId')
campoNomePrato = document.getElementById('campoNomePrato')
    
document.getElementById('radioPratoId').onclick = (e) => {
    campoPratoId.disabled = false
    campoNomePrato.disabled = true
} 

document.getElementById('radioPratoNome').onclick = (e) => {
    campoPratoId.disabled = true
    campoNomePrato.disabled = false
}
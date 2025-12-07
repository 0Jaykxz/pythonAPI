//é os guri, não adianta

function excluir(id) {
    fetch(`/delete/${id}`, { method: "POST" })
        .then(() => location.reload())
}


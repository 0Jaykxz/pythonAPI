document.getElementById('userForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const form = e.target;
    const action = form.action;

    const data = {
        nome: document.getElementById('name').value,
        email: document.getElementById('email').value
    };

    const isEdit = action.includes('/update') || action.match(/\/\d+$/);

    fetch(action, {
        method: isEdit ? 'PUT' : 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(resp => {
        if (resp.redirect) {
            window.location.href = resp.redirect;
        }
    })
    .catch(() => {
        alert('Erro ao salvar usuário');
    });
});

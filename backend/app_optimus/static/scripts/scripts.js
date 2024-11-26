document.querySelectorAll('.toggle-sidebar').forEach((button) => {
    button.addEventListener('click', () => {
        document.querySelector('.sidebar').classList.toggle('collapsed');
    });
});

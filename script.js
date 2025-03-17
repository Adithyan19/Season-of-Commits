function redirectTo(page) {
    window.location.href = page;
}

document.addEventListener('DOMContentLoaded', () => {
    const sidebar = document.getElementById('sidebar');

    sidebar.addEventListener('mouseenter', () => {
        sidebar.classList.remove('collapsed');
    });

    sidebar.addEventListener('mouseleave', () => {
        sidebar.classList.add('collapsed');
    });
});
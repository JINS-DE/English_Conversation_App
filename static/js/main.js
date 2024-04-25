document.addEventListener('DOMContentLoaded', function() {
    const loginButton = document.querySelector('.btn-primary');
    loginButton.addEventListener('click', function() {
        loginButton.textContent = "Logging in...";
    });
});
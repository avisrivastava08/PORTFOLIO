document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.getElementById('theme-toggle');
    const body = document.body;
    const icon = themeToggle.querySelector('i');
    
    // Check for saved theme preference
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        body.classList.add('dark-mode');
        icon.classList.replace('bi-moon-fill', 'bi-sun-fill');
    }
    
    themeToggle.addEventListener('click', () => {
        body.classList.toggle('dark-mode');
        
        if (body.classList.contains('dark-mode')) {
            localStorage.setItem('theme', 'dark');
            icon.classList.replace('bi-moon-fill', 'bi-sun-fill');
        } else {
            localStorage.setItem('theme', 'light');
            icon.classList.replace('bi-sun-fill', 'bi-moon-fill');
        }
    });
}); 
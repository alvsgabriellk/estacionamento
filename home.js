function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('sidebarOverlay');
    const hamburger = document.getElementById('hamburgerMenu');
    
    sidebar.classList.toggle('active');
    overlay.classList.toggle('active');
    hamburger.classList.toggle('active');
}

function closeSidebar() {
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('sidebarOverlay');
    const hamburger = document.getElementById('hamburgerMenu');
    
    sidebar.classList.remove('active');
    overlay.classList.remove('active');
    hamburger.classList.remove('active');
}

function showPlaceholder(option) {
    alert(`${option} - Esta funcionalidade estará disponível em breve.`);
    closeSidebar();
}

// Fechar sidebar ao pressionar ESC
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        closeSidebar();
    }
});


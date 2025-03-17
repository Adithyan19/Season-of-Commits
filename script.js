document.addEventListener('DOMContentLoaded', () => {
    const sidebar = document.getElementById('sidebar');
    
    // Sidebar hover effect
    sidebar.addEventListener('mouseenter', () => {
        sidebar.classList.remove('collapsed');
    });

    sidebar.addEventListener('mouseleave', () => {
        sidebar.classList.add('collapsed');
    });

    // Mobile sidebar toggle
    function toggleMobileSidebar() {
        sidebar.classList.toggle('active');
    }

    // Responsive sidebar handling
    function handleResponsiveSidebar() {
        if (window.innerWidth <= 768) {
            sidebar.classList.add('collapsed');
            sidebar.removeEventListener('mouseenter', sidebarHoverHandler);
            sidebar.removeEventListener('mouseleave', sidebarHoverHandler);
        } else {
            sidebar.addEventListener('mouseenter', sidebarHoverHandler);
            sidebar.addEventListener('mouseleave', sidebarHoverHandler);
        }
    }

    function sidebarHoverHandler() {
        sidebar.classList.toggle('collapsed');
    }

    // Initial responsive check
    handleResponsiveSidebar();
    window.addEventListener('resize', handleResponsiveSidebar);

    // Product card interaction
    function toggleProductDetails(card) {
        card.classList.toggle('expanded');
    }

    // Attach global method
    window.toggleProductDetails = toggleProductDetails;
});
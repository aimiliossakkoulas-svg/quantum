// Browse page JavaScript - Load and filter items
document.addEventListener('DOMContentLoaded', function() {
    const categoryFilter = document.getElementById('category-filter');
    const itemsContainer = document.getElementById('items-container');
    
    loadItems('all');
    
    categoryFilter.addEventListener('change', function(e) {
        loadItems(e.target.value);
    });
});

function loadItems(category) {
    const itemsContainer = document.getElementById('items-container');
    const url = `/api/items?category=${category}`;
    
    fetch(url)
        .then(response => response.json())
        .then(items => {
            if (items.length === 0) {
                itemsContainer.innerHTML = '<p class="empty-state">No items available right now. Check back soon!</p>';
                return;
            }
            
            itemsContainer.innerHTML = items.map(item => `
                <div class="item-card" onclick="goToItem(${item.id})">
                    <div class="item-header">
                        <h3>${item.name}</h3>
                        <span class="category-badge">${item.category}</span>
                    </div>
                    <p>${item.description || 'No description provided'}</p>
                    <p class="status available">✓ Available</p>
                </div>
            `).join('');
        })
        .catch(error => {
            console.error('Error loading items:', error);
            itemsContainer.innerHTML = '<p class="empty-state">Error loading items. Please try again.</p>';
        });
}

function goToItem(itemId) {
    window.location.href = `/item/${itemId}`;
}

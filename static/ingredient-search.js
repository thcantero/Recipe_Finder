
document.addEventListener('DOMContentLoaded', () => {
    const input = document.getElementById('ingredient-input');
    const suggestions = document.getElementById('suggestions');
    const form = document.getElementById('ingredient-form');
    let selectedIngredients = [];

    input.addEventListener('input', async () => {
        const query = encodeURIComponent(input.value.trim());

        if (query.length < 2) {
            suggestions.innerHTML = '';
            return;
        }

        const response = await fetch(`/autocomplete?q=${query}`);
        const data = await response.json();

        suggestions.innerHTML = '';
        data.forEach(ingredient => {
            const item = document.createElement('div');
            item.textContent = ingredient.name;
            item.classList.add('suggestion-item', 'p-2', 'border-bottom');
            item.style.cursor = 'pointer';

            item.addEventListener('click', () => {
                if (!selectedIngredients.includes(ingredient.name)) {
                    selectedIngredients.push(ingredient.name);
                }
                input.value = '';
                suggestions.innerHTML = '';
                displaySelected();
            });

            suggestions.appendChild(item);
        });
    });

    function displaySelected() {
        const display = selectedIngredients.map(i => `<span class="badge bg-secondary mx-1">${i}</span>`).join('');
        suggestions.innerHTML = `<p>Selected Ingredients:</p>${display}`;
    }

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        if (selectedIngredients.length > 0) {
            const queryStr = selectedIngredients.join(',');
            window.location.href = `/recipe/${encodeURIComponent(queryStr)}`;
        } else {
            alert('Please select at least one ingredient.');
        }
    });
});
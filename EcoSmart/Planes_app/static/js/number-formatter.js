// Parsear números al estilo español
function parseSpanishNumber(text) {
    // Remover separadores de miles y cambiar separador decimal
    const cleaned = text.replace(/\./g, '').replace(',', '.');
    return parseFloat(cleaned);
}

// Formatear números al estilo español
function formatSpanishNumber(number) {
    const num = parseFloat(number);
    const isWhole = num % 1 === 0;
    return new Intl.NumberFormat('es-ES', {
        minimumFractionDigits: isWhole ? 0 : 2,
        maximumFractionDigits: 2
    }).format(num);
}

// Formatear todos los elementos con clase 'format-currency'
document.addEventListener('DOMContentLoaded', function() {
    const elements = document.querySelectorAll('.format-currency');
    elements.forEach(element => {
        const text = element.textContent.trim();
        const number = parseSpanishNumber(text);
        if (!isNaN(number)) {
            element.textContent = formatSpanishNumber(number);
        }
    });
});
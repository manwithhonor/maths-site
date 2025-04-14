// Получаем элементы со страницы
const counterElement = document.getElementById('counter');
const incrementBtn = document.getElementById('incrementBtn');

// Начальное значение счетчика
let count = 0;

// Функция для обновления счетчика на странице
function updateCounter() {
    counterElement.textContent = count;
}

// Обработчик клика по кнопке
incrementBtn.addEventListener('click', function() {
    count++; // Увеличиваем счетчик на 1
    updateCounter(); // Обновляем отображение

    // Дополнительный эффект (необязательно)
    counterElement.style.transform = 'scale(1.2)';
    setTimeout(() => {
        counterElement.style.transform = 'scale(1)';
    }, 200);
});

// Инициализация счетчика при загрузке
updateCounter();
// Функция смены изображения
function changeImage(newSrc) {
    var mainImage = document.getElementById("mainImage");
    mainImage.src = newSrc;  // Меняем изображение на выбранное
    localStorage.setItem("selectedImage", newSrc);  // Сохраняем выбранное изображение в localStorage
}

// При загрузке страницы проверяем, есть ли сохранённое изображение
window.onload = function() {
    var savedImage = localStorage.getItem("selectedImage");
    if (savedImage) {
        document.getElementById("mainImage").src = savedImage;  // Загружаем сохранённое изображение
    } else {
        // Если нет сохранённого изображения, установите изображение по умолчанию
        var defaultImage = document.getElementById("mainImage");
        defaultImage.src = defaultImage.getAttribute('data-default');  // data-default — это атрибут с изображением по умолчанию
    }
}

// Для кнопок перехода между карточками, очищайте старое изображение из localStorage
function clearStoredImage() {
    localStorage.removeItem("selectedImage");  // Очищаем сохранённое изображение, если переходим на новую карточку
}

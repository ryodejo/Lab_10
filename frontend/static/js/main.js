// Открытие и закрытие модального окна теста
function openModal() {
  document.getElementById("modal").classList.remove("hidden");
}
function closeModal() {
  document.getElementById("modal").classList.add("hidden");
}

// Открытие и закрытие логина
function openLoginModal() {
  document.getElementById("loginModal").classList.remove("hidden");
}
function closeLoginModal() {
  document.getElementById("loginModal").classList.add("hidden");
}

// Открытие и закрытие регистрации
function openSignUpModal() {
  document.getElementById("signUpModal").classList.remove("hidden");
}
function closeSignUpModal() {
  document.getElementById("signUpModal").classList.add("hidden");
}

// Проверка логина (пока просто заглушка, Django это делает сам)
let isLoggedIn = false;

// Основная логика — обработка кнопок "Take Test"
document.addEventListener("DOMContentLoaded", function () {
  const takeTestButtons = document.querySelectorAll(".take-test");

  takeTestButtons.forEach(button => {
    button.addEventListener("click", function (event) {
      if (!isLoggedIn) {
        event.preventDefault();

        // Установка поля next в форме логина
        const nextInput = document.getElementById("login-next");
        if (nextInput) {
          nextInput.value = this.getAttribute("href"); // путь к тесту
        }

        openLoginModal(); // Показываем модалку логина
      }
    });
  });
});

let contact_manipulation_button = document.querySelector(".contact_manipulation_button")

contact_manipulation_button.addEventListener("click", function () {
    let operation = contact_manipulation_button.dataset.operation
    let url = "/contact_manipulation/" + contact_manipulation_button.dataset.id + "/" + operation
    let xhr = new XMLHttpRequest()
    xhr.open('GET', url, true);
    xhr.send();

    if (operation == "remove"){
        contact_manipulation_button.dataset.operation = "add"
        contact_manipulation_button.textContent = "Добавить в контакты"
    }

    else{
        contact_manipulation_button.dataset.operation = "remove"
        contact_manipulation_button.textContent = "Удалить из контактов"
    }
})
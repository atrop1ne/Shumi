let card_buttons = document.querySelectorAll(".card_button")

card_buttons.forEach(button =>
    card_add_behavior(button, button.classList[1])) // Button 2nd class = button context

function card_add_behavior(button, button_context) {
    const card_face = button.parentElement.parentElement
    const card_content = card_face.querySelector(".card_content")
    const card_images = card_face.querySelector(".card_images")
    const card_text_content = card_face.querySelector(".card_text_content")
    const card_description_hider = card_text_content.querySelector(".card_description_hider")

    card_content.addEventListener("click", function () {
        card_face.classList.toggle("card_content_full")
        card_content.classList.toggle("card_content_full")
        card_text_content.classList.toggle("card_content_full")
        card_images.classList.toggle("card_images_full")
        card_images.querySelectorAll("div, img").forEach(child => {
            child.classList.toggle("card_images_full")
        })
        // childs = card_images.childNodes
        // card_images.childNodes.forEach(child => {
        //     child.classList.toggle(".card_images_full")
        // })
        card_description_hider.classList.toggle("card_description_hider_hide")
    })

    button.addEventListener("click", function () {
        card_face.classList.add(button_context + "_clicked")

        let url = "/card_to_archive/" + card_face.dataset.id + "/" + button_context
        let xhr = new XMLHttpRequest()
        xhr.open('GET', url, true);
        xhr.send();

        card_on_delete(card_face)

        //CARD MESSAGE BEHAVIOR

        // if (button_context != "message") {
        //     card_on_delete(card_underlay)
        // }
    })
}

function card_on_delete(card_face) {
    const scrollIntoViewParams = {
        behavior: "smooth",
        block: "center"
    }

    if (card_face.nextElementSibling) {
        card_face.nextElementSibling.scrollIntoView(scrollIntoViewParams)
    }

    else if (card_face.previousElementSibling) {
        card_face.previousElementSibling.scrollIntoView(scrollIntoViewParams)
    }

    setTimeout(() => {
        card_face.remove()
    }, 600)
}
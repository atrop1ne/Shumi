let card_buttons = document.querySelectorAll(".card_button")

card_buttons.forEach(button =>
    card_add_behavior(button, button.classList[1])) // Button 2nd class = button context

function card_add_behavior(button, button_context) {
    const card_face = button.parentElement.parentElement
    const card_content = card_face.querySelector(".card_content")
    const card_images = card_face.querySelector(".card_images")
    const card_text_content = card_face.querySelector(".card_text_content")

    card_content.addEventListener("click", function () {
        card_face.classList.toggle("card_content_full")
        card_content.classList.toggle("card_content_full")
        card_images.classList.toggle("card_content_full")
        card_text_content.classList.toggle("card_content_full")
    })

    button.addEventListener("click", function () {
        card_face.classList.add(button_context + "_clicked")

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
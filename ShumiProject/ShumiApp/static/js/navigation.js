let nav_elements = document.querySelectorAll(".nav_element")

nav_elements.forEach(nav_element => {
    let nav_button = nav_element.querySelector(".nav_button")
    let nav_description = nav_element.querySelector(".nav_button_description")

    nav_button.addEventListener("mouseover", function () { //Add hover on mouseover
        nav_description.classList.add("nav_button_description_hovered")
    })

    nav_button.addEventListener("mouseout", function () { //Add hover on mouseout
        nav_description.classList.remove("nav_button_description_hovered")
    })
})
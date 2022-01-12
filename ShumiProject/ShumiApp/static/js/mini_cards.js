let card_manipulation_buttons = document.querySelectorAll(".card_manipulation")

card_manipulation_buttons.forEach(card_manipulation_button => {
    card_manipulation_button.addEventListener("click", function(){

        card_manipulation_buttons.forEach(card_manipulation_button => {
            card_manipulation_button.classList.remove("card_more_options_container_visible")
        })

        let container = card_manipulation_button.parentElement.querySelector(".card_more_options_container")
        container.classList.toggle("card_more_options_container_visible")

        let button_context = card_manipulation_button.querySelector(".card_more")

        if(container.classList.contains("card_more_options_container_visible")){
            button_context.textContent = "close"
        }

        else{
            button_context.textContent = "more_vert"
        }

        let options_behaviour_added = false
        let options = container.querySelectorAll(".card_more_option")
        if(!options_behaviour_added){
            options.forEach(option => {
                option.addEventListener("click", function(){
                    let url =  `/${option.dataset.url}/${container.dataset.id}`
                    if(option.dataset.url == "card_to_archive"){
                        url += "/no"
                    }
                    let xhr = new XMLHttpRequest()
                    xhr.open('GET', url, true);
                    xhr.send();
                    card_manipulation_button.parentNode.remove()
                })
            })

            options_behaviour_added = true
        }
    })  
})
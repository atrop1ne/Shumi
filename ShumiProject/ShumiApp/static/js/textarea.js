let textareas = document.querySelectorAll('textarea')
let current_symbol_count = 0
let symbol_count = 0
let counts = [0]

textareas.forEach(textarea => {
    textarea.addEventListener('keydown', function(){
        current_symbol_count += 1
        if(this.scrollTop > 0){
          this.style.height = this.scrollHeight + "px"
        }
      })
})
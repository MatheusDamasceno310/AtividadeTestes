$('.navTrigger').click(function () {
    $(this).toggleClass('active');
    console.log("Clicked menu");
    $("#mainListDiv").toggleClass("show_list");
    $("#mainListDiv").fadeIn();

});

// Seleciona o elemento da div
const divMensagens = document.querySelector('.contMsg');

// Define a função para remover a div após 5 segundos
const removerDiv = () => {
    divMensagens.remove();
}

// Define o atraso de 5 segundos e chama a função de remover a div
setTimeout(removerDiv, 5000);

 $(window).scroll(function() {
            if ($(document).scrollTop() > 50) {
                $('.nav').addClass('affix');
                console.log("OK");
            } else {
                $('.nav').removeClass('affix');
            }
        });

 // Recupera o modo atual do armazenamento local, se disponível
const isDarkMode = localStorage.getItem("isDarkMode");

// Verifica se o modo escuro está habilitado no armazenamento local
if (isDarkMode === "true") {
  document.documentElement.classList.add("dark-mode");
}

// Recupera o ícone atual do armazenamento local, se disponível
const currentIcon = localStorage.getItem("currentIcon");

// Define o ícone padrão como o ícone claro
let iconSrc = "{{ url_for('static', filename='imagens/claro.png') }}";

// Verifica se o ícone escuro está selecionado no armazenamento local
if (currentIcon === "dark") {
  iconSrc = "{{ url_for('static', filename='imagens/claro.png') }}";
}

// Define o ícone no HTML
const icon = document.getElementById("icon");
icon.setAttribute("src", iconSrc);

function toggleDarkMode() {
  const html = document.documentElement;
  html.classList.toggle("dark-mode");

  // Salva o modo atual no armazenamento local
  const isDarkMode = html.classList.contains("dark-mode");
  localStorage.setItem("isDarkMode", isDarkMode);

  // Salva o ícone atual no armazenamento local
  let currentIcon = "light";
  if (html.classList.contains("dark-mode")) {
    currentIcon = "dark";
  }
  localStorage.setItem("currentIcon", currentIcon);

  // Alterna entre os ícones com animação
  icon.classList.toggle("animate-icon");
  setTimeout(() => {
    if (icon.getAttribute("src") === "{{ url_for('static', filename='imagens/modo-escuro.png') }}") {
      icon.setAttribute("src", "{{ url_for('static', filename='imagens/claro.png') }}");
    } else {
      icon.setAttribute("src", "{{ url_for('static', filename='imagens/modo-escuro.png') }}");
    }
    icon.classList.toggle("animate-icon");
  }, 300);
}


//* Filtrar Jogos//

let list = document.querySelectorAll('.list');
let card = document.querySelectorAll('.card');

for (let i = 0; i<list.length; i++){
  list[i].addEventListener('click', function(){
    for(let j=0; j<list.length; j++){
      list[j].classList.remove('active');
    }
    this.classList.add('active');

    let dataFilter = this.getAttribute('data-filter');

    for( let k=0; k<card.length; k++)
    {
      card[k].classList.remove('active');
      card[k].classList.add('hide');

      if(card[k].getAttribute('data-item') == dataFilter || dataFilter == 'all'){
        card[k].classList.remove('hide');
        card[k].classList.add('active');
      }
    }
  })
}


// Seleciona o link do carrinho e a mini janela do carrinho
const carrinhoLink = document.getElementById("carrinho-link");
const carrinhoModal = document.getElementById("carrinho-modal");

// Adiciona um ouvinte de eventos ao link do carrinho
carrinhoLink.addEventListener("click", function(e) {
    // Impede que o link funcione como um link normal
    e.preventDefault();

    // Exibe a mini janela do carrinho
    carrinhoModal.style.display = "block";
});

// Seleciona o link da conta e a mini janela da conta
const contaLink = document.getElementById("conta-link");
const contaModal = document.getElementById("conta-modal");

// Adiciona um ouvinte de eventos ao link da conta
contaLink.addEventListener("click", function(e) {
    // Impede que o link funcione como um link normal
    e.preventDefault();

    // Exibe a mini janela da conta
    contaModal.style.display = "block";
});

// Seleciona todos os botões "Fechar"
const closeButton = document.querySelectorAll(".modal-close");

// Adiciona um ouvinte de eventos a cada botão "Fechar"
closeButton.forEach(function(button) {
    button.addEventListener("click", function() {
        // Oculta a mini janela
        this.parentNode.parentNode.style.display = "none";
    });
});

//Scroll automatico//
    document.querySelector('a[href="#games"]').addEventListener('click', function(e) {
        e.preventDefault(); // evita o comportamento padrão do link
        document.querySelector('#games').scrollIntoView({ behavior: 'smooth' });
    });


    document.querySelector('a[href="#topo"]').addEventListener('click', function(e) {
        e.preventDefault(); // evita o comportamento padrão do link
        document.querySelector('#topo').scrollIntoView({ behavior: 'smooth' });
    });


    // Adiciona a classe "animate" quando a div estiver visível
window.addEventListener("scroll", function() {
  var animatedDiv = document.querySelector(".animated-div");
  var position = animatedDiv.getBoundingClientRect();

  if (position.top < window.innerHeight && position.bottom >= 0) {
    animatedDiv.classList.add("animate");
  }
});

window.addEventListener("scroll", function() {
  var animatedDiv = document.querySelector(".animated-div2");
  var position = animatedDiv.getBoundingClientRect();

  if (position.top < window.innerHeight && position.bottom >= 0) {
    animatedDiv.classList.add("animate");
  }
});







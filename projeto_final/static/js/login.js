// Seleciona o elemento da div
const divMensagens = document.querySelector('.contMsg');

// Define a função para remover a div após 5 segundos
const removerDiv = () => {
    divMensagens.remove();
}

// Define o atraso de 5 segundos e chama a função de remover a div
setTimeout(removerDiv, 5000);

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
// Seleciona o elemento da div
const divMensagens = document.querySelector('.contMsg');

// Define a função para remover a div após 5 segundos
const removerDiv = () => {
    divMensagens.remove();
}

// Define o atraso de 5 segundos e chama a função de remover a div
setTimeout(removerDiv, 5000);


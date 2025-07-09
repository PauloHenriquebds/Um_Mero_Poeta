# 🌙 Um Mero Poeta — Site de Poesias

Este é um projeto simples e poético de site pessoal com foco em **poesias autorais**, desenvolvido com HTML, CSS e um script Python auxiliar.

---

## 🖼️ Visão Geral

A página principal (`index.html`) exibe uma série de poemas distribuídos em seções estilizadas, com design responsivo e fundo com imagem. O projeto visa oferecer uma leitura agradável em diversos dispositivos.

---

## 📁 Estrutura do Projeto

```
Nova pasta - Copia/
├── index.html       # Página com os poemas
├── style.css        # Estilo visual com responsividade
├── main.py          # Script Python para organização de arquivos
└── .git/            # Repositório Git
```

---

## 💡 Destaques do Projeto

### 📄 `index.html`

- Contém 8 poemas autorais organizados em `<section class="poema">`.
- Cabeçalho com título e navegação:
  - Link para próxima página.
  - Link para Instagram pessoal.
- Rodapé com menu repetido e crédito do autor.

### 🎨 `style.css`

- Design com **Flexbox** e **media queries**.
- Fundo com imagem (`IMG_20240919_204437_038.jpg`).
- Poemas com estilo suave em fundo azul escuro e texto cinza claro.
- Totalmente **responsivo** para tablets e celulares.

### 🐍 `main.py`

- Script para organizar arquivos automaticamente por extensão em subpastas.
- Exclui arquivos `.py` e `.ipynb` da organização.

---

## 📱 Responsividade

Adapta-se automaticamente a diferentes tamanhos de tela:

- `@media (max-width: 768px)` reorganiza menus e reduz margens.
- `@media (max-width: 480px)` ajusta tamanhos de fonte e paddings.

---

## 📷 Pré-visualização (recomendada)

Abra `index.html` em seu navegador para visualizar os poemas com o layout responsivo.

---

## 🧪 Como Executar

### Visualização do site:

1. Extraia o ZIP.
2. Abra o arquivo `index.html` em qualquer navegador.

### Organização de arquivos com Python:

```bash
python main.py
```

> O script criará uma pasta `arquivos/` com subpastas por extensão (exceto `.py` e `.ipynb`).

---

## 📜 Autor

Desenvolvido por **Paulo Henrique (P.H.)**  
📸 [Instagram](https://www.instagram.com/paulo_hds_/)

---

## 📄 Licença

Uso pessoal e educacional liberado. Dê os créditos se for compartilhar!

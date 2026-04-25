// THEME
const toggle = document.getElementById('themeToggle');

toggle.addEventListener('click', () => {
    document.body.classList.toggle('light');

    toggle.innerHTML =
        document.body.classList.contains('light')
        ? '<i class="fa-solid fa-sun"></i>'
        : '<i class="fa-solid fa-moon"></i>';
});


// COPY + EDIT per card
document.querySelectorAll('.history-card').forEach(card => {

    const post = card.querySelector('.history-post');
    const copyBtn = card.querySelector('.copyBtn');
    const editBtn = card.querySelector('.editBtn');

    // COPY
    copyBtn.addEventListener('click', () => {
        navigator.clipboard.writeText(post.innerText);

        copyBtn.classList.add('copied');
        copyBtn.innerHTML = '<i class="fa-solid fa-check"></i>';

        setTimeout(() => {
            copyBtn.classList.remove('copied');
            copyBtn.innerHTML = '<i class="fa-regular fa-copy"></i>';
        },1000);
    });

    // EDIT
    editBtn.addEventListener('click', () => {
        post.contentEditable = true;
        post.focus();
    });

});
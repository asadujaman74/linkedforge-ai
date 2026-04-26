// const post = document.getElementById('generatedPost');
// const copyBtn = document.getElementById('copyBtn');
// const editBtn = document.getElementById('editBtn');
// const toggle = document.getElementById('themeToggle');

// // COPY + TICK
// copyBtn.addEventListener('click', () => {
//     navigator.clipboard.writeText(post.innerText);

//     copyBtn.classList.add('copied');
//     copyBtn.innerHTML = '<i class="fa-solid fa-check"></i>';

//     setTimeout(()=>{
//         copyBtn.classList.remove('copied');
//         copyBtn.innerHTML = '<i class="fa-regular fa-copy"></i>';
//     },1000);
// });

// // EDIT
// editBtn.addEventListener('click', () => {
//     post.contentEditable = true;
//     post.focus();
// });

// // DARK / LIGHT
// toggle.addEventListener('click', () => {
//     document.body.classList.toggle('light');

//     toggle.innerHTML = document.body.classList.contains('light')
//         ? '<i class="fa-solid fa-sun"></i>'
//         : '<i class="fa-solid fa-moon"></i>';
// });




const toggle = document.getElementById('themeToggle');

/* =========================
 THEME TOGGLE (SAFE)
========================= */
if (toggle) {
    toggle.addEventListener('click', () => {
        document.body.classList.toggle('light');

        toggle.innerHTML = document.body.classList.contains('light')
            ? '<i class="fa-solid fa-sun"></i>'
            : '<i class="fa-solid fa-moon"></i>';
    });
}

/* =========================
 COPY BUTTON (SAFE)
========================= */
const copyBtn = document.getElementById('copyBtn');
const post = document.getElementById('generatedPost');

if (copyBtn && post) {
    copyBtn.addEventListener('click', () => {
        navigator.clipboard.writeText(post.innerText);

        copyBtn.classList.add('copied');
        copyBtn.innerHTML = '<i class="fa-solid fa-check"></i>';

        setTimeout(() => {
            copyBtn.classList.remove('copied');
            copyBtn.innerHTML = '<i class="fa-regular fa-copy"></i>';
        }, 1000);
    });
}

/* =========================
 EDIT BUTTON (SAFE)
========================= */
const editBtn = document.getElementById('editBtn');

if (editBtn && post) {
    editBtn.addEventListener('click', () => {
        post.contentEditable = true;
        post.focus();
    });
}
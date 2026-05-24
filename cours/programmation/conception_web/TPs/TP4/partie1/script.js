document.addEventListener("DOMContentLoaded", function () {
  const sections = document.querySelectorAll(".articles section");

  sections.forEach(function (section) {
    const pArticle = section.querySelector(".pArticle");
    const btnDisplayArticle = section.querySelector(".btnDisplayArticle");

    if (!pArticle || !btnDisplayArticle) {
      return;
    }

    btnDisplayArticle.addEventListener("click", function (event) {
      event.preventDefault();
      const articleVisible = pArticle.style.display === "block";

      if (articleVisible) {
        pArticle.style.display = "none";
        btnDisplayArticle.textContent = "(Cliquer ici pour lire la suite)";
      } else {
        pArticle.style.display = "block";
        btnDisplayArticle.textContent = "Masquer";
      }
    });
  });
});

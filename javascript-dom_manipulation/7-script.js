function getMovieTitles() {
    fetch("https://swapi-api.hbtn.io/api/films/?format=json")
    .then(response => response.json())
    .then(data => {
        const movies = data.results;
        const ulElement = document.getElementById("list_movies");
        movies.forEach(movie => {
            const liElement = document.createElement("li");
            liElement.textContent = movie.title;
            ulElement.appendChild(liElement);
            
        });
    })
    .catch(error => {
        console.error("Case:", error);
});
}
getMovieTitles();

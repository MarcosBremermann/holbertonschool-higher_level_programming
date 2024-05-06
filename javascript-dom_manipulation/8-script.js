fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
  .then((response) => response.json())
  .then((data) => {
    const hellosalut = data.hello;
    const elementHello = document.getElementById("hello");
    elementHello.innerText = hellosalut;
  })
  .catch((error) => {
    console.error("Error fetching data", error);
  });

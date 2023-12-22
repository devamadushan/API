let divPays=document.querySelector("#lesPays")
let inputrecherche= document.querySelector("#recherchePays")

async function fetchPays(url){
    let reponse= await fetch(url)
    let data = await reponse.json()
    return data
}

fetchPays("https://restcountries.com/v3.1/all").then(function (dataPays){
    for (const lePays of dataPays) {
        console.log(lePays)
       divPays.innerHTML+=affichePays(lePays)+"<br>"
    }
})

function affichePays(lePays){
    return `<div class="col my-2"><div class="card" style="width: 18rem;">
    <img src="${lePays.flags.png}" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title">${lePays.name.common}</h5>
      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
      <a href="#" class="btn btn-primary">Go somewhere</a>
    </div>
  </div>
  </div>`
}

inputrecherche.addEventListener("keyup",function(){
    divPays.innerHTML=""
    fetchPays("https://restcountries.com/v3.1/name/"+inputrecherche.value).then(function (dataPays){
        for (const lePays of dataPays) {
            console.log(lePays)
           divPays.innerHTML+=affichePays(lePays)+"<br>"
        }
    })
})
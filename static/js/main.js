//Search form and page links
let searchForm = document.getElementById('searchForm')
let pageLinks = document.getElementsByClassName('page-link')

if (searchForm)
{
  for (let i = 0; i < pageLinks.length; i++) 
  {
    pageLinks[i].addEventListener('click', function (e) {
      e.preventDefault()

      //Getting Data Attribute
      let page = this.dataset.page

      //Adding search query to html
      searchForm.innerHTML += `<input value=${page} name="page" hidden />`

      //Submitting
      searchForm.submit()
    })
    
  }
}
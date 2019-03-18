document.getElementById('rate').addEventListener('click', like);

function like() {
   var xhr = new XMLHttpRequest();

   xhr.open('POST', 'rate/', true);

   xhr.onload = function(){
      if(this.status==200){
         var user = JSON.parse(this.responseText)

         console.log(user)
      } else {
         console.log('Couldn\'t fetch the data.')
      }
   }
   
   xhr.send();
}
// Author : Emily Mo
// Date : Jul 15, 2019
// Javascript : handling of a hand of tiles
//
//

// should be every time when a tile is retrieved
var resequence = " ";
var winner = false;

function getRndInteger(min, max) {
  return Math.floor(Math.random() * (max - min + 1) ) + min;
}



var first_round = document.querySelector(".info_4").innerHTML
if (first_round == "first") {
    resequence = document.getElementById('resequence').innerHTML;
    document.querySelector(".info_4").innerHTML ='notfirst'
    console.log('resequence', resequence);
 //   win = d3.select("#win").style("visibility", "hidden");
 //   dice = d3.select("#dice").style("visibility", "hidden");
 //   crack = d3.select("#crack").style("visibility", "visible");
 //   source = d3.select("#source").style("visibility", "hidden");
 //   working_space = d3.select("#working_space").style("visibility", "hidden");
         
}
   

//roll 3 dice - between 3 and 18
var crack = d3.select("#crack");

crack.on("click", function() {

  // Prevent the page from refreshing
      d3.event.preventDefault();
      console.log('crack');
//      var roll = getRndInteger(3, 18);    
//      console.log('roll:', roll);  
//      var url = "/crack/"+roll;
//      d3.json(url).then(function(start) {
//        console.log('crack - roll and start:', roll, start);
//        win = d3.select("#win").style("visibility", "visible");
//        dice = d3.select("#dice").style("visibility", "visible");
//        dice_text = 'Dice : "+roll;
//        dice = d3.select("#dice").text(dice_text);
//        crack = d3.select("#crack").style("visibility", "hidden");
//        source = d3.select("#source").style("visibility", "visible");
//        working_space = d3.select("#working_space").style("visibility", "visible");
         
     
//    })
})


//declare to win
var win = d3.select("#win");

win.on("click", function() {

  // Prevent the page from refreshing
      d3.event.preventDefault();
      console.log('win');
      winner = true;

})

//undo - restart to resequence tiles 
var undo = d3.select("#undo");

undo.on("click", function() {

  // Prevent the page from refreshing
      d3.event.preventDefault();
      console.log('undo')
 
      var seq = document.getElementById('resequence').innerHTML;
      var seq_node = document.getElementById('resequence');
      console.log('seq', seq);
      if (seq) {
        seq_node.innerHTML="";
        seq_node.innerHTML = resequence;  
      console.log('re: ', resequence);    
  }      
    
    
//      document.getElementById('resequence')= resequence;
//       document.replaceChild(new, old)
    
    
})



function allowDrop(ev) {
  ev.preventDefault();
}
        
function drag(ev) {
  ev.dataTransfer.setData("text", ev.target.id);
}
        
function drop(ev) {

    ev.preventDefault();
   
  var data = ev.dataTransfer.getData("text");
  ev.target.appendChild(document.getElementById(data));
  console.log('data', data); 
  var parent_id = document.getElementById(data).parentElement.id;
  console.log('parent_id', parent_id);  
  if (parent_id == 'dump') {
      
      var removed_item = document.getElementById(data);  
      if (removed_item) {
          removed_item.remove();
          console.log('removed item', removed_item); 
      }
  }
    
}

   
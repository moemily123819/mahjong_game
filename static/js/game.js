// Author : Emily Mo
// Date : Jul 15, 2019
// Javascript : handling of a hand of tiles
//
//


sticks =[];
sticks.push('images/stick_1.PNG');
sticks.push('images/stick_2.PNG');
sticks.push('images/stick_3.PNG');
sticks.push('images/stick_4.PNG');
sticks.push('images/stick_5.PNG');
sticks.push('images/stick_6.PNG');
sticks.push('images/stick_7.PNG');
sticks.push('images/stick_8.PNG');
sticks.push('images/stick_9.PNG');

mans =[];
mans.push('images/man_1.PNG');
mans.push('images/man_2.PNG');
mans.push('images/man_3.PNG');
mans.push('images/man_4.PNG');
mans.push('images/man_5.PNG');
mans.push('images/man_6.PNG');
mans.push('images/man_7.PNG');
mans.push('images/man_8.PNG');
mans.push('images/man_9.PNG');

circles =[];
circles.push('images/circle_1.PNG');
circles.push('images/circle_2.PNG');
circles.push('images/circle_3.PNG');
circles.push('images/circle_4.PNG');
circles.push('images/circle_5.PNG');
circles.push('images/circle_6.PNG');
circles.push('images/circle_7.PNG');
circles.push('images/circle_8.PNG');
circles.push('images/circle_9.PNG');


winds = [];
winds.push('images/east.PNG');
winds.push('images/south.PNG');
winds.push('images/west.PNG');
winds.push('images/north.PNG');
winds.push('images/center.PNG');
winds.push('images/fortune.PNG');
winds.push('images/paa.PNG');

flowers = [];
flowers.push('images/flowera_1.PNG');
flowers.push('images/flowera_2.PNG');
flowers.push('images/flowera_3.PNG');
flowers.push('images/flowera_4.PNG');
flowers.push('images/flowerb_1.PNG');
flowers.push('images/flowerb_2.PNG');
flowers.push('images/flowerb_3.PNG');
flowers.push('images/flowerb_4.PNG');


// should be every time when a tile is retrieved
var resequence = " ";

var first_round = document.querySelector(".info_4").innerHTML
if (first_round == "first") {
    resequence = document.getElementById('resequence').innerHTML;
    document.querySelector(".info_4").innerHTML ='notfirst'
    console.log('resequence', resequence);
}
   

function getRndInteger(min, max) {
  return Math.floor(Math.random() * (max - min + 1) ) + min;
}


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
    
    
})

//confirm - tile discarded
var confirm = d3.select("#confirm");

confirm.on("click", function() {

  // Prevent the page from refreshing
      d3.event.preventDefault();
      console.log('confirm');
      var discard_tile = localStorage.getItem("removed");
      var url = "/discard/"+discard_tile;
      d3.json(url).then(function(status) {
        console.log('status:', statue);
 
    
})

//confirm - tile discarded
var crack = d3.select("#crack");

crack.on("click", function() {

  // Prevent the page from refreshing
      d3.event.preventDefault();
      console.log('crack');
      var roll = getRndInteger(3, 18);       
      var url = "/crack/"+roll;
      d3.json(url).then(function(start) {
        console.log('crack - roll and start:', roll, start);
     
    })
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
          localStorage.clear();
          localStorage.setItem("removed", removed_item);

      }
  }
    
}

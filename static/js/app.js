// Author : Emily Mo
// Date : Jul 4, 2019
// Javascript : to receive user input and pwd...then start playing mahjong
//
//


// clear error message

function clear_err_msg() {

    
   var userinput = d3.select('#user').text("")
    
   var newUserinput = d3.select('#newUser').text("")
    
   var pwdinput = d3.select('#pwd').text("")
    
   var newPwdinput = d3.select('#newPwd').text("")
    
   var userinput = d3.select('#user').text("")
   
    var err_msg = d3.select('.err-msg-1')
       .classed("hidden", true);
   if (!err_msg.empty()) {
          err_msg.remove();
        }
    
    
   err_msg = d3.select('.err-msg-2')
       .classed("hidden", true);
   if (!err_msg.empty()) {
          err_msg.remove();
        }
    
   err_msg = d3.select('.err-msg-3')
       .classed("hidden", true);
   if (!err_msg.empty()) {
          err_msg.remove();
        }
    
   err_msg = d3.select('.err-msg-4')
       .classed("hidden", true);
   if (!err_msg.empty()) {
          err_msg.remove();
        }
    
  
}    



// screen the screen of the previous results 

function clear_screen() {

    
    var users = d3.select('#user')
       .attr("text", " ");
  
   try {  
     var end_results = d3.select('#my_hand').selectAll('h5');
     if (!end_results.empty()) {
          end_results.remove();
        }

   }
   catch(err) {
     console.log('no h5');   
   }    
       
   var my_hand = d3.select('.my_hand')
       .classed("hidden", true);
  
   try {  
     var end_results = d3.select('#my_hand').selectAll('h5');
     if (!end_results.empty()) {
          end_results.remove();
        }

   }
   catch(err) {
     console.log('no h5');   
   }    
       
}    




// when reset


var reset = d3.select("#reset");
console.log('reset', reset);


reset.on("click", function() {

  // Prevent the page from refreshing
  d3.event.preventDefault();
  console.log('function - reset starts');
    
  clear_err_msg()

})    



var submit = d3.select("#login");
console.log('submit');

submit.on("click", function() {

  // Prevent the page from refreshing
  d3.event.preventDefault();
  console.log('function - submit starts');
  
  var user = d3.select("#user")
  var existing_user = user.property("value");
  var pwd = d3.select("#pwd")  
  var existing_pwd = pwd.property("value");
  var newUser = d3.select("#newUser")  
  var new_user = newUser.property("value");
  var newPwd = d3.select("#newPwd")  
  var new_pwd = newPwd.property("value");
  console.log('login :', existing_user, existing_pwd, new_user, new_pwd);
    
    
    
  d3.json("/send").then((login_status) =>{
           console.log('login_status :', login_status.user, login_status.login, login_status.error);
           l_status = login_status.login;
           l_user = login_status.user;
           l_error = login_status.error;
           location.replace("../play")
           console.log('login- success');
       
})
})    
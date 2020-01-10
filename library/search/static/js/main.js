/*
//get elements
const txtElementToken = document.getElementById("token");
const fileUpload = document.getElementById("upload");
const okButton = document.getElementById("clickok");

$("#upload").hide();
$(".no").hide();


let newItem = document.createElement("a");
newItem.id = id;
$('.content').prepend(newItem);
$('#'+id).addClass('itemee').text(file.name).attr("target", "_blank");
$('#pro'+id).toggle();


let newItem = document.createElement("a");
newItem.href = url;
let id = snapshot.val().link.split('/').pop().split('.')[0];
newItem.id = id;
$('.content').append(newItem);
$('#' + id).addClass('itemee').text(snapshot.val().name + '.' + snapshot.val().ext)
    .attr("target", "_blank");

txtElementToken.value = '';
$(".login").toggle();
$(".loading").toggle();


txtElementToken.onkeypress = keypress;
function keypress(e) {
  if (e.code === "Enter") {
    bruh();
  }
}

okButton.onclick = bruh;
*/
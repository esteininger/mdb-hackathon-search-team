// 1.
function callFromServer() {
  $.ajax({
    'url': "/load",
    'method': "GET"
  }).done(function(data) {
    forEachParse(data)
  })
}


$(document).ready(function() {
  callFromServer();
});

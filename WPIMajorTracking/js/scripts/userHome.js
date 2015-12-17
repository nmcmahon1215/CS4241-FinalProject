
function selectSheet(id){
  window.location.href = "/api/trackingsheet/" + id;
}

function deleteSheet(event, id){
  var realEvent = event || window.event;
  realEvent.stopPropagation();

  var req = new XMLHttpRequest();

  req.onreadystatechange = function() {
    if (req.readyState = XMLHttpRequest.DONE && req.status == 200){
      var elt = $('#' + id);

      elt.slideUp(500, function() {
        elt.remove();
      })
    }
  }

  req.open("DELETE", '/api/trackingsheet/' + id);
  req.send();

}
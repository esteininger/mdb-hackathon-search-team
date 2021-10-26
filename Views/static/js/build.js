// 1.
function initLoadDataButton() {
  $("#industrySelectionButton").click(function() {
    let industryValue = $('#industrySelectionDropdown').val();

    $.ajax({
      'url': `/ingest?industry=${industryValue}`,
      'method': "POST"
    }).done(function(data) {

      // aaron sample json
      let dataDictionary = [
        {
          'fieldIdentifier': "cardholderRewardCaps1",
          'addToSearchIndex': false,
          'dataType': 'UNSUPPORTED FOR NOW'
        },
        {
          'fieldIdentifier': "cardholderRewardCaps2",
          'addToSearchIndex': false,
          'dataType': 'UNSUPPORTED FOR NOW'
        }
    ]
      updateDataDictionary(dataDictionary)
    })
  });
}

function updateDataDictionary(dataDictionary) {
  var html = ``;
  dataDictionary.forEach(function(obj) {
    // console.log(obj)
    html += `<div class="form-check">
      <input class="form-check-input dataDictionaryCheckbox" type="checkbox" value="${obj['fieldIdentifier']}" id="${obj['fieldIdentifier']}">
      <label class="form-check-label" for="${obj['fieldIdentifier']}">
        ${obj['fieldIdentifier']}
      </label>
    </div>`
  });

  $('#data-dictionary').html(html)
  // init build index
  initBuildIndexButton();

}


function initBuildIndexButton(){
  $("#buildIndexButton").click(function() {

    var dataDictionary = [];

    var checkBoxes = $(".dataDictionaryCheckbox");
    checkBoxes.each(function() {
      console.log( this.value + ":" + this.checked );

      let d = {
        'fieldIdentifier': this.value,
        'addToSearchIndex': this.checked,
        'dataType': 'UNSUPPORTED FOR NOW'
      }
      dataDictionary.push(d)
    })

    // send to server
    $.ajax({
      'url': `/index`,
      'method': "POST",
      'dataType': "json",
      'data': dataDictionary,
      'contentType': "application/json"
    }).done(function(data) {
      console.log(data)
    })
  });
}


$(document).ready(function() {
  initLoadDataButton();
});

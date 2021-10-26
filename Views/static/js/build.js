// 1.
function initLoadDataButton() {
  $("#industrySelectionButton").click(function() {
    let industryValue = $('#industrySelectionDropdown').val();
    let loader = $('#loader');

    loader.html('<img src="../static/img/logo_title.png"/>')

    $.ajax({
      'url': `/ingest?industry=${industryValue}`,
      'method': "POST"
    }).done(function(data) {
      console.log(data)
      // aaron sample json
    //   let dataDictionary = [
    //     {
    //       'fieldIdentifier': "cardholderRewardCaps1",
    //       'addToSearchIndex': false,
    //       'dataType': 'UNSUPPORTED FOR NOW'
    //     },
    //     {
    //       'fieldIdentifier': "cardholderRewardCaps2",
    //       'addToSearchIndex': false,
    //       'dataType': 'UNSUPPORTED FOR NOW'
    //     }
    // ]
      updateDataDictionary(data)
      loader.html('');
    })
  });
}

function updateDataDictionary(dataDictionary) {
  var html = ``;
  dataDictionary.forEach(function(obj) {
    // console.log(obj)
    html += `<div class="form-check">
      <input class="form-check-input dataDictionaryCheckbox" type="checkbox" value="${obj['fieldIdentifier']}" id="${obj['fieldIdentifier']}" data-type=${obj['dataType']}>
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
        'dataType': $(this).data('type')
      }
      dataDictionary.push(d)
    })

    // send to server
    $.ajax({
      "url": `/index-creation?industry=${$('#industrySelectionDropdown').val()}`,
      "method": "POST",
      "headers": {
        "Content-Type": "application/json"
      },
      "data": JSON.stringify(dataDictionary)
    }).done(function(data) {
      console.log(data)
    })

  });
}

function runSearchQuery(){
  // search server
  $.ajax({
    "url": `/search`,
    "method": "GET",
    "headers": {
      "Content-Type": "application/json"
    },
    "data": JSON.stringify(dataDictionary)
  }).done(function(data) {
    console.log(data)
  })
}


$(document).ready(function() {
  initLoadDataButton();
});

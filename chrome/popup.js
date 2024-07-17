document.addEventListener('DOMContentLoaded', function() {
  var clickButton = document.getElementById('clickButton');
  clickButton.addEventListener('click', function() {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
      chrome.tabs.sendMessage(tabs[0].id, {action: 'clickButton'}, function(response) {
        if (chrome.runtime.lastError) {
          console.error(chrome.runtime.lastError.message);
        }
      });
    });
  });
});

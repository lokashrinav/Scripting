
document.addEventListener('DOMContentLoaded', function() {
  async function handleFileUpload() {
    let response = await fetch("https://drive.google.com/file/d/1DNIkFwmMZ85xp2GW0h5p4yb5stbMw6Sb/view?usp=sharing")
    response = await response.blob()
    let file = new File([response], "Jake_Resume.pdf");
    console.error(document.documentElement.outerHTML)
    let input = document.querySelector('[data-automation-id="file-upload-input-ref"]');
    let container = new DataTransfer();
    container.items.add(file)
    input.files = container.files
    alert("Hello")
  }
  
  chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
    if (message.action === 'clickButton') {
      handleFileUpload();
    }
  });
});

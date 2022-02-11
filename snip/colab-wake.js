/* Paste in Colab Console */
function Wake() {
  //console.log("Working");
  document.querySelector("colab-toolbar-button#connect").click()
}
setInterval(Wake, 60000)

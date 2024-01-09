function checkAnswer() {
  var answer = document.getElementById("answerTextarea").value.toLowerCase();
  
  if (answer === "kiwi kjeller") {
    document.getElementById("answerBox").style.display = "none";
    document.getElementById("newBox").style.display = "block";
  }
}

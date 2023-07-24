let recognition = new (window.SpeechRecognition ||
  window.webkitSpeechRecognition ||
  window.mozSpeechRecognition ||
  window.msSpeechRecognition)();
recognition.lang = "en-US";
recognition.interimResults = false;
recognition.maxAlternatives = 5;
recognition.lang = "en-US";
recognition.interimResults = false;
recognition.maxAlternatives = 5;

const recordButton = document.getElementById("record-Button");
const askButton = document.getElementById("ask-Button");
const audioElement = document.getElementById("audio-element");
const transcription = document.getElementById("transcript");

recordButton.addEventListener("mousedown", function () {
  transcript.textContent = "";
  recognition.start();
});

recordButton.addEventListener("mouseup", function () {
  recognition.stop();
});

//console.log("456");

recognition.addEventListener("result", function (event) {
  let last = event.results.length - 1;
  let text = event.results[last][0].transcript;

  let responseText = text;
  transcription.textContent = responseText;
});

askButton.addEventListener("click", function () {
  const message = transcript.value;
  const textData = { message: message };
  fetch("/ask", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(textData),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      document.getElementById("responseText").innerHTML = "";
      const audio = data.audio;
      audioElement.src = audio;
      audioElement.controls = true;
      audioElement.play();
      new TypeIt("#responseText", {
        strings: data.text,
        speed: 39,
        waitUntilVisible: false,
        cursorChar: "▊",
      }).go();
    });
});

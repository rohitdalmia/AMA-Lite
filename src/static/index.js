document.addEventListener('DOMContentLoaded', function() {
            const recordButton = document.getElementById('record-button');
            const transcriptionBox = document.getElementById('transcription-box');
            const askButton = document.getElementById('ask-button');
            const audioElement = document.getElementById('audio-element');

            askButton.addEventListener('click', function() {
                const message = transcriptionBox.value;
                const textData = { message: message };
                fetch('/ask', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(textData)
                })
                .then(response => {return response.json()})
                .then(data => {
                    const audio = data.audio;
                    audioElement.src = audio;
                    audioElement.controls = true;
                    audioElement.play();
                })
            });

            let chunks = [];
            let mediaRecorder = null;
            let isRecording = false;

            navigator.mediaDevices.getUserMedia({ audio: true })
            .then(stream => {
                mediaRecorder = new MediaRecorder(stream);
                mediaRecorder.ondataavailable = function(e) {
                    chunks.push(e.data);
                }

                mediaRecorder.onstop = function(e) {
                    const audioBlob = new Blob(chunks, { type: 'audio/mp3' });
                    const formData = new FormData();
                    formData.append('file', audioBlob, 'audio.mp3');

                    fetch('/transcribe', {
                        method: 'POST',
                        body: formData,
                    })
                    .then(response => response.json())
                    .then(data => {
                        console.log(data.text);
                        transcriptionBox.value = data.text;
                    })
                    .catch(error => {
                        console.error('Error:', error);
                    });
                };
            })
            .catch(error => {
                console.error('Error accessing the microphone:', error);
            });

            recordButton.addEventListener('click', function() {
                if (isRecording) {
                    mediaRecorder.stop();
                    isRecording = false;
                    recordButton.innerText = 'Start Recording';
                } else {
                    chunks = [];
                    mediaRecorder.start();
                    isRecording = true;
                    recordButton.innerText = 'Stop Recording';
                }
            });
        });
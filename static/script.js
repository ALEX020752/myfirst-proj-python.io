document.addEventListener('DOMContentLoaded', function() {
    var video = document.getElementById('myVideo');
    var playButton = document.getElementById('playButton');

    playButton.addEventListener('click', function() {
        if (video.paused) {
            video.play();
            playButton.textContent = 'Пауза';
        } else {
            video.pause();
            playButton.textContent = 'Воспроизвести видео';
        }
    });
});


捕获桌面流的例子
navigator.mediaDevices.getUserMedia({
     audio: true,
     video: {
         width: {min: 1024, ideal: 1280, max: 1920},
         height: {min: 576, ideal: 720, max: 1080},
         frameRate: {max: 30}
     }
}).then(stream => {
    const video1 = document.getElementById("video1")
    video1.srcObject = stream
    video1.onloadedmetadata = function(){video1.play()}
})
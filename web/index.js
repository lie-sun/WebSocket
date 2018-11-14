$(document).ready(function () {
    window.WebSocket = window.WebSocket || window.MozWebSocket;
    let websocket = new WebSocket('ws://192.168.3.112:9001');
    websocket.onopen = function (e) {
        console.log(e)
    };
    websocket.onmessage = function (e) {
        console.log(e)
    };
    console.log(websocket);

    $("#btn").on("click",function () {
        websocket.send('aaa');
        console.log(12)
    });


});
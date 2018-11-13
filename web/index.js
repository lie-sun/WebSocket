$(document).ready(function () {
    window.WebSocket = window.WebSocket || window.MozWebSocket;
    var ip_addr = document.location.hostname;
    let websocket = new WebSocket('ws://192.168.1.110:9001');
    console.log(websocket)

});
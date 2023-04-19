// chat/static/js/chat.js
var chatSocket = new WebSocket(
    'ws://' + window.location.host +
    '/ws/chat/' + roomName + '/'
);

chatSocket.onmessage = function(e) {
    var data = JSON.parse(e.data);
    var message = data['message'];
    var author = data['author'];
    var timestamp = data['timestamp'];
    var log = document.getElementById('chat_log');
    var msg = document.createElement('div');
    msg.innerHTML = '<p>[' + timestamp + '] ' + author + ': ' + message + '</p>';
    log.appendChild(msg);
    log.scrollTop = log.scrollHeight;
};

chatSocket.onclose = function(e) {
    console.error('WebSocket closed unexpectedly');
};

document.querySelector('#input_message').focus();
document.querySelector('#input_message').onkeyup = function(e) {
    if (e.keyCode === 13) {  // Enter 키 입력 시
        document.querySelector('#send_message').click();
    }
};

document.querySelector('#send_message').onclick = function(e) {
    var input = document.querySelector('#input_message');
    var message = input.value;
    input.value = '';
    chatSocket.send(JSON.stringify({
        'message': message
    }));
};


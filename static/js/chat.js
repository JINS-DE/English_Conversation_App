document.addEventListener('DOMContentLoaded', function() {
    // WebSocket 연결 설정
    const chatSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/chat/'
    );

    const chatContainer = document.getElementById('chat-container');
    const messageInput = document.getElementById('message-input');
    const sendButton = document.getElementById('send-button');

    // 메시지를 채팅 창에 표시하는 함수
    function appendMessage(text, sender='self') {
        const messageElement = document.createElement('div');
        messageElement.textContent = text;
        messageElement.className = sender === 'self' ? 'text-end' : 'text-start';
        chatContainer.appendChild(messageElement);
        chatContainer.scrollTop = chatContainer.scrollHeight; // 항상 최신 메시지 보기
    }

    // 메시지 전송 이벤트 처리
    sendButton.addEventListener('click', function(e) {
        const message = messageInput.value;
        if (message) {
            chatSocket.send(JSON.stringify({
                'message': message
            }));
            appendMessage(message, 'self');
            messageInput.value = '';
        }
    });

    // WebSocket을 통해 메시지를 받았을 때 이벤트 처리
    chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        appendMessage(data.message, 'other');
    };

    // WebSocket 연결이 닫혔을 때의 이벤트 처리
    chatSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };

    // 메시지 입력 시 엔터 키로도 메시지 전송 가능하게 하기
    messageInput.addEventListener('keyup', function(e) {
        if (e.key === 'Enter') {
            sendButton.click();
        }
    });
});

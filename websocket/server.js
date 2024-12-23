const WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', (ws) => {
  console.log('클라이언트 연결됨');

  ws.on('message', (message) => {
    try {
      // Buffer 데이터를 문자열로 변환
      const decodedMessage = message.toString('utf8');
      console.log('클라이언트로부터 메시지:', decodedMessage);

      // 클라이언트로 응답 전송
      ws.send(JSON.stringify({ response: "메시지 수신 완료!", received: decodedMessage }));
    } catch (error) {
      console.error("메시지 처리 오류:", error);
    }
  });

  // 클라이언트로 초기 메시지 전송
  ws.send(JSON.stringify({ message: "안녕하세요, 클라이언트!" }));
});

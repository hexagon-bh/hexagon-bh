const WebSocket = require('ws');
// WebSocket 객체 생성
const socket = new WebSocket("ws://192.168.35.19:8080");

// 연결이 열렸을 때 실행되는 이벤트 리스너
socket.onopen = () => {
  console.log("서버와 연결되었습니다.");
  // 서버로 메시지 보내기
  socket.send("안녕하세요, 서버!");
};

// 서버로부터 메시지를 받았을 때 실행되는 이벤트 리스너
socket.onmessage = (event) => {
  console.log("서버로부터 메시지:", event.data);
};

// 연결이 닫혔을 때 실행되는 이벤트 리스너
socket.onclose = () => {
  console.log("서버와의 연결이 닫혔습니다.");
};

// 오류가 발생했을 때 실행되는 이벤트 리스너
socket.onerror = (error) => {
  console.log("WebSocket 오류:", error);
};

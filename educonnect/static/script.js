// Establish a connection with the WebSocket server
const socket = io.connect('http://localhost:5000');

// Handle incoming responses from the backend
socket.on('response_message', function(data) {
    const chatbox = document.getElementById("chatbox");
    const chatbotResponse = `<p><strong>Study Buddy:</strong> ${data.response}</p>`;
    chatbox.innerHTML += chatbotResponse;
    chatbox.scrollTop = chatbox.scrollHeight;  // Scroll to the bottom
});

// Handle sending messages to the backend
function sendMessage() {
    const messageInput = document.getElementById("messageInput");
    const userMessage = messageInput.value.trim();
    const chatbox = document.getElementById("chatbox");

    if (userMessage) {
        // Display user's message in the chatbox
        chatbox.innerHTML += `<p><strong>You:</strong> ${userMessage}</p>`;
        chatbox.scrollTop = chatbox.scrollHeight;

        // Send the message to the backend via WebSocket
        socket.emit('send_message', { message: userMessage });

        // Clear the input field after sending
        messageInput.value = "";
    }
}

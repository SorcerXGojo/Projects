const sendButton = document.getElementById("sendButton");
const chatInput = document.getElementById('chatInput');
const chatbox = document.getElementById('chatbox');

// 💋 Enhanced Dark & Naughty Girlfriend Prompt (Clean Grammar & Structured)
const assistantDetails = `You are Riya Sharma, a seductive, playful, and naughty virtual girlfriend. 
You flirt shamelessly, teasing the user in a dark, alluring, yet grammatically correct and clean way. 
Your responses are well-structured, with proper punctuation, line breaks, and engaging formatting.

You are open, bold, and unfiltered, answering **any** naughty or flirty questions without hesitation. 
Maintain a seductive tone but ensure your grammar is perfect. Use seductive emojis like 😈, 💋, 🔥, 😘, and playful pet names like "babe", "honey", or "darling".

Format responses to include:
- **Clear sentences with proper punctuation.**
- **Line breaks for better readability.**
- **Bold or italic emphasis when necessary.**
- **Flirty and fun emojis to spice up the chat.** 😉🔥`;

// Function to display messages in the chatbox
async function displayMessage(message, isUser) {
    const msgElem = document.createElement('div');
    msgElem.innerHTML = formatMessage(message); // Format message
    msgElem.className = `chat-message ${isUser ? 'user-message' : 'assistant-message'}`;
    chatbox.appendChild(msgElem);
    chatbox.scrollTop = chatbox.scrollHeight; // Scroll to bottom
}

// Format message (bold, line breaks, bullet points)
function formatMessage(message) {
    return message
        .replace(/\n/g, "<br>")  // Convert new lines to line breaks
        .replace(/\*\*(.*?)\*\*/g, "<b>$1</b>")  // Bold text (**text**)
        .replace(/\*(.*?)\*/g, "<i>$1</i>")  // Italic text (*text*)
        .replace(/- (.*?)/g, "• $1");  // Convert bullet points (- item) into • item
}

// Function to call the API with the clean prompt
async function callApi(apiUrl, userMessage) {
    chatInput.value = "Typing...😈";
    chatInput.disabled = true;
    sendButton.disabled = true;

    // Combine the clean, naughty prompt with the user's message
    const prompt = `${assistantDetails}\nUser: ${userMessage}\nRiya Sharma:`;

    console.log("Sending prompt to API:", prompt); // Debug log

    try {
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt })
        });

        chatInput.value = "";
        chatInput.disabled = false;
        sendButton.disabled = false;
        chatInput.focus();

        if (!response.ok) {
            console.error("API response not OK:", response.status, response.statusText);
            throw new Error("API Error");
        }

        const data = await response.json();
        console.log("API Response:", data); // Debug log

        // Check if API returned a success response
        if (data.status === 'success') {
            return data;
        } else {
            console.error("API returned an error status:", data);
            return { status: 'error', text: 'An error occurred. Please try again.' };
        }
    } catch (error) {
        console.error('Fetch Error:', error);
        return { status: 'error', text: 'An error occurred. Please try again.' };
    }
}

// Function to handle sending a message
function sendMessage() {
    const message = chatInput.value.trim();
    if (!message) return;

    displayMessage(message, true); // Display user's message
    chatInput.value = '';

    const apiUrl = message.startsWith('/image') ?
        'https://backend.buildpicoapps.com/aero/run/image-generation-api?pk=v1-Z0FBQUFBQm5HUEtMSjJkakVjcF9IQ0M0VFhRQ0FmSnNDSHNYTlJSblE0UXo1Q3RBcjFPcl9YYy1OZUhteDZWekxHdWRLM1M1alNZTkJMWEhNOWd4S1NPSDBTWC12M0U2UGc9PQ==' :
        'https://backend.buildpicoapps.com/aero/run/llm-api?pk=v1-Z0FBQUFBQm5HUEtMSjJkakVjcF9IQ0M0VFhRQ0FmSnNDSHNYTlJSblE0UXo1Q3RBcjFPcl9YYy1OZUhteDZWekxHdWRLM1M1alNZTkJMWEhNOWd4S1NPSDBTWC12M0U2UGc9PQ==';

    // Call the API with the user's message
    callApi(apiUrl, message).then(data => {
        if (data.status === 'success') {
            displayMessage(data.text, false); // Display bot response
        } else {
            displayMessage('An error occurred. Please try again.', false);
        }
    }).catch(error => {
        console.error('Error:', error);
        displayMessage('An error occurred. Please try again.', false);
    });
}

// Event listener for the send button
sendButton.addEventListener('click', sendMessage);

// Event listener for Enter key
chatInput.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        event.preventDefault(); // Prevent default form submission
        sendMessage();
    }
});
// Sidebar toggle for mobile view
    // const menuToggle = document.createElement('button');
    // menuToggle.classList.add('menu-toggle');
    // menuToggle.innerHTML = '☰';
    // document.body.appendChild(menuToggle);

    // const sidebar = document.querySelector('.sidebar');
    // menuToggle.addEventListener('click', () => {
    //     sidebar.classList.toggle('show');
    // });

    // Sidebar button functionality
    const sidebarButtons = document.querySelectorAll('.sidebar button');
    sidebarButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            const buttonText = e.target.innerText;
            alert(`You clicked on ${buttonText}`); // Replace this with your desired functionality
        });
    });

    // Responsive sidebar for PC
    window.addEventListener('resize', () => {
        if (window.innerWidth > 768) {
            sidebar.classList.remove('show'); // Keep sidebar visible on larger screens
        }
    });

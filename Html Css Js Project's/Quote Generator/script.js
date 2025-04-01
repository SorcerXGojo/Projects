document.addEventListener("DOMContentLoaded", function () {
    const quoteButton = document.getElementById("quoteButton");
    const quoteDisplay = document.getElementById("quoteDisplay");

    quotes = [
        { "text": "The only limit to our realization of tomorrow is our doubts of today.", "author": "Franklin D. Roosevelt" },
        { "text": "Do what you can, with what you have, where you are.", "author": "Theodore Roosevelt" },
        { "text": "Success is not final, failure is not fatal: It is the courage to continue that counts.", "author": "Winston Churchill" },
        { "text": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt" },
        { "text": "Act as if what you do makes a difference. It does.", "author": "William James" },
        { "text": "Life is 10% what happens to us and 90% how we react to it.", "author": "Charles R. Swindoll" },
        { "text": "What lies behind us and what lies before us are tiny matters compared to what lies within us.", "author": "Ralph Waldo Emerson" },
        { "text": "Happiness depends upon ourselves.", "author": "Aristotle" },
        { "text": "You must be the change you wish to see in the world.", "author": "Mahatma Gandhi" },
        { "text": "He who opens a school door, closes a prison.", "author": "Victor Hugo" },
        { "text": "We are what we repeatedly do. Excellence, then, is not an act, but a habit.", "author": "Aristotle" },
        { "text": "Opportunities don't happen. You create them.", "author": "Chris Grosser" },
        { "text": "The way to get started is to quit talking and begin doing.", "author": "Walt Disney" },
        { "text": "If you look at what you have in life, you'll always have more.", "author": "Oprah Winfrey" },
        { "text": "The secret of getting ahead is getting started.", "author": "Mark Twain" },
        { "text": "Keep your face always toward the sunshine—and shadows will fall behind you.", "author": "Walt Whitman" },
        { "text": "Hardships often prepare ordinary people for an extraordinary destiny.", "author": "C.S. Lewis" },
        { "text": "Don’t count the days, make the days count.", "author": "Muhammad Ali" },
        { "text": "Everything you’ve ever wanted is on the other side of fear.", "author": "George Addair" },
        { "text": "The best way to predict the future is to invent it.", "author": "Alan Kay" },
        { "text": "You are never too old to set another goal or to dream a new dream.", "author": "C.S. Lewis" },
        { "text": "Your time is limited, so don’t waste it living someone else’s life.", "author": "Steve Jobs" },
        { "text": "The future belongs to those who believe in the beauty of their dreams.", "author": "Eleanor Roosevelt" },
        { "text": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius" },
        { "text": "Success usually comes to those who are too busy to be looking for it.", "author": "Henry David Thoreau" },
        { "text": "Don’t watch the clock; do what it does. Keep going.", "author": "Sam Levenson" },
        { "text": "You miss 100% of the shots you don’t take.", "author": "Wayne Gretzky" },
        { "text": "The only way to do great work is to love what you do.", "author": "Steve Jobs" },
        { "text": "If you can dream it, you can do it.", "author": "Walt Disney" },
        { "text": "The best revenge is massive success.", "author": "Frank Sinatra" },
        { "text": "Success is walking from failure to failure with no loss of enthusiasm.", "author": "Winston Churchill" },
        { "text": "The only place where success comes before work is in the dictionary.", "author": "Vidal Sassoon" },
        { "text": "Dream big and dare to fail.", "author": "Norman Vaughan" },
        { "text": "What we fear doing most is usually what we most need to do.", "author": "Tim Ferriss" },
        { "text": "You can’t use up creativity. The more you use, the more you have.", "author": "Maya Angelou" },
        { "text": "Success is not how high you have climbed, but how you make a positive difference to the world.", "author": "Roy T. Bennett" },
        { "text": "The only limit to our realization of tomorrow is our doubts of today.", "author": "Franklin D. Roosevelt" },
        { "text": "You are never too old to set another goal or to dream a new dream.", "author": "C.S. Lewis" },
        { "text": "The best way to predict the future is to create it.", "author": "Peter Drucker" }

    ];

    function getQuote() {
        const randomIndex = Math.floor(Math.random() * quotes.length);
        const quote = quotes[randomIndex];
        quoteDisplay.innerHTML = `<p>${quote.text}</p><p>- ${quote.author}</p>`;
    }
    quoteButton.addEventListener("click", getQuote);
});
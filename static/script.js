// static/script.js
document.addEventListener('DOMContentLoaded', function(){
  // QUIZ
  document.querySelectorAll('.opt').forEach(btn => {
    btn.addEventListener('click', function(){
      const qblock = this.closest('.qblock');
      const qid = parseInt(qblock.dataset.qid);
      const chosen = parseInt(this.dataset.idx);
      fetch('/quiz/check', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({qid: qid, chosen: chosen})
      }).then(r => r.json()).then(data => {
        if(data.error){ qblock.querySelector('.result').textContent = 'Error'; return; }
        qblock.querySelector('.result').textContent = data.correct ? 'Correct ✅' : 'Wrong ❌';
      });
    });
  });

  // CHATBOT
  const chatForm = document.getElementById('chatForm');
  const chatInput = document.getElementById('chatInput');
  const chatbox = document.getElementById('chatbox');
  const sendBtn = document.getElementById('sendBtn');
  function appendMsg(text, cls){
    const div = document.createElement('div');
    div.className = 'chat-msg ' + cls;
    div.textContent = text;
    chatbox.appendChild(div);
    chatbox.scrollTop = chatbox.scrollHeight;
  }
  if(sendBtn){
    sendBtn.addEventListener('click', function(){
      const message = chatInput.value.trim();
      if(!message) return;
      appendMsg('You: ' + message, 'chat-user');
      chatInput.value = '';
      fetch('/chatbot/message', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({message})
      }).then(r => r.json()).then(data => {
        appendMsg('Bot: ' + (data.reply || 'No reply'), 'chat-bot');
      });
    });
  }

  // WEATHER
  const getWeatherBtn = document.getElementById('getWeather');
  if(getWeatherBtn){
    getWeatherBtn.addEventListener('click', function(){
      const city = document.getElementById('city').value.trim();
      if(!city) return;
      fetch('/weather/get', {
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body: JSON.stringify({city})
      }).then(r => r.json()).then(data => {
        const div = document.getElementById('weatherResult');
        if(data.error){
          div.innerHTML = '<p>Error: ' + (data.error || 'Unknown') + '</p>';
        } else {
          div.innerHTML = `<h4>${data.city}</h4>
            <p>${data.description}</p>
            <p>Temp: ${data.temp} °C</p>
            <p>Humidity: ${data.humidity}%</p>
            <p>Wind: ${data.wind} m/s</p>`;
        }
      });
    });
  }
});


document.getElementById('contactForm').addEventListener('submit', async (e) => {
  e.preventDefault();

  const form = e.target;
  const data = {
    name: form.name.value,
    email: form.email.value,
    message: form.message.value
  };

  try {
    const res = await fetch('https://your-api-gateway-endpoint.amazonaws.com/contact', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });

    const result = await res.json();
    document.getElementById('responseMessage').innerText = 'Message sent successfully!';
  } catch (err) {
    document.getElementById('responseMessage').innerText = 'Error sending message.';
  }
});
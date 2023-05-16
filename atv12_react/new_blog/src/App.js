import React, { useState, useEffect } from 'react'
import './App.css';

function App() {
  const [data, setData] = useState(null);
  const [busca, setBusca] = useState('');

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await fetch('https://script.google.com/macros/s/AKfycbzBn3sALe1rYjz7Ze-Ik7q9TEVP0I2V3XX7GNcecWP8NvCzGt4yO_RT1OlQp09TE9cU/exec');
        const data = await response.json();
        setData(data);
      } catch (error) {
        console.error(error);
      }
    }

    fetchData();
  }, []);


  const msgFiltered = data?.filter((msg) => typeof msg[0] === 'string' && msg[0].startsWith(busca) || msg[1] === 'string' && msg[1].startsWith(busca))

  console.log(msgFiltered);

  return (
    <div>
      <h4> Procure sua mensagem</h4>
      <input type="text" value={busca} onChange={(e) => setBusca(e.target.value)} />
        <tbody>
          {msgFiltered && msgFiltered.map((msg) => <tr key={msg}><td>{msg[0]}</td><td>{msg[1]}</td><td>{msg[2]}</td></tr>)}
        </tbody>
    </div>
  );
}


export default App;

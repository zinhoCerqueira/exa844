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

  console.log(typeof data);
  console.log(data)

  const msgFiltered = data?.filter((msg) => typeof msg[0] === 'string' && msg[0].startsWith(busca))

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








function Table(props) {
  const rows = props.data.map(item => (
    <tr key={item.id}>
      <td>{item.id}</td>
      <td>{item.name}</td>
      <td>{item.price}</td>
    </tr>
  ));

  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Price</th>
        </tr>
      </thead>
      <tbody>
        {rows}
      </tbody>
    </table>
  );
}




export default App;

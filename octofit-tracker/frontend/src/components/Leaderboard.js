import { useEffect, useState } from 'react';

const apiBase = process.env.REACT_APP_CODESPACE_NAME
  ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api`
  : 'http://localhost:8000/api';

function Leaderboard() {
  const [rows, setRows] = useState([]);
  const endpoint = `${apiBase}/leaderboard/`;

  useEffect(() => {
    async function fetchLeaderboard() {
      try {
        console.log('Leaderboard endpoint:', endpoint);
        const response = await fetch(endpoint);
        const payload = await response.json();
        console.log('Leaderboard fetched data:', payload);
        const normalized = Array.isArray(payload) ? payload : payload?.results || [];
        setRows(normalized);
      } catch (error) {
        console.error('Leaderboard fetch error:', error);
      }
    }

    fetchLeaderboard();
  }, [endpoint]);

  return (
    <section>
      <h2>Leaderboard</h2>
      <ul className="list-group">
        {rows.map((row) => (
          <li key={row.id} className="list-group-item">
            Rank {row.rank} - Score {row.score}
          </li>
        ))}
      </ul>
    </section>
  );
}

export default Leaderboard;

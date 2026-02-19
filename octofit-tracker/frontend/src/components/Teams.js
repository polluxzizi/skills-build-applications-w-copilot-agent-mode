import { useEffect, useState } from 'react';

const apiBase = process.env.REACT_APP_CODESPACE_NAME
  ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api`
  : 'http://localhost:8000/api';

function Teams() {
  const [teams, setTeams] = useState([]);
  const endpoint = `${apiBase}/teams/`;

  useEffect(() => {
    async function fetchTeams() {
      try {
        console.log('Teams endpoint:', endpoint);
        const response = await fetch(endpoint);
        const payload = await response.json();
        console.log('Teams fetched data:', payload);
        const normalized = Array.isArray(payload) ? payload : payload?.results || [];
        setTeams(normalized);
      } catch (error) {
        console.error('Teams fetch error:', error);
      }
    }

    fetchTeams();
  }, [endpoint]);

  return (
    <section>
      <h2>Teams</h2>
      <ul className="list-group">
        {teams.map((team) => (
          <li key={team.id} className="list-group-item">
            {team.name}
          </li>
        ))}
      </ul>
    </section>
  );
}

export default Teams;

import { useEffect, useState } from 'react';

const apiBase = process.env.REACT_APP_CODESPACE_NAME
  ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api`
  : 'http://localhost:8000/api';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const endpoint = `${apiBase}/workouts/`;

  useEffect(() => {
    async function fetchWorkouts() {
      try {
        console.log('Workouts endpoint:', endpoint);
        const response = await fetch(endpoint);
        const payload = await response.json();
        console.log('Workouts fetched data:', payload);
        const normalized = Array.isArray(payload) ? payload : payload?.results || [];
        setWorkouts(normalized);
      } catch (error) {
        console.error('Workouts fetch error:', error);
      }
    }

    fetchWorkouts();
  }, [endpoint]);

  return (
    <section>
      <h2>Workouts</h2>
      <ul className="list-group">
        {workouts.map((workout) => (
          <li key={workout.id} className="list-group-item">
            {workout.title} ({workout.difficulty}) - {workout.duration_minutes} minutes
          </li>
        ))}
      </ul>
    </section>
  );
}

export default Workouts;

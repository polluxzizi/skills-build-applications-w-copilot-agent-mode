import { useEffect, useState } from 'react';

const apiBase = process.env.REACT_APP_CODESPACE_NAME
  ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api`
  : 'http://localhost:8000/api';

function Activities() {
  const [activities, setActivities] = useState([]);
  const endpoint = `${apiBase}/activities/`;

  useEffect(() => {
    async function fetchActivities() {
      try {
        console.log('Activities endpoint:', endpoint);
        const response = await fetch(endpoint);
        const payload = await response.json();
        console.log('Activities fetched data:', payload);
        const normalized = Array.isArray(payload) ? payload : payload?.results || [];
        setActivities(normalized);
      } catch (error) {
        console.error('Activities fetch error:', error);
      }
    }

    fetchActivities();
  }, [endpoint]);

  return (
    <section>
      <h2>Activities</h2>
      <ul className="list-group">
        {activities.map((activity) => (
          <li key={activity.id} className="list-group-item">
            {activity.activity_type} - {activity.duration_minutes} minutes
          </li>
        ))}
      </ul>
    </section>
  );
}

export default Activities;

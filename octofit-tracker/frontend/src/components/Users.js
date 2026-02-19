import { useEffect, useState } from 'react';

const apiBase = process.env.REACT_APP_CODESPACE_NAME
  ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api`
  : 'http://localhost:8000/api';

function Users() {
  const [users, setUsers] = useState([]);
  const endpoint = `${apiBase}/users/`;

  useEffect(() => {
    async function fetchUsers() {
      try {
        console.log('Users endpoint:', endpoint);
        const response = await fetch(endpoint);
        const payload = await response.json();
        console.log('Users fetched data:', payload);
        const normalized = Array.isArray(payload) ? payload : payload?.results || [];
        setUsers(normalized);
      } catch (error) {
        console.error('Users fetch error:', error);
      }
    }

    fetchUsers();
  }, [endpoint]);

  return (
    <section>
      <h2>Users</h2>
      <ul className="list-group">
        {users.map((user) => (
          <li key={user.id} className="list-group-item">
            {user.name} ({user.email})
          </li>
        ))}
      </ul>
    </section>
  );
}

export default Users;

import './styles.css';
import { AuthPage } from './pages/AuthPage';
import { DashboardPage } from './pages/DashboardPage';
import { useAuth } from './hooks/useAuth';

function App() {
  const { token, login } = useAuth();

  if (!token) {
    return <AuthPage onLogin={login} />;
  }

  return <DashboardPage />;
}

export default App;
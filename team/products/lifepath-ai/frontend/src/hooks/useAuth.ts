import { useState, useEffect } from 'react';

interface User {
  id: number;
  email: string;
}

export function useAuth() {
  const [token, setToken] = useState<string | null>(null);
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const storedToken = localStorage.getItem('token');
    if (storedToken) {
      setToken(storedToken);
      // 这里可以从 token 解析用户信息或调用 API 获取用户详情
      try {
        const payload = JSON.parse(atob(storedToken.split('.')[1]));
        setUser({ id: payload.user_id, email: payload.email });
      } catch (e) {
        // Token 无效，清除
        localStorage.removeItem('token');
        setToken(null);
      }
    }
    setLoading(false);
  }, []);

  const login = (newToken: string, userData: User) => {
    localStorage.setItem('token', newToken);
    setToken(newToken);
    setUser(userData);
  };

  const logout = () => {
    localStorage.removeItem('token');
    setToken(null);
    setUser(null);
  };

  return { token, user, loading, login, logout };
}
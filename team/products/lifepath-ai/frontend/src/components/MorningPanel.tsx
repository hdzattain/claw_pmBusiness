import { useState, useEffect } from 'react';
import { api } from '../services/api';

export function MorningPanel() {
  const [advice, setAdvice] = useState<string>('');
  const [loading, setLoading] = useState(false);

  const fetchAdvice = async () => {
    setLoading(true);
    try {
      const response = await api.get('/morning/advice');
      setAdvice(response.advice);
    } catch (err: any) {
      setAdvice('获取晨间建议失败，请稍后重试');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchAdvice();
  }, []);

  return (
    <div className="bg-white rounded-xl shadow-sm p-6">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-xl font-semibold text-gray-900">🌅 晨间建议</h2>
        <button
          onClick={fetchAdvice}
          disabled={loading}
          className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors disabled:opacity-50"
        >
          {loading ? '刷新中...' : '刷新建议'}
        </button>
      </div>
      <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
        <p className="text-gray-700 whitespace-pre-wrap">{advice || '暂无建议'}</p>
      </div>
    </div>
  );
}
import { useState } from 'react';
import { api } from '../services/api';

export function EveningPanel() {
  const [reflection, setReflection] = useState<string>('');
  const [loading, setLoading] = useState(false);

  const fetchReflection = async () => {
    setLoading(true);
    try {
      const response = await api.get('/evening/reflection');
      setReflection(response.reflection);
    } catch (err: any) {
      setReflection('获取晚间复盘失败，请稍后重试');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white rounded-xl shadow-sm p-6">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-xl font-semibold text-gray-900">🌙 晚间复盘</h2>
        <button
          onClick={fetchReflection}
          disabled={loading}
          className="px-4 py-2 bg-purple-500 text-white rounded-lg hover:bg-purple-600 transition-colors disabled:opacity-50"
        >
          {loading ? '加载中...' : '获取复盘'}
        </button>
      </div>
      <div className="bg-purple-50 border border-purple-200 rounded-lg p-4">
        <p className="text-gray-700 whitespace-pre-wrap">{reflection || '暂无复盘内容'}</p>
      </div>
    </div>
  );
}
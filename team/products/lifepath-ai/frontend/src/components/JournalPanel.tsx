import { useState } from 'react';
import { api } from '../services/api';

export function JournalPanel() {
  const [entries, setEntries] = useState<any[]>([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);
  const [loading, setLoading] = useState(false);

  const loadEntries = async (page: number = 1) => {
    setLoading(true);
    try {
      const response = await api.get(`/journal?page=${page}&limit=10`);
      setEntries(response.entries);
      setTotalPages(Math.ceil(response.total / 10));
      setCurrentPage(page);
    } catch (err) {
      console.error('Failed to load entries:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white rounded-xl shadow-sm p-6">
      <h2 className="text-xl font-semibold text-gray-900 mb-4">📝 日记记录</h2>
      <div className="mb-4">
        <button
          onClick={() => loadEntries(1)}
          className="px-4 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600 transition-colors"
        >
          刷新记录
        </button>
      </div>
      <div className="space-y-4">
        {entries.map((entry) => (
          <div key={entry.id} className="border border-gray-200 rounded-lg p-4">
            <div className="text-sm text-gray-500 mb-2">
              {new Date(entry.created_at).toLocaleString()}
            </div>
            <p className="text-gray-700">{entry.text_masked}</p>
            {entry.mood && (
              <div className="mt-2">
                <span className="inline-block px-2 py-1 bg-blue-100 text-blue-800 text-xs rounded">
                  心情: {entry.mood}
                </span>
              </div>
            )}
          </div>
        ))}
      </div>
      {totalPages > 1 && (
        <div className="flex justify-center mt-6 space-x-2">
          {[...Array(totalPages)].map((_, i) => (
            <button
              key={i}
              onClick={() => loadEntries(i + 1)}
              className={`px-3 py-1 rounded ${
                currentPage === i + 1
                  ? 'bg-blue-500 text-white'
                  : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
              }`}
            >
              {i + 1}
            </button>
          ))}
        </div>
      )}
    </div>
  );
}
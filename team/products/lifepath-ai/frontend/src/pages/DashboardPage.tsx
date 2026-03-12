import { useState } from 'react';
import { MorningPanel } from '../components/MorningPanel';
import { EveningPanel } from '../components/EveningPanel';
import { JournalPanel } from '../components/JournalPanel';
import { TaskBoard } from '../components/TaskBoard';
import { useAuth } from '../hooks/useAuth';

export function DashboardPage() {
  const { user, logout } = useAuth();
  const [activeTab, setActiveTab] = useState<'morning' | 'journal' | 'tasks' | 'evening'>('morning');

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="flex items-center">
              <h1 className="text-xl font-semibold text-gray-900">LifePath AI</h1>
              <span className="ml-2 text-sm text-gray-500">欢迎, {user?.email}</span>
            </div>
            <button
              onClick={logout}
              className="px-4 py-2 text-sm text-gray-700 hover:text-gray-900 transition-colors"
            >
              退出登录
            </button>
          </div>
        </div>
      </header>

      {/* Navigation Tabs */}
      <nav className="bg-white border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex space-x-8">
            {[
              { id: 'morning', label: '晨间建议', icon: '🌅' },
              { id: 'journal', label: '日记记录', icon: '📝' },
              { id: 'tasks', label: '任务看板', icon: '📋' },
              { id: 'evening', label: '晚间复盘', icon: '🌙' },
            ].map((tab) => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id as any)}
                className={`flex items-center px-1 py-4 text-sm font-medium border-b-2 transition-colors ${
                  activeTab === tab.id
                    ? 'border-blue-500 text-blue-600'
                    : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                }`}
              >
                <span className="mr-2">{tab.icon}</span>
                {tab.label}
              </button>
            ))}
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
        {activeTab === 'morning' && <MorningPanel />}
        {activeTab === 'journal' && <JournalPanel />}
        {activeTab === 'tasks' && <TaskBoard />}
        {activeTab === 'evening' && <EveningPanel />}
      </main>
    </div>
  );
}
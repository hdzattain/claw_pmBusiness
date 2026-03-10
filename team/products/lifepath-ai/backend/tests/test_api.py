import sys
from pathlib import Path
from fastapi.testclient import TestClient

sys.path.append(str(Path(__file__).resolve().parents[1]))
from app.main import app
from app.core.db import init_db

init_db()
client = TestClient(app)


def test_health():
    r = client.get('/health')
    assert r.status_code == 200
    assert r.json()['ok'] is True


def test_auth_and_advice_flow():
    email = 'phase2_user@example.com'
    pwd = '12345678'

    reg = client.post('/api/auth/register', json={'email': email, 'password': pwd})
    assert reg.status_code in (200, 409)

    login = client.post('/api/auth/login', json={'email': email, 'password': pwd})
    assert login.status_code == 200
    token = login.json()['token']
    headers = {'Authorization': f'Bearer {token}'}

    morning = client.post('/api/advice/morning', json={
        'text': '我想转产品经理但很焦虑',
        'mood': '焦虑',
        'goal': '两周内完成一份作品集'
    }, headers=headers)
    assert morning.status_code == 200
    assert morning.json()['success'] is True

    evening = client.post('/api/advice/evening', json={
        'wins': '完成了作品集首页',
        'blockers': '不确定案例结构',
        'next_action': '明早补齐一个项目案例'
    }, headers=headers)
    assert evening.status_code == 200
    assert evening.json()['success'] is True

    journal = client.get('/api/advice/journal', headers=headers)
    assert journal.status_code == 200
    assert journal.json()['success'] is True
    assert 'pagination' in journal.json()


def test_journal_pagination_and_validation():
    email = 'phase2_user_2@example.com'
    pwd = '12345678'

    reg = client.post('/api/auth/register', json={'email': email, 'password': pwd})
    assert reg.status_code in (200, 409)

    login = client.post('/api/auth/login', json={'email': email, 'password': pwd})
    assert login.status_code == 200
    token = login.json()['token']
    headers = {'Authorization': f'Bearer {token}'}

    # 新增至少 12 条，验证分页
    for i in range(12):
        r = client.post('/api/advice/morning', json={
            'text': f'第{i}条记录',
            'mood': '平静',
            'goal': '持续推进'
        }, headers=headers)
        assert r.status_code == 200

    page1 = client.get('/api/advice/journal?limit=5&offset=0', headers=headers)
    assert page1.status_code == 200
    body1 = page1.json()
    assert body1['success'] is True
    assert len(body1['items']) == 5
    assert body1['pagination']['limit'] == 5
    assert body1['pagination']['offset'] == 0
    assert body1['pagination']['total'] >= 12
    assert body1['pagination']['has_more'] is True

    page3 = client.get('/api/advice/journal?limit=5&offset=10', headers=headers)
    assert page3.status_code == 200
    body3 = page3.json()
    assert body3['success'] is True
    assert len(body3['items']) >= 2
    assert body3['pagination']['offset'] == 10

    # 输入校验：空字符串应被拒绝
    bad = client.post('/api/advice/morning', json={
        'text': '',
        'mood': '平静',
        'goal': '测试'
    }, headers=headers)
    assert bad.status_code == 422

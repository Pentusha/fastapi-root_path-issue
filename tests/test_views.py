async def test_get_users(client):
    resp = await client.get('/users/')
    assert resp.raise_for_status().json() == {
        'path': '/users/',
        'raw_path': '/users/',
        'root_path': '/auth',
    }


async def test_get_auth(client):
    resp = await client.get('/auth/')
    assert resp.raise_for_status().json() == {
        'path': '/auth/',
        'raw_path': '/auth/',
        'root_path': '/auth',
    }

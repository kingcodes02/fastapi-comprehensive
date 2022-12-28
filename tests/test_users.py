import pytest
from jose import jwt
from app import schemas
from app.config import settings


# def test_root(client):
#     response = client.get("/")
#     print(response.json().get("message"))
#     assert response.json().get("message") == "This is my fastAPI comprehensive tutorial!!!!"
#     assert response.status_code == 200


def test_create_user(client):
    response = client.post("/users/", json={"email": "king1@gmail.com", "password": "password123"}
                           )
    new_user = schemas.UserOut(**response.json())
    assert new_user.email == "king1@gmail.com"
    assert response.status_code == 201


def test_login_user(client,  test_user):
    response = client.post("/login", data={"username": test_user['email'], "password": test_user['password']}
                           )
    login_response = schemas.Token(**response.json())
    payLoad = jwt.decode(login_response.access_token,
                         settings.secret_key, algorithms=[settings.algorithm])
    id = payLoad.get("user_id")
    assert id == test_user['id']
    assert login_response.token_type == "bearer"
    assert response.status_code == 200


@pytest.mark.parametrize("email, password, status_code", [
    ('wrongemail@gmail.com', 'pass123', 403),
    ('king@gmail.com', 'pass123', 403),
    (None, 'pass123', 422),
    ('king@gmail.com', None, 422)
])
def test_incorrect_login(test_user, client, email, password, status_code):
    response = client.post(
        "/login", data={"username": email, "password": password})

    assert response.status_code == status_code
    # assert response.json().get(
    #     'detail') == "Invalid Credentials. Either email or password is/are wrong."

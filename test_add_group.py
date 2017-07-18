# -*- coding: utf-8 -*-
from application import Application
import pytest

@pytest.fixture
def app():
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
        success = True
        app.open_home_page()
        app.login(login="admin", password="secret")
        app.open_groups_page()
        app.create_group()
        app.logout()


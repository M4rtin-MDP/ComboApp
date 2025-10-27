import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.database import Base, engine

client = TestClient(app)

def setup_module(module):
    Base.metadata.create_all(bind=engine)

def teardown_module(module):
    Base.metadata.drop_all(bind=engine)

def test_create_product_local_combo_order():
    # create product base and ingredient
    p1 = client.post("/products", json={"nombre":"Pan brioche","tipo":"base","precio":600}).json()
    p2 = client.post("/products", json={"nombre":"Queso","tipo":"ingrediente","precio":200}).json()
    # create local and add product mapping
    l = client.post("/locals", json={"nombre":"BurgerMix","direccion":"Calle Falsa 123"}).json()
    client.post(f"/locals/{l['id']}/products/{p1['id']}")
    client.post(f"/locals/{l['id']}/products/{p2['id']}")
    # create combo
    combo_payload = {"nombre":"Mi Combo","base_id":p1['id'],"ingredient_ids":[p2['id']],"bebida_id":None,"acompanamiento_id":None}
    c = client.post("/combos", json=combo_payload).json()
    assert c["total"] == 800.0
    # create order
    order_payload = {"combo_id": c['id'], "user_id": 1, "local_id": l['id']}
    o = client.post("/orders", json=order_payload).json()
    assert o["combo_id"] == c['id']

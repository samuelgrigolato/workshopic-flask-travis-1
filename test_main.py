
import main

def test_soma():
	app = main.app.test_client()
	res = app.get("/soma/81/51")
	assert res.data == b"131"

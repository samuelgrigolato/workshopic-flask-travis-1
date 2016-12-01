
import main

def test_soma():
	app = main.app.test_client()
	res = app.get("/soma/50/81")
	assert res.data == b"131"

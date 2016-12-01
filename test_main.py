
import main

def test_soma():
	app = main.app.test_client()
	res = app.get("/soma/50/80")
	assert res.data == b"130"

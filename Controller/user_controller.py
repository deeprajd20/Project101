from app import app
from model.user_model import user_model
obj_um = user_model()

@app.route("/user/signup")
def signup():
    return obj_um.user_model_test()
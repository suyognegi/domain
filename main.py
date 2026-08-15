from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {
        "/is_exist": "http://127.0.0.1:8000/is_exist?email=suyognegi1@gmail.com",
        "/send_create_account_otp": "http://127.0.0.1:8000/send_create_account_otp?email=suyognegi1@gmail.com&ip=117.207.52.46&city=Palampur&region=Himachal%20Pradesh&country=India",
        "/check_create_otp": "http://127.0.0.1:8000/check_create_otp?email=suyognegi1@gmail.com&input_otp=616765",
        "/create_new_account":"http://127.0.0.1:8000/create_new_account",
        "/send_forgot_password_otp":"http://127.0.0.1:8000/send_forgot_password_otp?email=suyognegi1@gmail.com&ip=117.207.52.46&city=Palampur&region=Himachal%20Pradesh&country=India",
        "/check_forgot_password_otp": "http://127.0.0.1:8000/check_forgot_password_otp?email=suyognegi1@gmail.com&input_otp=616765"
    }

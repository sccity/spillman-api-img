import os, sys, yaml, uuid, pymysql
from flask import Flask, send_file, request, abort

app = Flask(__name__)

settings_file = "./config/settings.yaml"
if not os.path.exists(settings_file):
    print("settings.yaml not found!")
    sys.exit()

with open(settings_file, "r") as f:
    settings_data = yaml.load(f, Loader=yaml.FullLoader)


def connect():
    return pymysql.connect(
        host=settings_data["database"]["host"],
        user=settings_data["database"]["user"],
        password=settings_data["database"]["password"],
        database=settings_data["database"]["schema"],
    )


db = connect()
cursor = db.cursor()
cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED")
cursor.close()
db.close()


class AuthService:
    def __init__(self):
        return

    def validate_token(token, ip_address):
        db = connect()
        cursor = db.cursor()
        try:
            cursor.execute(f"""SELECT active from auth where uuid = '{token}'""")
            db_response = cursor.fetchone()
            cursor.close()
            db.close()
        except Exception:
            cursor.close()
            db.close()

        try:
            db_valid = db_response[0]
        except Exception:
            db_valid = 0

        if db_valid is None:
            valid = False

            db = connect()
            cursor = db.cursor()
            unique_id = uuid.uuid1()

            try:
                cursor.execute(
                    f"insert into auditlog (uuid,token,ip_address,resource,action,datetime) values ('{unique_id}','{token}','{ip_address}','AUTH','ACCESS DENIED',now())"
                )
                db.commit()
                cursor.close()
                db.close()
            except Exception:
                cursor.close()
                db.close()

        elif db_valid == 1:
            valid = True
        else:
            valid = False
            db = connect()
            cursor = db.cursor()
            unique_id = uuid.uuid1()

            try:
                cursor.execute(
                    f"insert into auditlog (uuid,token,ipaddr,resource,action,datetime) values ('{unique_id}','{token}','{ip_address}','AUTH','ACCESS DENIED',now())"
                )
                db.commit()
                cursor.close()
                db.close()
            except Exception:
                cursor.close()
                db.close()

        return valid

    def audit_request(token, ip_address, resource, action):
        db = connect()
        cursor = db.cursor()
        unique_id = uuid.uuid1()
        try:
            cursor.execute(
                f"insert into auditlog (uuid,token,ipaddr,resource,action,datetime) values ('{unique_id}','{token}','{ip_address}','{resource}','{action}',now())"
            )
            db.commit()
            cursor.close()
            db.close()
        except Exception:
            cursor.close()
            db.close()
        return


@app.route("/<img_name>")
def myapp(img_name):
    token = request.args.get("token", "")
    img_path = os.path.join("images", img_name)

    if not os.path.exists(img_path):
        return "Image not found"

    if token == "":
        AuthService.audit_request(
            "Missing", request.access_route[0], "AUTH", "ACCESS DENIED"
        )
        abort(403, description="Missing or invalid security token.")

    auth = AuthService.validate_token(token, request.access_route[0])
    if auth is True:
        pass
    else:
        abort(401, description="Invalid or disabled security token provided.")

    AuthService.audit_request(
        token,
        request.access_route[0],
        "image",
        f'[{{"image": "{img_path}", "token": "{token}"}}]',
    )

    return send_file(img_path, mimetype="image/png")


if __name__ == "__main__":
    from waitress import serve

    serve(app, host="0.0.0.0", port=5000, threads=100)

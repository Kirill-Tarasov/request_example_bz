import requests
import datetime
import time
import random
from jose import jws
from jose.constants import ALGORITHMS

class Bitzlato:
    BASE_URL = "https://bitzlato.com"
    def __init__(self, uid : int, key : dict, key_id : str):
        self.uid = uid
        self.key = key
        self.key_id = key_id

    def generate_token(self):
        dt = datetime.datetime.now()
        ts = time.mktime(dt.timetuple())
        payload = {
            "uid": self.uid,
            "aud": "usr",
            "iat" : int(ts),
            "jti": hex(random.getrandbits(64))
        }
        print(payload)
        return jws.sign(payload, self.key, headers={"kid" : self.key_id}, algorithm=ALGORITHMS.ES256)

    def get_list_adds(self, cryptocurrency: str, currency: str, is_owner_active: bool, limit: int,
                       pay_method: str, order_type: str) -> dict:
        end_point = "/api/p2p/exchange/dsa/"

        response = requests.get(self.BASE_URL + end_point, headers={
            "Authorization": "Bearer " + self.generate_token()
        },
            params={
                "cryptocurrency": f"{cryptocurrency}",
                "currency": f"{currency}",
                "type": f"{order_type}",  # purchase, selling
                "isOwnerActive": True,
                "limit": 20,
                "paymethod": f"{pay_method}"
        })

        return response.json()

import os
import pathlib

import requests

from constans import HOST
create = "/api/items/create/"
delete = "/api/items/delete/"
add_to_cart = "/shop/cart/add/{id}"


class PreconditionSteps:

    @staticmethod
    def create_item(data, file_name=None):
        if file_name is not None:
            current_dir = pathlib.Path(__file__).parent.resolve()
            file = open(os.path.join(current_dir, "../params/",  f'{file_name}.txt'), 'r')
            image = file.read()
            data.update({"photo": image})
        resp = requests.post(HOST + create, data=data).json()
        return resp

    @staticmethod
    def delete_item(id):
        data = {
            "id": id
        }
        resp = requests.post(HOST + delete, data=data).json()
        return resp

    @staticmethod
    def add_to_cart(id, count):
        params ={"count": count}
        add = add_to_cart.replace('{id}', str(id))
        resp = requests.get(HOST + add, params = params,
                          headers={
                              "Cookie": f"PHPSESSID=ad614d3c68b2ff30482a4a31b009de8f; _csrf=b97a76ece62f7730c330e6f53e88eec7e7500e632bbe8a54ba4b2046f5ef3e4aa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22cnaEupI6qR6ys35Dfr515O9bKruZzEzR%22%3B%7D"})
        return resp
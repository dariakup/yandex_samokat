import configuration
import requests
import data


def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order_body)


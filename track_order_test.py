import configuration
import data
import requests
import order_request

# Дарья Куприянова, 5-я когорта - Финальный проект. Инженер по тестированию плюс

def get_order_track():
    order_request.post_new_order(data.order_body)
    track = order_request.post_new_order(data.order_body).json()["track"]
    return track


def find_order_by_track():
    track = get_order_track()
    params_with_track = data.params.copy()
    params_with_track["t"] = track
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_PATH,
                        params=params_with_track)


def positive_assert():
    response = find_order_by_track()

    assert response.status_code == 200


def test_find_order_track_get_success():
    positive_assert()

from dateutil import parser

from apis.heb_cal import HebCalSession


def extract_shabbos_times():
    """
    To change the the times for candle lighting, havdala, and the zip code, jump into
    ```get_shabbos_times```
    Defaults to return shabbos/yom tov times for the current week
    """
    with HebCalSession() as session:
        dataset = session.get_shabbos_times().json()["items"]
        return [d for d in dataset if d.get("category") in ["havdalah", "candles"]]


def transform_day_time(dataset):
    message_dict = {"havdalah": "Havdalah", "candles": "Candle Lighting"}
    for record in dataset:
        record["message"] = parser.parse(record["date"]).strftime(
            f"{message_dict[record['category']]} on %A is at %-I:%M%p"
        )
        record["message"] = record["message"].replace("Saturday", "Shabbos")
    return dataset


def get_shabbos_times():
    dataset = extract_shabbos_times()
    dataset = transform_day_time(dataset)

    for record in dataset:
        # print(record) -> explore what is in the record
        print(record.get("message"))

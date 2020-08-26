""" https://www.hebcal.com/home/195/jewish-calendar-rest-api """
import datetime
import logging

from apis.sessions import BaseSession

BASE_URL = "https://www.hebcal.com"
ENDPOINTS = {
    "standard": f"{BASE_URL}/hebcal",
    "shabbat": f"{BASE_URL}/shabbat",
}
logger = logging.getLogger(__name__)


class HebCalSession(BaseSession):
    def get_full_heb_cal(
        self,
        version=1,
        output_config="json",
        year="now",
        month="now",
        major_holidays="on",
        minor_holidays="on",
        rosh_chodesh="on",
        minor_fasts="on",
        special_shabbos="on",
        modern_holidays="on",
        parsha="on",
        candle_lighting="on",
        havdalah_minutes=50,
        candle_minutes=18,
        hebrew_date_event="on",
        hebrew_date_all="on",
        omer="on",
        israel="off",
        geo="zip",
        zip="07621",
    ):
        """
        :param version: v, version, 1
        :param output_config: cfg, output JSON instead of HTML. Also variant cfg=fc for fullcalendar.io integration
        :param year: year, “now” for current year, or 4-digit YYYY such as 2003
        :param month: month, “x” for entire Gregorian year, or use a numeric month (1=January, 6=June, etc.)
        :param major_holidays: maj, Major holidays
        :param minor_holidays: min, Minor holidays (Tu BiShvat, Lag B’Omer, …)
        :param rosh_chodesh: nx, Rosh Chodesh
        :param minor_fasts: mf, Minor fasts (Ta’anit Esther, Tzom Gedaliah, …)
        :param special_shabbos: ss, Special Shabbatot (Shabbat Shekalim, Zachor, …)
        :param modern_holidays: mod, Modern holidays (Yom HaShoah, Yom HaAtzma’ut, …)
        :param parsha: s Parashat ha-Shavuah on Saturday
        :param candle_lighting:, c: Candle lighting times. See also candle-lighting options below.
        :param havdalah_minutes: m, Havdalah 50 minutes after sundown. Set to m=0 (zero) to disable Havdalah times
        :param candle_minutes: b, Candle-lighting time minutes before sunset
        :param hebrew_date_event: D, Hebrew date for dates with some event
        :param hebrew_date_all: Hebrew date for entire date range
        :param omer: o, Days of the Omer
        :param israel: i,
            off: Diaspora holidays and Torah readings (default if unspecified)
            on:  Israel holidays and Torah readings
        :param geo:
            none – no candle-lighting location (default if unspecified)
            geoname – location specified by GeoNames.org numeric ID.
                requires additional parameter geonameid=3448439
                Hebcal.com supports approximately 47,000 different GeoNames IDs.
                These are cities with a population of 5000+.
                See cities5000.zip from http://download.geonames.org/export/dump/.
            zip – location specified by United States ZIP code. requires additional parameter
                zip=90210
            city – location specified by one of the Hebcal.com legacy city identifiers. requires additional parameter
                city=GB-London
            pos – location specified by latitude, longitude, and timezone. Requires additional 3 parameters:
                latitude=[-90 to 90] – latitude in decimal format (e.g. 31.76904 or -23.5475)
                longitude=[-180 to 180] – longitude decimal format (e.g. 35.21633 or -46.63611)
                tzid=TimezoneIdentifier (See List of tz database time zones)
        :param zip: use default value of Bergenfield

        :return: response from hebcal
        """
        params = {}
        params["v"] = version
        params["cfg"] = output_config
        params["year"] = year
        params["month"] = month
        params["maj"] = major_holidays
        params["min"] = minor_holidays
        params["nx"] = rosh_chodesh
        params["mf"] = minor_fasts
        params["ss"] = special_shabbos
        params["mod"] = modern_holidays
        params["s"] = parsha
        params["c"] = candle_lighting
        params["m"] = havdalah_minutes
        params["b"] = candle_minutes
        params["D"] = hebrew_date_event
        params["d"] = hebrew_date_all
        params["o"] = omer
        params["i"] = israel
        params["geo"] = geo
        if params["geo"] == "zip":
            params["zip"] = zip
        url = ENDPOINTS["standard"]
        return self.get(url, params=params)

    def get_omer(self):
        """ Get the omer dates for the current year"""
        params = {
            "v": 1,
            "cfg": "json",
            "year": "now",
            "o": "on",
        }

        url = ENDPOINTS["standard"]
        return self.get(url, params=params)

    def get_shabbos_times(self, zip: str = "07621", date: datetime.date = datetime.date.today()):
        """ Get shabbos times """
        params = {
            "cfg": "json",
            "m": 42,
            "b": 18,
            "a": "on",
            "leyning": "off",
            "geo": "zip",
            "zip": zip,
            "gy": date.year,
            "gm": date.month,
            "gd": date.day,
        }

        url = ENDPOINTS["shabbat"]
        return self.get(url, params=params)

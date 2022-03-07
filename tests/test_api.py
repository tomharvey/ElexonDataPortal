from ElexonDataPortal.api import Client


def test_api_b1770():

    client = Client()

    start_date = "2022-01-01 00:00:00"
    end_date = "2022-01-01 01:00:00"

    r = client.get_B1770(start_date=start_date, end_date=end_date)

    assert len(r) == 4
    # There seems to be 2 for each SP


def test_api_dersysdata():
    client = Client()

    start_date = "2022-01-01"
    end_date = "2022-02-01"

    r = client.get_DERSYSDATA(start_date=start_date, end_date=end_date)

    assert len(r) == 32 * 48
    # one for each SP in Janurary and on 1st Feb


def test_api_rolsysdem():
    client = Client()

    start_date = "2022-02-01 00:00:00"
    end_date = "2022-02-02 00:00:00"

    r = client.get_ROLSYSDEM(FromDateTime=start_date, ToDateTime=end_date)

    assert len(r) == 289
    # one for each SP in Janurary and on 1st Feb

import pytest

from src.models.models import NodalCalcResponse
from src.calculations.nodal import calc_nodal


@pytest.fixture
def generate_data_for_tests():
    return {
        "vlp": {
            "q_liq": [0, 30, 60, 90, 120, 150],
            "p_wf": [200, 190, 180, 175, 185, 200]
        },
        "ipr": {
            "q_liq": [0, 30, 60, 90, 120, 150],
            "p_wf": [200, 180, 160, 140, 120, 100]
            }
    }


def test_calc_model_success(api_client, generate_data_for_tests):
    expected_result = NodalCalcResponse.parse_obj(
        calc_nodal(**generate_data_for_tests)
    ).dict()["__root__"]

    actual_result = api_client.post(
        "http://localhost:8003/nodal/calc",
        json=generate_data_for_tests
    ).text
    a = actual_result
    assert eval(actual_result) == expected_result

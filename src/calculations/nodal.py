from shapely.geometry import LineString
import numpy as np


def calc_nodal(vlp: dict, ipr: dict):
    """
    Расчёт точки пересечения VLP vs IPR

    Parameters
    ----------
    vlp : dict
        Словарь, содержащий VLP
    ipr : dict
        Словарь, содержащий IPR
    """
    # Можно использовать numpy или библиотеку Shapely, LineString intersection

    vlp_curve = LineString(np.column_stack((vlp["q_liq"], vlp["p_wf"])))
    ipr_curve = LineString(np.column_stack((ipr["q_liq"], ipr["p_wf"])))
    intersection = vlp_curve.intersection(ipr_curve)
    q_liq, p_wf = intersection.xy

    return [
        {
            "p_wf": list(p_wf)[0],
            "q_liq": list(q_liq)[0]
        }
    ]


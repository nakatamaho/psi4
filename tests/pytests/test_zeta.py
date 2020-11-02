import pytest

from .utils import *

import psi4
import numpy as np

pytestmark = pytest.mark.skip

ref = {
    "conv": {
        "ene": {
            "d": -100.01941126909895,
            "t": -100.05801143109962,
            "q": -100.06768524807164,
            "5": -100.0704303543983,
            "6": -100.07073832974459,
            "7": -100.07079540040381,
        },
        "grd": {
            "d": np.array([[0, 0, -1.97897507e-02], [0, 0, 1.97897507e-02]]),
            "t": np.array([[0, 0, -2.44719827e-02], [0, 0, 2.44719827e-02]]),
            "q": np.array([[0, 0, -2.56632476e-02], [0, 0, 2.56632476e-02]]),
            "5": np.array([[0, 0, -2.55690860e-02], [0, 0, 2.55690860e-02]]),
            "6": np.array([[0, 0, -2.55202901e-02], [0, 0, 2.55202901e-02]]),
            "7": np.array([[0, 0, -2.54893228e-02], [0, 0, 2.54893228e-02]]),
        },
        "hss": {
            "d": np.array(
                [
                    [1.14201580e-02, 2.88636997e-16, 3.97687335e-16, -1.14201580e-02, -2.78228656e-16, -3.97687335e-16],
                    [2.88636997e-16, 1.14201580e-02, -5.22281113e-16, -3.80143660e-16, -1.14201580e-02, 5.22281113e-16],
                    [3.97687335e-16, -5.22281113e-16, 6.37133401e-01, -3.97687335e-16, 5.22281113e-16, -6.37133401e-01],
                    [-1.14201580e-02, -3.80143660e-16, -3.97687335e-16, 1.14201580e-02, 3.58459616e-16, 3.97687335e-16],
                    [-2.78228656e-16, -1.14201580e-02, 5.22281113e-16, 3.58459616e-16, 1.14201580e-02, -5.22281113e-16],
                    [-3.97687335e-16, 5.22281113e-16, -6.37133401e-01, 3.97687335e-16, -5.22281113e-16, 6.37133401e-01],
                ]
            ),
            "t": np.array(
                [
                    [1.41221543e-02, 3.43562420e-15, -5.56983751e-16, -1.41221543e-02, -8.82111243e-16, 5.56983751e-16],
                    [3.43562420e-15, 1.41221543e-02, -5.72652355e-16, -4.26135257e-15, -1.41221543e-02, 5.72652355e-16],
                    [-5.56983751e-16, -5.72652355e-16, 6.33543175e-01, 5.56983751e-16, 5.72652355e-16, -6.33543175e-01],
                    [-1.41221543e-02, -4.26135257e-15, 5.56983751e-16, 1.41221543e-02, 1.60375621e-15, -5.56983751e-16],
                    [-8.82111243e-16, -1.41221543e-02, 5.72652355e-16, 1.60375621e-15, 1.41221543e-02, -5.72652355e-16],
                    [5.56983751e-16, 5.72652355e-16, -6.33543175e-01, -5.56983751e-16, -5.72652355e-16, 6.33543175e-01],
                ]
            ),
            "q": np.array(
                [
                    [1.48096027e-02, -5.90539645e-15, 9.84881270e-16, -1.48096027e-02, 4.75007061e-15, -9.84881270e-16],
                    [-5.90539645e-15, 1.48096027e-02, 9.45937039e-17, 1.76222627e-15, -1.48096027e-02, -9.45937039e-17],
                    [9.84881270e-16, 9.45937039e-17, 6.27190954e-01, -9.84881270e-16, -9.45937039e-17, -6.27190954e-01],
                    [-1.48096027e-02, 1.76222627e-15, -9.84881270e-16, 1.48096027e-02, -7.22703890e-15, 9.84881270e-16],
                    [4.75007061e-15, -1.48096027e-02, -9.45937039e-17, -7.22703890e-15, 1.48096027e-02, 9.45937039e-17],
                    [-9.84881270e-16, -9.45937039e-17, -6.27190954e-01, 9.84881270e-16, 9.45937039e-17, 6.27190954e-01],
                ]
            ),
            "5": np.array(
                [
                    [1.47552645e-02, 2.85244420e-13, 4.57266232e-16, -1.47552645e-02, -4.56798164e-13, -4.57266234e-16],
                    [2.85244420e-13, 1.47552645e-02, 4.63692795e-16, -2.69798442e-13, -1.47552645e-02, -4.63692795e-16],
                    [4.57266232e-16, 4.63692795e-16, 6.26827336e-01, -4.57266233e-16, -4.63692795e-16, -6.26827336e-01],
                    [
                        -1.47552645e-02,
                        -2.69798442e-13,
                        -4.57266233e-16,
                        1.47552645e-02,
                        -1.26964042e-13,
                        4.57266233e-16,
                    ],
                    [
                        -4.56798164e-13,
                        -1.47552645e-02,
                        -4.63692795e-16,
                        -1.26964042e-13,
                        1.47552645e-02,
                        4.63692795e-16,
                    ],
                    [-4.57266234e-16, -4.63692795e-16, -6.26827336e-01, 4.57266233e-16, 4.63692795e-16, 6.26827336e-01],
                ]
            ),
            "6": np.array(
                [
                    [
                        1.47271054e-02,
                        -3.46663981e-13,
                        -6.58652686e-17,
                        -1.47271054e-02,
                        -4.04281331e-13,
                        6.58652675e-17,
                    ],
                    [-3.46663981e-13, 1.47271054e-02, 9.55744800e-16, 1.12365491e-14, -1.47271054e-02, -9.55744797e-16],
                    [-6.58652686e-17, 9.55744800e-16, 6.26683611e-01, 6.58652679e-17, -9.55744800e-16, -6.26683610e-01],
                    [-1.47271054e-02, 1.12365491e-14, 6.58652679e-17, 1.47271054e-02, 5.85830351e-14, -6.58652754e-17],
                    [-4.04281331e-13, -1.47271054e-02, -9.55744800e-16, 5.85830351e-14, 1.47271054e-02, 9.55744798e-16],
                    [6.58652675e-17, -9.55744797e-16, -6.26683610e-01, -6.58652754e-17, 9.55744798e-16, 6.26683610e-01],
                ]
            ),
            # "7": np.zeros(36).reshape((6, 6)),
        },
    },
    "df": {
        "ene": {
            "d": -100.01940060570712,
            "t": -100.05800433992121,
            "q": -100.06768368288756,
            "5": -100.0704283042375,
            "6/5": -100.07073665835942,
            "6": -100.07073587640389,
            "7/6": -100.07079295732615,
            # "7": 0.0,
        },
        "grd": {
            "d": np.array([[0, 0, -1.97887695e-02], [0, 0, 1.97887695e-02]]),
            "t": np.array([[0, 0, -2.44674251e-02], [0, 0, 2.44674251e-02]]),
            "q": np.array([[0, 0, -2.56623539e-02], [0, 0, 2.56623539e-02]]),
            "5": np.array([[0, 0, -2.55665605e-02], [0, 0, 2.55665605e-02]]),
            "6/5": np.array([[0, 0, -2.55170642e-02], [0, 0, 2.55170642e-02]]),
            "6": np.array([[0, 0, -2.55207994e-02], [0, 0, 2.55207994e-02]]),
            "7/6": np.array([[0, 0, -2.54898158e-02], [0, 0, 2.54898158e-02]]),
            # "7": np.zeros(6).reshape(2, 3),
        },
        "hss": {
            "d": np.array(
                [
                    [1.14195918e-02, -8.20455290e-15, 8.48376579e-16, -1.14195918e-02, 1.01425643e-14, -8.48376580e-16],
                    [-8.20455290e-15, 1.14195918e-02, 7.87137296e-16, 8.63378854e-15, -1.14195918e-02, -7.87137294e-16],
                    [8.48376579e-16, 7.87137296e-16, 6.37098987e-01, -8.48376579e-16, -7.87137296e-16, -6.37098987e-01],
                    [-1.14195918e-02, 8.63378854e-15, -8.48376579e-16, 1.14195918e-02, -8.52027257e-15, 8.48376579e-16],
                    [1.01425643e-14, -1.14195918e-02, -7.87137296e-16, -8.52027257e-15, 1.14195918e-02, 7.87137295e-16],
                    [-8.48376580e-16, -7.87137294e-16, -6.37098987e-01, 8.48376579e-16, 7.87137295e-16, 6.37098987e-01],
                ]
            ),
            "t": np.array(
                [
                    [1.41195242e-02, -1.44279825e-13, -2.62663252e-16, -1.41195242e-02, 2.52178758e-13, 2.62663246e-16],
                    [-1.44279825e-13, 1.41195242e-02, 7.25775059e-16, 1.88123226e-13, -1.41195242e-02, -7.25775063e-16],
                    [-2.62663252e-16, 7.25775059e-16, 6.33561555e-01, 2.62663253e-16, -7.25775060e-16, -6.33561555e-01],
                    [-1.41195242e-02, 1.88123226e-13, 2.62663253e-16, 1.41195242e-02, -3.52532511e-13, -2.62663248e-16],
                    [2.52178758e-13, -1.41195242e-02, -7.25775060e-16, -3.52532511e-13, 1.41195242e-02, 7.25775063e-16],
                    [2.62663246e-16, -7.25775063e-16, -6.33561555e-01, -2.62663248e-16, 7.25775063e-16, 6.33561555e-01],
                ]
            ),
            "q": np.array(
                [
                    [1.48090869e-02, 2.05969460e-14, -1.49618888e-15, -1.48090869e-02, 3.81831832e-14, 1.49618913e-15],
                    [2.05969460e-14, 1.48090870e-02, -9.64983006e-16, 1.26240566e-13, -1.48090869e-02, 9.64982950e-16],
                    [-1.49618888e-15, -9.64983006e-16, 6.27200845e-01, 1.49618893e-15, 9.64982952e-16, -6.27200845e-01],
                    [-1.48090869e-02, 1.26240566e-13, 1.49618893e-15, 1.48090869e-02, -8.38158432e-14, -1.49618905e-15],
                    [3.81831832e-14, -1.48090869e-02, 9.64982952e-16, -8.38158432e-14, 1.48090869e-02, -9.64982956e-16],
                    [1.49618913e-15, 9.64982950e-16, -6.27200845e-01, -1.49618905e-15, -9.64982956e-16, 6.27200845e-01],
                ]
            ),
            "5": np.array(
                [
                    [1.47538071e-02, 5.47383498e-13, -1.15209254e-15, -1.47538071e-02, -2.32833029e-13, 1.15209256e-15],
                    [5.47383498e-13, 1.47538071e-02, 4.09315798e-16, -5.13303988e-13, -1.47538071e-02, -4.09315765e-16],
                    [-1.15209254e-15, 4.09315798e-16, 6.26827395e-01, 1.15209262e-15, -4.09316413e-16, -6.26827395e-01],
                    [-1.47538071e-02, -5.13303988e-13, 1.15209262e-15, 1.47538071e-02, 4.11866032e-13, -1.15209258e-15],
                    [-2.32833029e-13, -1.47538071e-02, -4.09316413e-16, 4.11866032e-13, 1.47538071e-02, 4.09315929e-16],
                    [1.15209256e-15, -4.09315765e-16, -6.26827395e-01, -1.15209258e-15, 4.09315929e-16, 6.26827395e-01],
                ]
            ),
            "6/5": np.array(
                [
                    [1.47252438e-02, 5.92051339e-14, -1.14461969e-15, -1.47252438e-02, 5.68396132e-14, 1.14461967e-15],
                    [5.92051339e-14, 1.47252438e-02, 6.43834765e-16, -9.29323460e-14, -1.47252437e-02, -6.43834148e-16],
                    [-1.14461969e-15, 6.43834765e-16, 6.26683723e-01, 1.14461973e-15, -6.43834668e-16, -6.26683723e-01],
                    [-1.47252438e-02, -9.29323460e-14, 1.14461973e-15, 1.47252438e-02, 3.73113650e-14, -1.14461967e-15],
                    [5.68396132e-14, -1.47252437e-02, -6.43834668e-16, 3.73113650e-14, 1.47252438e-02, 6.43834161e-16],
                    [1.14461967e-15, -6.43834148e-16, -6.26683723e-01, -1.14461967e-15, 6.43834161e-16, 6.26683723e-01],
                ]
            ),
            # "6": np.zeros(36).reshape((6, 6)),
            # "7/6": np.zeros(36).reshape((6, 6)),
            # "7": np.zeros(36).reshape((6, 6)),
        },
    },
}


# hand-adjust zetas -- what to pass/xfail/fail is NOT read from Libint2 config
# * @pytest.mark.parametrize("zeta", ["d", "t", "q", "5"])
@pytest.mark.parametrize("zeta", ["d", "t", "q", "5", "6/5", "6", "7/6", "7"])
@pytest.mark.parametrize("scftype", ["conv", "df"])
@pytest.mark.parametrize("der", ["ene", "grd", "hss"])
def test_zeta(scftype, zeta, der, request):

    if zeta not in ref[scftype][der]:
        pytest.skip()

    hf = psi4.geometry(
        """
        H    0.          0.         -1.64558411
        F    0.          0.          0.08729475
        symmetry c1
        units bohr
    """
    )

    if zeta in "dtq56":
        basis = f"cc-pv{zeta}z"
    elif zeta == "6/5":
        basis = "cc-pv6z"
    elif zeta in ["7/6", "7"]:
        basis = "7zapa-nr"

    psi4.set_options(
        {
            # "e_convergence": 10,
            # "d_convergence": 9,
            "scf_type": {
                "df": "df",
                "conv": "direct",
            }[scftype],
            "basis": basis,
        }
    )

    df_basis_scf = None
    if scftype == "df":
        if zeta in "dtq5":
            df_basis_scf = f"cc-pv{zeta}z-jkfit"
        elif zeta == "6/5":
            df_basis_scf = "cc-pv5z-jkfit"
        elif zeta in ["6", "7/6"]:
            df_basis_scf = "cc-pv6z-ri"
    elif scftype == "conv":
        # * only used for preiterations
        # * 7zapa gets aug-cc-pv6z-ri by default
        if zeta == "6":
            df_basis_scf = "cc-pv6z-ri"
    if df_basis_scf:
        psi4.set_options({"df_basis_scf": df_basis_scf})

    if der == "hss":
        kwargs = {"ref_gradient": psi4.core.Matrix.from_array(ref[scftype]["grd"][zeta])}
    else:
        kwargs = {}

    ans, wfn = {"ene": psi4.energy, "grd": psi4.gradient, "hss": psi4.hessian,}[
        der
    ]("hf", return_wfn=True, **kwargs)
    if isinstance(ans, float):
        print(ans)
    else:
        print(ans.np)

    assert compare_values(ref[scftype][der][zeta], ans, 6, f"Hartree--Fock {scftype} {der} {zeta}-zeta")

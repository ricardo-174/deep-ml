from typing import Optional, Union

try:
    import numpy as np
except Exception:
    np = None

ArrayLike = Union[list, "np.ndarray"]

def flow_epe(pred: ArrayLike,
             gt: ArrayLike,
             mask: Optional[ArrayLike] = None,
             max_flow: Optional[float] = None) -> float:
    pred = np.asarray(pred,dtype=np.float64)
    gt = np.asarray(gt,dtype=np.float64)
    if pred.shape != gt.shape or pred.ndim !=3 or pred.shape[-1] != 2:
        return -1
    e = np.sqrt(((pred - gt) ** 2).sum(axis=-1))
    if max_flow != None:
        e = np.minimum(e,max_flow)
    vaild = np.isfinite(e)
    if mask is not None:
        m = np.asarray(mask,dtype=np.float64)
        if m.size != e.size:
            try:
                m = np.broadcast_to(m,e.shape)
            except ValueError:
                return -1
        m = m.reshape(e.shape)    
        vaild &= m>0.5
    if not vaild.any():
        return -1
    return float(e[vaild].mean())
    pass
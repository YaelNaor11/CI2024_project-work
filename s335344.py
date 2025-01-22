import numpy as np


def f1(x: np.ndarray) -> np.ndarray:
  return np.sin(x[0])


def f2(x: np.ndarray) -> np.ndarray:
  return (np.power(-35.77865211740968, 4) * (np.cos(((x[1] + x[2]) * (0.049825662719513275 * x[0]))) * x[0]))


def f3(x: np.ndarray) -> np.ndarray:
  return ((np.power((x[2] + (-0.15334261790093606 + -1.3457410645123407)), 2) + np.power((-1.1840450316899656 * x[0]), 2)) + ((x[2] - (np.power(x[1], 2) + x[2])) * x[1]))


def f4(x: np.ndarray) -> np.ndarray:
  return ((np.cos(x[1]) * 3.167794160296859) + ((np.cos(x[1]) * 3.167794160296859) + 2.6422928296213577))


def f5(x: np.ndarray) -> np.ndarray:
  return (x[1] - x[1])


def f6(x: np.ndarray) -> np.ndarray:
  return ((-0.585796320561327 * x[0]) + (x[1] + x[1]))


def f7(x: np.ndarray) -> np.ndarray:
  return np.power(((x[1] * (x[0] * (x[1] + x[0]))) * np.sin(x[0])), 2)


def f8(x: np.ndarray) -> np.ndarray:
  return np.power((np.cos((np.power(np.arctan(x[5]), 3) + -5.240068819211974)) + (4.647572411669573 * x[5])), 3)


import pytest
from optimizador.modules.OptimizationModel import OptimizationModel

headers = ['Product_A_Production_Time_Machine_1', 'Product_A_Production_Time_Machine_2', 'Product_B_Production_Time_Machine_1', 'Product_B_Production_Time_Machine_2', 'Machine_1_Available_Hours', 'Machine_2_Available_Hours', 'Price_Product_A', 'Price_Product_B']
values = ['3.5', '4.0', '3.0', '3.5', '11.0', '13.0', '130', '110']

def test_optimizacion():
    optimizador = OptimizationModel(headers, values)
    res = optimizador.procesar()
    
    assert res.x[0] == 3.142857142857143
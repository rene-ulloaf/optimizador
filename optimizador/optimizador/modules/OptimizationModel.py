from scipy.optimize import linprog
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

class OptimizationModel:
    datosDict = {}
    res = ""
    
    def __init__(self, headers, values):        
        self.datosDict = dict(zip(headers, map(float, values)))
        
    def procesar(self):
        c = [self.datosDict['Price_Product_A']*-1, self.datosDict['Price_Product_B']*-1]
        A = [
            [self.datosDict['Product_A_Production_Time_Machine_1'], self.datosDict['Product_B_Production_Time_Machine_1']],
            [self.datosDict['Product_A_Production_Time_Machine_2'], self.datosDict['Product_B_Production_Time_Machine_2']],
        ]
        b = [self.datosDict['Machine_1_Available_Hours'], self.datosDict['Machine_2_Available_Hours']]
        x_bounds = [(0, None), (0, None)]

        self.res = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')
        return self.res
    
    def grafico(self):
        b = [self.datosDict['Machine_1_Available_Hours'], self.datosDict['Machine_2_Available_Hours']]
        x_vals = np.linspace(0, 10, 300)
        y1 = (b[0] - self.datosDict['Product_A_Production_Time_Machine_1'] * x_vals) / self.datosDict['Product_B_Production_Time_Machine_1']
        y2 = (b[1] - self.datosDict['Product_A_Production_Time_Machine_2'] * x_vals) / self.datosDict['Product_B_Production_Time_Machine_2']

        plt.figure(figsize=(10, 6))
        plt.plot(x_vals, y1, label="1.5A + 1.0B ≤ 8 (Máquina 1)")
        plt.plot(x_vals, y2, label="2.0A + 1.5B ≤ 10 (Máquina 2)")
        plt.fill_between(x_vals, 0, np.minimum(y1, y2), where=(y1 >= 0) & (y2 >= 0), color='lightgray', label='Región factible')

        x_opt, y_opt = self.res.x
        plt.plot(x_opt, y_opt, 'ro', label='Solución óptima')
        plt.text(x_opt + 0.2, y_opt, f"({x_opt:.2f}, {y_opt:.2f})", color='red')
            
        plt.xlim(0, 10)
        plt.ylim(0, 10)
        plt.xlabel("Unidades de Producto A")
        plt.ylabel("Unidades de Producto B")
        plt.title("Optimización de Producción: Región Factible y Solución Óptima")
        plt.legend()
        plt.grid(True)
        
        buffer = io.BytesIO()
        plt.tight_layout()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        return base64.b64encode(image_png).decode('utf-8')
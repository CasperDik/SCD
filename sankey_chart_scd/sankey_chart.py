import plotly.graph_objects as go
import pandas as pd

df = pd.read_excel("sankey_flow_data.xlsx", sheet_name="Sheet2")
x = df["flow"].tolist()

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad=20,
      thickness=10,
      line=dict(color = "black", width = 0.5),
      label=["CORINTHOS REFINERIES S.A.", "SOUTH REFINERIES COMPLEX – ELEFSIS INDUSTRIAL FACILITIES", "TITAN CEMENT S.A. - KAMARI PLANT", "HERACLES G.C.Co, VOLOS PLANT", "INDUSTRIAL DIVISION OF ASPROPYRGOS", "Emitted", "Ledra Ltd", "B.H.P. Co. Ltd", "Novamix", "Vimatec", "Gavriel Ltd", "Vellis Chemicals Ltd", "MOTOR OIL Hellas", "Hellenic Petroleum", "Storage_Cluster"],
      color="blue"
    ),         
    link=dict(
      source=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
      target=[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
      value=x
  ))])

fig.update_layout(title_text="CO2 flow", font_size=10)
fig.write_image("fig1.png")

fig.show()

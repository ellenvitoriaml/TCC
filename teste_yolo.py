from ultralytics import YOLO

modelo = YOLO("yolo11n.pt")
resultados = modelo.predict(source="teste.jpg", save=True, show=False)

for r in resultados:
    print(f"Objetos detectados: {len(r.boxes)}")
    for box in r.boxes:
        print(f"  Classe: {int(box.cls.item())} | Confiança: {float(box.conf.item()):.2f}")

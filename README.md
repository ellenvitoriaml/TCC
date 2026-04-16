# TCC — Autenticação Biométrica Local

Sistema de controle de acesso por reconhecimento facial. Tudo roda localmente no Raspberry Pi 5, sem nuvem.

**Aluna:** Ellen Vitória Menezes Lima  
**Orientador:** Prof. Dr. Hendrik Macedo  
**UFS — STI/DCOMP | Abril–Julho 2026**

## O que o sistema faz
Detecta e reconhece rostos em tempo real usando YOLOv11 e FaceNet. Se a pessoa estiver cadastrada, envia sinal para o Arduino acionar a tranca. Tudo armazenado localmente em SQLite — nenhuma imagem é salva, só os vetores.

## Tecnologias
- YOLOv11 nano — detecção facial
- FaceNet — embeddings
- SQLite — banco local
- Arduino — atuação física via serial

## Como rodar
```bash
python3 -m venv tcc-env
source tcc-env/bin/activate
pip install -r requirements.txt
python3 teste_yolo.py
```

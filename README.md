# Monitor de Proyectos — Modo SEGURO (solo Google News RSS)

Esta versión evita scrapers y usa **solo Google News RSS**, que es la fuente más estable.
Incluye **logging detallado** y un script `test_feed.py` para verificar tu conexión.

## Paso 1 — Ejecutar
```bash
pip install -r requirements.txt
python pipeline.py
```
Abre `output/mapa_proyectos.html` y `output/proyectos.csv`

## Paso 2 — Si “no trae nada”
1) Prueba el tester:
```bash
python test_feed.py
```
   - Deberías ver títulos; si falla tu red/bloqueo corporativo, Google News puede estar filtrado.
2) Cambia a otra región/idioma en `config/feeds_rss.yaml` (p.ej. `hl=en`, `gl=US`, `ceid=US:en`).
3) Reduce filtros del query (quita ciudades o países) para ver si llega contenido.

## Personaliza queries
Edita `config/feeds_rss.yaml`. Cada entrada es una búsqueda de Google News transformada a RSS.

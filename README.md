# moonglaive
Three-bladed weapon of the night elf Sentinels

### Installation

```bash
pip3 install moonglaive
```

### Usage

```bash
python3 -m moonglaive --active --upcoming

+------------+---------------------------------+-------+----------+
| platform   | title                           |   eta |   reward |
+============+=================================+=======+==========+
| Code4rena  | Party Protocol - Versus contest |    6- |  $56,500 |
+------------+---------------------------------+-------+----------+
| Code4rena  | Rubicon v2                      |    5- |  $60,500 |
+------------+---------------------------------+-------+----------+
| Code4rena  | Caviar Private Pools            |    5- |  $47,000 |
+------------+---------------------------------+-------+----------+
| Code4rena  | Frankencoin                     |    4+ |  $60,500 |
+------------+---------------------------------+-------+----------+
| Sherlock   | Notional Update #3              |    1+ |  $16,000 |
+------------+---------------------------------+-------+----------+
| Sherlock   | Notional V3                     |   36- | $164,000 |
+------------+---------------------------------+-------+----------+
```

Negative ETA means "days remaining", while Positive ETA menas "days to start"

### Publishing

```
# update setup.py version
python3 setup.py sdist
python3 -m twine upload dist/*
```
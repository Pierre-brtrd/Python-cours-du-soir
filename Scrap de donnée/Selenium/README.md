# Scrapping de donnée avec Sélénium

Pour pouvoir effectuer le scrap de donnée avec Sélénium, vous devez avoir Docker pour build un image configurée avec les chromes options.

## Build de l'image Docker

Pour build l'image Docker, vous devez ouvrir un terminal de commande à l'emplacement du fichier `docker-compose.yml` et entrer la commande

```bash
docker-compose up -d
```

Une fois que l'image est buildée et que votre container est lancé, vous devez entrer la commande dans un terminal :

```bash
docker exec -it scrap-data bash
```

Vous serez ensuite dans le terminal bash de votre container, vous devrez vous rendre dans le dossier où sont placés vos scripts python :

```bash
cd scrap
```

Ensuite vous pourrez lancer votre script sur le container grâce à la commande :

```bash
python3 votreScript.py
```

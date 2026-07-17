# Déploiement Linode — spm.harounc.com

Prévu pour Ubuntu 24.04, Nginx, PostgreSQL, Gunicorn et Certbot. L’application système, la base et le service sont nommés `spm`. Le DNS `spm.harounc.com` doit pointer vers `172.104.159.89`.

## 1. Paquets et utilisateur système

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-venv python3-pip postgresql nginx certbot python3-certbot-nginx git
sudo adduser --system --group --home /srv/spm spm
sudo mkdir -p /srv/spm
sudo chown -R spm:www-data /srv/spm
```

## 2. Base PostgreSQL

```bash
sudo -u postgres psql
CREATE USER spm WITH PASSWORD 'MOT_DE_PASSE_FORT';
CREATE DATABASE spm OWNER spm;
\q
```

## 3. Application

Copier ou cloner le projet dans `/srv/spm`, puis :

```bash
cd /srv/spm
sudo -u spm python3 -m venv .venv
sudo -u spm .venv/bin/pip install -r requirements.txt
sudo cp .env.production.example /etc/spm.env
sudo chmod 640 /etc/spm.env
sudo chown root:spm /etc/spm.env
sudo editor /etc/spm.env
sudo -u spm bash -c 'set -a; source /etc/spm.env; .venv/bin/python manage.py migrate'
sudo -u spm bash -c 'set -a; source /etc/spm.env; .venv/bin/python manage.py collectstatic --noinput'
sudo -u spm bash -c 'set -a; source /etc/spm.env; .venv/bin/python manage.py createsuperuser'
```

Ne jamais conserver les valeurs d’exemple de `DJANGO_SECRET_KEY` et `DB_PASSWORD`.

## 4. Gunicorn et Nginx

```bash
sudo cp deploy/gunicorn.service /etc/systemd/system/spm.service
sudo systemctl daemon-reload
sudo systemctl enable --now spm
sudo cp deploy/nginx-spm.harounc.com.conf /etc/nginx/sites-available/spm.harounc.com
sudo ln -s /etc/nginx/sites-available/spm.harounc.com /etc/nginx/sites-enabled/spm.harounc.com
sudo nginx -t
sudo systemctl reload nginx
```

Supprimer ou désactiver l’ancien bloc Nginx qui répond pour `harounc.com` s’il entre en conflit.

## 5. HTTPS

```bash
sudo certbot --nginx -d spm.harounc.com --redirect
sudo certbot renew --dry-run
```

Certbot doit être exécuté après la propagation DNS et avant la mise en ligne finale.

## 6. Contrôles

```bash
sudo -u spm bash -c 'set -a; source /etc/spm.env; .venv/bin/python manage.py check --deploy'
sudo systemctl status spm --no-pager
sudo journalctl -u spm -n 100 --no-pager
curl -I https://harounc.com
```

Prévoir des sauvegardes quotidiennes de PostgreSQL et du dossier `/srv/spm/media`.

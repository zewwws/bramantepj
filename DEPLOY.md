# Deploying the demo

Two options: **PythonAnywhere** (a permanent link the client can open any time) or a
**Cloudflare quick tunnel** (a temporary link to your own PC, for a live demo).

Replace `USERNAME` below with your PythonAnywhere username. The site will be at
`https://USERNAME.pythonanywhere.com`.

## PythonAnywhere (free plan)

### 1. Get the code

Create a free ("Beginner") account at https://www.pythonanywhere.com, then open
**Consoles → Bash** and run:

```bash
git clone https://github.com/zewwws/bramantepj.git
cd bramantepj
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
python -c "import secrets; print(secrets.token_urlsafe(50))"   # copy this: it's the secret key
```

If the GitHub repository is private, `git clone` asks for a password: use a GitHub
personal access token (GitHub → Settings → Developer settings → Tokens) instead of
your account password.

### 2. Create the web app

**Web → Add a new web app → Manual configuration → Python 3.12**. Then, on the Web tab:

- **Virtualenv:** `/home/USERNAME/bramantepj/.venv`
- **Static files** (add two entries):

  | URL        | Directory                                |
  |------------|------------------------------------------|
  | `/static/` | `/home/USERNAME/bramantepj/staticfiles`  |
  | `/media/`  | `/home/USERNAME/bramantepj/media`        |

- **Force HTTPS:** on

### 3. Edit the WSGI file

Click the **WSGI configuration file** link on the Web tab, delete everything in it and
paste this, filling in the secret key you generated:

```python
import os
import sys

path = '/home/USERNAME/bramantepj'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'br_core.settings'
os.environ['DJANGO_SECRET_KEY'] = 'PASTE-THE-GENERATED-KEY-HERE'
os.environ['DJANGO_DEBUG'] = '0'
os.environ['DJANGO_ALLOWED_HOSTS'] = 'USERNAME.pythonanywhere.com'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

Save, go back to the Web tab and click **Reload**. The site is live.

### Updating the demo after changes

After pushing new commits from your PC, in a PythonAnywhere Bash console:

```bash
cd ~/bramantepj
source .venv/bin/activate
git pull
python manage.py migrate
python manage.py collectstatic --noinput
```

Then click **Reload** on the Web tab.

### Notes

- The free plan expires unless you log in and click **"Run until 3 months from today"**
  on the Web tab every 3 months.
- The database on PythonAnywhere is separate from your local one: products edited
  and contact requests received there stay there.

## Cloudflare quick tunnel (temporary)

Works only while your PC and the server are running; the link changes every time.

```powershell
winget install Cloudflare.cloudflared
$env:DJANGO_ALLOWED_HOSTS = ".trycloudflare.com,localhost,127.0.0.1"
.venv\Scripts\python manage.py runserver 8765
```

In a second terminal:

```powershell
cloudflared tunnel --url http://localhost:8765
```

Send the client the `https://….trycloudflare.com` link it prints.

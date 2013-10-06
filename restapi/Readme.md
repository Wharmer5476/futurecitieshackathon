### Running the api

```
export futurecities_db_user=...
export futurecities_db_pass=...

cd futurecitieshackathon/restapi
pip install -r requirements.txt
# for development
python api.py
# OR run daemonized using gunicorn
gunicorn -w 4 -b 127.0.0.1:5000 api:app -D
````

Installed python-pip and virtualenvwrapper.


Commands for DEMO/Container (only requires Docker):
1. git clone https://github.com/esteininger/mdb-hackathon-search-team.git
2. cd mdb-hackathon-search-team/
3. docker build . -t mdb-cinnamon
4. docker run -p 5010:5010 mdb-cinnamon
5. http://127.0.0.1:5010

Commands for DEVELOPMENT (requires Python/virtualenv):
1. virtualenv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python manage.py

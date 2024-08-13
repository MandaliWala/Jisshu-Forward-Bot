echo "Cloning Repo...."
if [ -z $BRANCH ]
then
  echo "Cloning main branch...."
  git clone https://github.com/MandaliWala/Jisshu-forward-bot MandaliWala/Jisshu-forward-bot 
else
  echo "Cloning $BRANCH branch...."
  git clone https://github.com/MandaliWala/Jisshu-forward-bot -b $BRANCH /Jisshu-forward-bot
fiJisshubot
cd MandaliWala/Jisshu-forward-bot 
pip3 install -U -r requirements.txt
echo "Starting Bot...."
gunicorn app:app & python3 main.py
